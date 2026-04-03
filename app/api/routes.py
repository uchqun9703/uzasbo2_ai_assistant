"""
UzASBO 2.0 AI Assistant — REST API endpointlar

Bu fayl barcha HTTP endpointlarni belgilaydi.
Har bir endpoint foydalanuvchi so'rovini qabul qilib,
tegishli servisga yo'naltiradi va javobni qaytaradi.

Endpointlar:
    POST /api/chat/message     — Yangi xabar yuborish va javob olish
    GET  /api/chat/history/{id} — Chat tarixini olish
    DELETE /api/chat/history/{id} — Chat tarixini o'chirish
    POST /api/feedback          — Javobga baho berish (👍/👎)
    GET  /health                — Tizim holati tekshiruvi
"""

from fastapi import APIRouter, HTTPException, Depends
from loguru import logger
import uuid

from app.models.schemas import (
    ChatMessageRequest,
    ChatMessageResponse,
    ChatHistoryResponse,
    FeedbackRequest,
    HealthResponse,
)
from app.core.rag_engine import RAGEngine
from app.models.chat_history import ChatHistoryManager

# ============================================================
# Router yaratish
# prefix="/api" — barcha endpointlar /api/ bilan boshlanadi
# tags — Swagger dokumentatsiyasida guruhlash uchun
# ============================================================
router = APIRouter(prefix="/api", tags=["Chat API"])


# ============================================================
# Dependency Injection — har bir so'rov uchun kerakli servislar
# FastAPI avtomatik ravishda bu funksiyalarni chaqiradi
# ============================================================

def get_rag_engine() -> RAGEngine:
    """
    RAG Engine obyektini qaytaradi.
    Bu funksiya har bir so'rovda chaqiriladi (Depends orqali).
    Singleton pattern — bitta obyekt yaratiladi va qayta ishlatiladi.
    """
    return RAGEngine()


def get_chat_history() -> ChatHistoryManager:
    """
    Chat tarix boshqaruvchisini qaytaradi.
    Redis bilan ishlash uchun.
    """
    return ChatHistoryManager()


# ============================================================
# POST /api/chat/message — Asosiy endpoint: xabar yuborish
# ============================================================

@router.post(
    "/chat/message",
    response_model=ChatMessageResponse,
    summary="Yangi chat xabari yuborish",
    description="Foydalanuvchi savolini qabul qilib, AI javobini qaytaradi"
)
async def send_message(
    request: ChatMessageRequest,
    rag_engine: RAGEngine = Depends(get_rag_engine),
    chat_history: ChatHistoryManager = Depends(get_chat_history),
) -> ChatMessageResponse:
    """
    Foydalanuvchi xabarini qayta ishlash jarayoni:

    1. Sessiya ID tekshirish (yangi bo'lsa — yaratish)
    2. Foydalanuvchi xabarini chat tarixiga saqlash
    3. RAG Engine orqali javob generatsiya qilish
       - Savolni embedding ga aylantirish
       - ChromaDB dan tegishli chunklar topish
       - Ollama orqali javob yaratish
    4. AI javobini chat tarixiga saqlash
    5. Javobni foydalanuvchiga qaytarish
    """
    try:
        # 1-qadam: Sessiya ID — yangi suhbat bo'lsa yangi ID yaratamiz
        session_id = request.session_id or str(uuid.uuid4())
        logger.info(
            f"Yangi xabar: session={session_id}, "
            f"sahifa={request.current_page}, "
            f"til={request.language}"
        )

        # 2-qadam: Foydalanuvchi xabarini tarixga saqlash
        user_message_id = str(uuid.uuid4())
        await chat_history.save_message(
            session_id=session_id,
            message_id=user_message_id,
            role="user",
            content=request.message,
        )

        # 3-qadam: RAG Engine orqali javob olish
        # current_page konteksti RAG ga yuboriladi —
        # AI qaysi sahifada turganini bilib, aniqroq javob beradi
        rag_response = await rag_engine.get_answer(
            question=request.message,
            current_page=request.current_page,
            language=request.language.value,
            session_id=session_id,
        )

        # 4-qadam: AI javobini tarixga saqlash
        assistant_message_id = str(uuid.uuid4())
        await chat_history.save_message(
            session_id=session_id,
            message_id=assistant_message_id,
            role="assistant",
            content=rag_response["answer"],
        )

        # 5-qadam: Javobni foydalanuvchiga qaytarish
        return ChatMessageResponse(
            answer=rag_response["answer"],
            message_id=assistant_message_id,
            session_id=session_id,
            sources=rag_response.get("sources", []),
            confidence=rag_response.get("confidence", 0.0),
            current_page_context=request.current_page,
        )

    except Exception as e:
        # Xatolik bo'lsa, log yozamiz va foydalanuvchiga xabar beramiz
        logger.error(f"Xabar qayta ishlashda xato: {e}")
        raise HTTPException(
            status_code=500,
            detail="Xabarni qayta ishlashda xatolik yuz berdi. Iltimos qayta urinib ko'ring."
        )


