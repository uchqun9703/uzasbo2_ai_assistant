"""
UzASBO 2.0 AI Assistant — WebSocket handler

WebSocket — server va foydalanuvchi o'rtasida doimiy ulanish.
Oddiy HTTP da: so'rov → javob → ulanish yopiladi.
WebSocket da: ulanish ochiq qoladi, ikkala tomon istalgan vaqtda xabar yuborishi mumkin.

Bu foydalanuvchiga "ChatGPT effekti" beradi:
AI javobni token-by-token (so'z-so'z) yuboradi,
foydalanuvchi yozilayotganini real-time ko'radi.
"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from loguru import logger
import json
import uuid

from app.core.rag_engine import RAGEngine
from app.models.chat_history import ChatHistoryManager

# WebSocket endpointlar uchun router
ws_router = APIRouter()


class ConnectionManager:
    """
    WebSocket ulanishlarni boshqaruvchi.

    Bir vaqtda ko'plab foydalanuvchilar ulanishi mumkin.
    Bu klass barcha aktiv ulanishlarni kuzatib boradi.
    """

    def __init__(self):
        # Aktiv ulanishlar lug'ati: {session_id: WebSocket}
        # Har bir foydalanuvchining ulanishi session_id bilan saqlanadi
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, session_id: str):
        """
        Yangi ulanishni qabul qilish.
        Foydalanuvchi chat ochganda chaqiriladi.
        """
        # WebSocket ulanishni qabul qilamiz
        await websocket.accept()
        # Aktiv ulanishlar ro'yxatiga qo'shamiz
        self.active_connections[session_id] = websocket
        logger.info(f"WebSocket ulandi: session={session_id}")

    def disconnect(self, session_id: str):
        """
        Ulanishni yopish.
        Foydalanuvchi chat yopganda yoki internet uzilganda chaqiriladi.
        """
        if session_id in self.active_connections:
            del self.active_connections[session_id]
            logger.info(f"WebSocket uzildi: session={session_id}")

    async def send_token(self, session_id: str, token: str):
        """
        Bitta token (so'z bo'lagi) yuborish.
        AI javob generatsiya qilayotganda har bir yangi so'zni
        darhol foydalanuvchiga yuboradi.

        Masalan: "To'lov" → " topshiriqnomasi" → " yaratish" → " uchun..."
        """
        if session_id in self.active_connections:
            websocket = self.active_connections[session_id]
            await websocket.send_json({
                "type": "token",       # Xabar turi — yangi token
                "content": token,      # Token matni
            })

    async def send_complete(self, session_id: str, message_id: str,
                            sources: list, confidence: float):
        """
        Javob tugaganini bildirish.
        Barcha tokenlar yuborilgandan keyin chaqiriladi.
        Frontend bu signalni olib, "AI yozyapti..." animatsiyani to'xtatadi.
        """
        if session_id in self.active_connections:
            websocket = self.active_connections[session_id]
            await websocket.send_json({
                "type": "complete",         # Xabar turi — javob tugadi
                "message_id": message_id,   # Javob xabari ID si
                "sources": sources,         # Ishlatilgan manbalar
                "confidence": confidence,   # Ishonch darajasi
            })

    async def send_error(self, session_id: str, error_message: str):
        """
        Xatolik xabarini yuborish.
        AI javob bera olmasa, foydalanuvchiga xato xabarini ko'rsatamiz.
        """
        if session_id in self.active_connections:
            websocket = self.active_connections[session_id]
            await websocket.send_json({
                "type": "error",              # Xabar turi — xatolik
                "content": error_message,     # Xatolik matni
            })


# Global connection manager — barcha WebSocket lar shu orqali boshqariladi
manager = ConnectionManager()


# ============================================================
# WebSocket endpoint
# ws://localhost:8100/ws/chat?session_id=abc-123
# ============================================================

@ws_router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    """
    WebSocket orqali chat.

    Ishlash tartibi:
    1. Foydalanuvchi ulanadi (connect)
    2. Foydalanuvchi xabar yuboradi (JSON formatda)
    3. Server RAG Engine orqali javob generatsiya qiladi
    4. Javob token-by-token yuboriladi (streaming)
    5. Javob tugagach "complete" signal yuboriladi
    6. 2-5 qadamlar takrorlanadi (foydalanuvchi chat yopguncha)
    7. Foydalanuvchi uzilganda (disconnect) — resurslar tozalanadi

    Foydalanuvchi xabari formati (JSON):
    {
        "message": "Savolim...",
        "current_page": "/document/finance/paymentorder",
        "language": "uz_latn"
    }
    """
    # Sessiya ID ni query parametrdan olamiz yoki yangi yaratamiz
    # Misol: ws://localhost:8100/ws/chat?session_id=abc-123
    session_id = websocket.query_params.get("session_id", str(uuid.uuid4()))

    # Ulanishni qabul qilish
    await manager.connect(websocket, session_id)

    # RAG Engine va Chat History obyektlarini yaratish
    rag_engine = RAGEngine()
    chat_history = ChatHistoryManager()

    try:
        # Cheksiz tsikl — foydalanuvchi uzilguncha xabar kutamiz
        while True:
            # Foydalanuvchidan JSON xabar kutish
            # Bu qator foydalanuvchi xabar yuborguncha "kutib turadi"
            raw_data = await websocket.receive_text()

            try:
                # JSON ni Python dict ga aylantirish
                data = json.loads(raw_data)
            except json.JSONDecodeError:
                # Noto'g'ri JSON kelsa, xato yuboramiz
                await manager.send_error(session_id, "Noto'g'ri xabar formati")
                continue  # Keyingi xabarni kutish

            # Xabar matnini olish
            message = data.get("message", "").strip()
            if not message:
                await manager.send_error(session_id, "Xabar matni bo'sh")
                continue

            # Qo'shimcha parametrlar
            current_page = data.get("current_page")
            language = data.get("language", "uz_latn")

            logger.info(
                f"WS xabar: session={session_id}, "
                f"sahifa={current_page}, xabar={message[:50]}..."
            )

            # Foydalanuvchi xabarini tarixga saqlash
            user_msg_id = str(uuid.uuid4())
            await chat_history.save_message(
                session_id=session_id,
                message_id=user_msg_id,
                role="user",
                content=message,
            )

            try:
                # RAG Engine dan streaming javob olish
                # stream_answer — generator funksiya, har bir token ni
                # birma-bir qaytaradi (yield)
                full_answer = ""
                sources = []
                confidence = 0.0

                async for chunk in rag_engine.stream_answer(
                    question=message,
                    current_page=current_page,
                    language=language,
                    session_id=session_id,
                ):
                    if chunk["type"] == "token":
                        # Har bir tokenni foydalanuvchiga yuborish
                        await manager.send_token(session_id, chunk["content"])
                        full_answer += chunk["content"]
                    elif chunk["type"] == "metadata":
                        # Manbalar va ishonch darajasi
                        sources = chunk.get("sources", [])
                        confidence = chunk.get("confidence", 0.0)

                # Javobni tarixga saqlash
                assistant_msg_id = str(uuid.uuid4())
                await chat_history.save_message(
                    session_id=session_id,
                    message_id=assistant_msg_id,
                    role="assistant",
                    content=full_answer,
                )

                # Javob tugaganini bildirish
                await manager.send_complete(
                    session_id=session_id,
                    message_id=assistant_msg_id,
                    sources=sources,
                    confidence=confidence,
                )

            except Exception as e:
                logger.error(f"WS javob generatsiyada xato: {e}")
                await manager.send_error(
                    session_id,
                    "Javob generatsiya qilishda xatolik yuz berdi."
                )

    except WebSocketDisconnect:
        # Foydalanuvchi ulanishni yopdi (chat yopdi, sahifani tark etdi)
        manager.disconnect(session_id)
        logger.info(f"Foydalanuvchi uzildi: session={session_id}")
    except Exception as e:
        # Kutilmagan xatolik
        logger.error(f"WebSocket xatosi: {e}")
        manager.disconnect(session_id)
