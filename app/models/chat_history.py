"""
UzASBO 2.0 AI Assistant — Chat tarix boshqaruvi

Bu modul Redis yordamida chat tarixini saqlash va boshqarishni amalga oshiradi.

Nima uchun Redis?
    - Juda tez (in-memory = RAM da ishlaydi)
    - TTL (Time-To-Live) — avtomatik o'chirish muddati
    - Sodda key-value model — chat tarixini saqlash uchun ideal
    - Scalable — ko'p foydalanuvchilar bilan ishlaydi

Ma'lumotlar strukturasi Redis da:
    Key: "chat:{session_id}"
    Value: JSON ro'yxat (xabarlar)
    TTL: 86400 soniya (24 soat)

Misol:
    Key: "chat:abc-123-def"
    Value: [
        {"id": "msg-1", "role": "user", "content": "Salom", "timestamp": "..."},
        {"id": "msg-2", "role": "assistant", "content": "Salom!", "timestamp": "..."},
    ]
"""

import redis.asyncio as redis
from loguru import logger
from typing import List, Optional
from datetime import datetime
import json

from app.config import settings
from app.models.schemas import ChatMessage, MessageRole


class ChatHistoryManager:
    """
    Chat tarixini Redis da saqlash va boshqarish.

    Asosiy metodlar:
        save_message()    — Yangi xabar saqlash
        get_history()     — Sessiya tarixini olish
        delete_history()  — Sessiya tarixini o'chirish
        get_recent_context() — Oxirgi N xabarni olish (RAG kontekst uchun)
    """

    # Singleton pattern
    _instance = None
    _redis_client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Redis ulanishni sozlash."""
        if self._redis_client is not None:
            return

        try:
            # Redis asinxron klient yaratish
            # decode_responses=True — javoblarni bytes emas, string qaytaradi
            self._redis_client = redis.Redis(
                host=settings.redis.host,
                port=settings.redis.port,
                password=settings.redis.password or None,
                db=settings.redis.db,
                decode_responses=True,  # bytes → string avtomatik
            )
            logger.info(
                f"Redis klient yaratildi: "
                f"{settings.redis.host}:{settings.redis.port}"
            )
        except Exception as e:
            logger.error(f"Redis ulanishda xato: {e}")
            self._redis_client = None

    def _get_key(self, session_id: str) -> str:
        """
        Redis kalitini yaratish.

        Har bir sessiya uchun alohida kalit ishlatiladi.
        Prefiks "chat:" — boshqa Redis kalitlari bilan aralashib ketmasligi uchun.

        Args:
            session_id: Sessiya ID si

        Returns:
            Redis kaliti, masalan: "chat:abc-123-def"
        """
        return f"chat:{session_id}"

    async def save_message(
        self,
        session_id: str,
        message_id: str,
        role: str,
        content: str,
    ) -> bool:
        """
        Yangi xabarni chat tarixiga saqlash.

        Xabar Redis dagi ro'yxat (list) oxiriga qo'shiladi.
        Har safar TTL yangilanadi — so'nggi xabardan 24 soat keyin o'chiriladi.

        Args:
            session_id: Sessiya ID si
            message_id: Xabar ID si (unikal)
            role: Kim yozgan — "user" yoki "assistant"
            content: Xabar matni

        Returns:
            True — muvaffaqiyatli saqlandi
            False — xatolik yuz berdi

        Misol:
            await history.save_message(
                session_id="abc-123",
                message_id="msg-001",
                role="user",
                content="To'lov topshiriqnomasi nima?"
            )
        """
        if not self._redis_client:
            logger.warning("Redis ulangan emas, xabar saqlanmadi")
            return False

        try:
            key = self._get_key(session_id)

            # Xabar ma'lumotlarini dict shaklida tayyorlash
            message_data = {
                "id": message_id,
                "role": role,
                "content": content,
                "timestamp": datetime.now().isoformat(),
            }

            # Redis RPUSH — ro'yxat oxiriga element qo'shish
            # R = Right (o'ng tomon = oxir)
            await self._redis_client.rpush(key, json.dumps(message_data))

            # TTL (Time-To-Live) o'rnatish — muddati o'tgach avtomatik o'chiriladi
            await self._redis_client.expire(key, settings.chat.history_ttl)

            # Maksimal xabarlar sonini cheklash
            # Agar 50 dan oshsa, eng eski xabarlarni o'chiramiz
            current_length = await self._redis_client.llen(key)
            if current_length > settings.chat.max_messages:
                # LTRIM — ro'yxatni kesish (faqat oxirgi N elementni qoldirish)
                # 0 dan -(max+1) gacha = eng eski xabarlar o'chiriladi
                await self._redis_client.ltrim(
                    key,
                    current_length - settings.chat.max_messages,
                    -1  # -1 = oxirigacha
                )

            logger.debug(
                f"Xabar saqlandi: session={session_id}, "
                f"role={role}, id={message_id}"
            )
            return True

        except Exception as e:
            logger.error(f"Xabar saqlashda xato: {e}")
            return False

    async def get_history(self, session_id: str) -> List[ChatMessage]:
        """
        Sessiya bo'yicha barcha xabarlarni olish.

        Redis LRANGE buyrug'i bilan ro'yxatning barchasini o'qiydi.

        Args:
            session_id: Sessiya ID si

        Returns:
            ChatMessage obyektlari ro'yxati (vaqt bo'yicha tartiblangan)
        """
        if not self._redis_client:
            logger.warning("Redis ulangan emas")
            return []

        try:
            key = self._get_key(session_id)

            # LRANGE 0 -1 — ro'yxatning barchasini olish
            # 0 = boshidan, -1 = oxirigacha
            raw_messages = await self._redis_client.lrange(key, 0, -1)

            messages = []
            for raw in raw_messages:
                try:
                    # JSON string → dict → ChatMessage
                    data = json.loads(raw)
                    messages.append(ChatMessage(
                        id=data["id"],
                        role=MessageRole(data["role"]),
                        content=data["content"],
                        timestamp=datetime.fromisoformat(data["timestamp"]),
                    ))
                except (json.JSONDecodeError, KeyError, ValueError) as e:
                    logger.warning(f"Xabar parsing xatosi (o'tkazildi): {e}")
                    continue

            logger.debug(
                f"Tarix olindi: session={session_id}, "
                f"xabarlar soni={len(messages)}"
            )
            return messages

        except Exception as e:
            logger.error(f"Tarix olishda xato: {e}")
            return []

    async def delete_history(self, session_id: str) -> bool:
        """
        Sessiya tarixini to'liq o'chirish.

        Foydalanuvchi "Tarixni tozalash" tugmasini bosganda chaqiriladi.

        Args:
            session_id: Sessiya ID si

        Returns:
            True — muvaffaqiyatli o'chirildi
        """
        if not self._redis_client:
            return False

        try:
            key = self._get_key(session_id)
            # DEL — kalitni o'chirish (barcha xabarlar bilan birga)
            await self._redis_client.delete(key)
            logger.info(f"Chat tarixi o'chirildi: session={session_id}")
            return True
        except Exception as e:
            logger.error(f"Tarix o'chirishda xato: {e}")
            return False

    async def get_recent_context(
        self,
        session_id: str,
        count: int = 6,
    ) -> str:
        """
        Oxirgi N xabarni olish — RAG kontekst uchun.

        AI ga oldingi suhbat kontekstini berish uchun ishlatiladi.
        Masalan, foydalanuvchi avval "Shartnoma nima?" deb so'ragan bo'lsa,
        keyingi "Uni qanday yarataman?" savoliga shartnoma haqida javob beradi.

        Args:
            session_id: Sessiya ID si
            count: Nechta oxirgi xabar olinsin (default: 6 = 3 juft)

        Returns:
            Formatlangan matn:
            "Foydalanuvchi: Shartnoma nima?
             AI: Shartnoma — bu...
             Foydalanuvchi: Uni qanday yarataman?"
        """
        if not self._redis_client:
            return ""

        try:
            key = self._get_key(session_id)

            # Oxirgi N xabarni olish
            # -count = oxiridan count ta, -1 = oxirigacha
            raw_messages = await self._redis_client.lrange(key, -count, -1)

            if not raw_messages:
                return ""

            # Xabarlarni tushunarli formatga aylantirish
            context_parts = []
            for raw in raw_messages:
                try:
                    data = json.loads(raw)
                    role_label = (
                        "Foydalanuvchi" if data["role"] == "user"
                        else "AI"
                    )
                    context_parts.append(
                        f"{role_label}: {data['content']}"
                    )
                except (json.JSONDecodeError, KeyError):
                    continue

            return "\n".join(context_parts)

        except Exception as e:
            logger.error(f"Recent context olishda xato: {e}")
            return ""

    async def check_connection(self) -> bool:
        """
        Redis ulanishini tekshirish.
        Health check uchun.

        Returns:
            True — Redis ishlayapti
            False — Redis ishlamayapti
        """
        if not self._redis_client:
            return False

        try:
            # PING — Redis serverga "salom" yuborish
            # Javob: "PONG" — ishlayapti
            response = await self._redis_client.ping()
            return response is True
        except Exception as e:
            logger.error(f"Redis ping xatosi: {e}")
            return False