# ============================================================
# GET /api/chat/history/{session_id} — Chat tarixini olish
# ============================================================

@router.get(
    "/chat/history/{session_id}",
    response_model=ChatHistoryResponse,
    summary="Chat tarixini olish",
    description="Berilgan sessiya ID bo'yicha barcha xabarlarni qaytaradi"
)
async def get_history(
    session_id: str,
    chat_history: ChatHistoryManager = Depends(get_chat_history),
) -> ChatHistoryResponse:
    """
    Berilgan sessiya ID bo'yicha chat tarixini qaytaradi.
    Foydalanuvchi oldingi suhbatini davom ettirmoqchi bo'lganda ishlatiladi.
    """
    try:
        messages = await chat_history.get_history(session_id)
        return ChatHistoryResponse(
            session_id=session_id,
            messages=messages,
            total_messages=len(messages),
        )
    except Exception as e:
        logger.error(f"Tarix olishda xato: {e}")
        raise HTTPException(
            status_code=500,
            detail="Chat tarixini olishda xatolik yuz berdi."
        )


# ============================================================
# DELETE /api/chat/history/{session_id} — Chat tarixini o'chirish
# ============================================================

@router.delete(
    "/chat/history/{session_id}",
    summary="Chat tarixini o'chirish",
    description="Berilgan sessiya ID bo'yicha barcha xabarlarni o'chiradi"
)
async def delete_history(
    session_id: str,
    chat_history: ChatHistoryManager = Depends(get_chat_history),
) -> dict:
    """
    Foydalanuvchi "Tarixni tozalash" tugmasini bosganda chaqiriladi.
    Redis dan sessiyaga tegishli barcha xabarlarni o'chiradi.
    """
    try:
        await chat_history.delete_history(session_id)
        logger.info(f"Chat tarixi o'chirildi: session={session_id}")
        return {"status": "success", "message": "Chat tarixi o'chirildi"}
    except Exception as e:
        logger.error(f"Tarix o'chirishda xato: {e}")
        raise HTTPException(
            status_code=500,
            detail="Chat tarixini o'chirishda xatolik yuz berdi."
        )


# ============================================================
# POST /api/feedback — Javobga baho berish
# ============================================================

@router.post(
    "/feedback",
    summary="Javobga baho berish",
    description="Foydalanuvchi AI javobiga 👍 yoki 👎 baho beradi"
)
async def submit_feedback(request: FeedbackRequest) -> dict:
    """
    Foydalanuvchi bahosi — AI sifatini o'lchash uchun.

    Kelajakda bu ma'lumotlar:
    - Eng yomon javoblarni aniqlash uchun
    - Knowledge base ni yaxshilash uchun
    - Model fine-tuning uchun ishlatiladi
    """
    try:
        logger.info(
            f"Feedback: session={request.session_id}, "
            f"message={request.message_id}, "
            f"baho={request.feedback.value}, "
            f"izoh={request.comment}"
        )
        # TODO: Feedback ni bazaga saqlash (keyingi bosqichda)
        return {
            "status": "success",
            "message": "Bahoingiz qabul qilindi. Rahmat!"
        }
    except Exception as e:
        logger.error(f"Feedback saqlashda xato: {e}")
        raise HTTPException(
            status_code=500,
            detail="Bahoni saqlashda xatolik yuz berdi."
        )


# ============================================================
# Sog'liqni tekshirish (Health Check) — alohida router
# Monitoring tizimlar (Prometheus, Docker healthcheck) uchun
# ============================================================
health_router = APIRouter(tags=["Health"])


@health_router.get(
    "/health",
    response_model=HealthResponse,
    summary="Tizim holati tekshiruvi",
    description="Barcha komponentlar (Ollama, ChromaDB, Redis) holatini tekshiradi"
)
async def health_check(
    rag_engine: RAGEngine = Depends(get_rag_engine),
    chat_history: ChatHistoryManager = Depends(get_chat_history),
) -> HealthResponse:
    """
    Tizim holati tekshiruvi.
    Docker HEALTHCHECK va monitoring tizimlar bu endpoint ni
    muntazam chaqirib, tizim ishlayotganini tekshiradi.
    """
    # Har bir komponentni alohida tekshiramiz
    llm_ok = await rag_engine.check_llm_connection()
    ollama_ok = await rag_engine.check_ollama_connection()
    chroma_ok = await rag_engine.check_chroma_connection()
    redis_ok = await chat_history.check_connection()
    kb_chunks = await rag_engine.get_knowledge_base_count()

    # LLM provider nomi
    from app.config import settings
    llm_provider = settings.llm.provider

    # Agar birorta komponent ishlamasa, status "degraded" bo'ladi
    overall_status = "ok" if all([llm_ok, ollama_ok, chroma_ok, redis_ok]) else "degraded"

    return HealthResponse(
        status=overall_status,
        llm_provider=llm_provider,
        llm_connected=llm_ok,
        ollama_connected=ollama_ok,
        chroma_connected=chroma_ok,
        redis_connected=redis_ok,
        knowledge_base_chunks=kb_chunks,
    )
