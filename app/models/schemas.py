"""
UzASBO 2.0 AI Assistant — Pydantic sxemalar (modellar)

Bu fayl API so'rov va javoblarning strukturasini belgilaydi.
Pydantic avtomatik validatsiya qiladi — noto'g'ri ma'lumot kelsa, xato qaytaradi.

Misol: foydalanuvchi "message" maydonsiz so'rov yuborsa,
Pydantic 422 xato qaytaradi va qaysi maydon yetishmasligini ko'rsatadi.
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


# ============================================================
# Enumlar (ruxsat etilgan qiymatlar ro'yxati)
# ============================================================

class MessageRole(str, Enum):
    """
    Xabar muallifi roli.
    - user: foydalanuvchi yozgan xabar
    - assistant: AI yozgan javob
    - system: tizim xabarlari (ko'rinmaydi)
    """
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class FeedbackType(str, Enum):
    """
    Foydalanuvchi bahosi.
    Javob sifatini o'lchash va yaxshilash uchun.
    """
    POSITIVE = "positive"   # 👍 — yaxshi javob
    NEGATIVE = "negative"   # 👎 — yomon javob


class Language(str, Enum):
    """
    Qo'llab-quvvatlanadigan tillar.
    Foydalanuvchi qaysi tilda yozsa, shu tilda javob beramiz.
    """
    UZ_LATN = "uz_latn"   # O'zbek (lotin)
    UZ_CYRL = "uz_cyrl"   # Ўзбек (кирилл)
    RU = "ru"              # Русский


# ============================================================
# So'rov modellari (Request) — foydalanuvchi serverga yuboradi
# ============================================================

class ChatMessageRequest(BaseModel):
    """
    Foydalanuvchining chat xabari so'rovi.

    Misol JSON:
    {
        "message": "To'lov topshiriqnomasi qanday yaratiladi?",
        "session_id": "abc-123-def",
        "current_page": "/document/finance/paymentorder",
        "language": "uz_latn"
    }
    """

    # Foydalanuvchi yozgan xabar matni (majburiy)
    message: str = Field(
        ...,  # ... = majburiy maydon
        min_length=1,      # kamida 1 ta belgi
        max_length=2000,   # ko'pi bilan 2000 belgi
        description="Foydalanuvchi xabari matni"
    )

    # Sessiya identifikatori — bir suhbatdagi xabarlarni birlashtirish uchun
    # Har safar yangi chat ochilganda yangi session_id yaratiladi
    session_id: Optional[str] = Field(
        default=None,
        description="Chat sessiya ID si (yangi chat uchun bo'sh qoldiring)"
    )

    # Foydalanuvchi hozir qaysi sahifada turgan
    # Bu AI ga kontekst beradi — masalan, paymentorder sahifasida bo'lsa,
    # AI to'lov topshiriqnomasi haqida ko'proq bilim beradi
    current_page: Optional[str] = Field(
        default=None,
        description="Foydalanuvchining joriy sahifa URL i",
        examples=["/document/finance/paymentorder"]
    )

    # Foydalanuvchi tili — javob shu tilda beriladi
    language: Language = Field(
        default=Language.UZ_LATN,
        description="Foydalanuvchi tili"
    )


class FeedbackRequest(BaseModel):
    """
    Javobga baho berish so'rovi.
    Foydalanuvchi 👍 yoki 👎 bosganda yuboriladi.

    Misol JSON:
    {
        "message_id": "msg-456",
        "session_id": "abc-123",
        "feedback": "positive",
        "comment": "Juda aniq javob berdi"
    }
    """

    # Qaysi xabarga baho berilmoqda
    message_id: str = Field(..., description="Xabar ID si")
    # Qaysi sessiyada
    session_id: str = Field(..., description="Chat sessiya ID si")
    # Baho turi: positive yoki negative
    feedback: FeedbackType = Field(..., description="Baho (positive/negative)")
    # Ixtiyoriy izoh — foydalanuvchi qo'shimcha fikr yozishi mumkin
    comment: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Qo'shimcha izoh"
    )


# ============================================================
# Javob modellari (Response) — server foydalanuvchiga qaytaradi
# ============================================================

class ChatMessage(BaseModel):
    """
    Bitta chat xabari modeli.
    Chat tarixida har bir xabar shu formatda saqlanadi.
    """

    # Xabar identifikatori (unikal)
    id: str = Field(..., description="Xabar unikal ID si")
    # Kim yozgan: user yoki assistant
    role: MessageRole = Field(..., description="Xabar muallifi roli")
    # Xabar matni
    content: str = Field(..., description="Xabar matni")
    # Yaratilgan vaqti
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Xabar yaratilgan vaqti"
    )
    # AI ishonch darajasi (faqat assistant xabarlari uchun)
    # 0.0 = umuman ishonchsiz, 1.0 = to'liq ishonchli
    confidence: Optional[float] = Field(
        default=None,
        ge=0.0,  # 0 dan kichik bo'lmasin
        le=1.0,  # 1 dan katta bo'lmasin
        description="AI javob ishonch darajasi (0.0-1.0)"
    )


class ChatMessageResponse(BaseModel):
    """
    Chat xabariga javob.
    AI javob bergandan keyin foydalanuvchiga qaytariladigan ma'lumot.

    Misol JSON:
    {
        "answer": "To'lov topshiriqnomasi yaratish uchun...",
        "message_id": "msg-789",
        "session_id": "abc-123",
        "sources": ["paymentorder_guide.md"],
        "confidence": 0.87,
        "current_page_context": "finance/paymentorder"
    }
    """

    # AI javob matni
    answer: str = Field(..., description="AI javob matni")
    # Javob xabari ID si
    message_id: str = Field(..., description="Javob xabari ID si")
    # Sessiya ID si (yangi sessiya bo'lsa, yangi ID qaytariladi)
    session_id: str = Field(..., description="Chat sessiya ID si")
    # Javob tayyorlashda ishlatilgan manbalar ro'yxati
    # Foydalanuvchiga javob qayerdan olinganini ko'rsatish uchun
    sources: List[str] = Field(
        default_factory=list,
        description="Foydalanilgan manbalar"
    )
    # AI ishonch darajasi
    confidence: float = Field(
        default=0.0,
        description="Javob ishonch darajasi (0.0-1.0)"
    )
    # Qaysi sahifa kontekstida javob berildi
    current_page_context: Optional[str] = Field(
        default=None,
        description="Sahifa konteksti"
    )


class ChatHistoryResponse(BaseModel):
    """
    Chat tarixini qaytarish javob modeli.
    Foydalanuvchi chat tarixini so'raganda ishlatiladi.
    """

    # Sessiya ID si
    session_id: str = Field(..., description="Chat sessiya ID si")
    # Xabarlar ro'yxati (vaqt bo'yicha tartiblangan)
    messages: List[ChatMessage] = Field(
        default_factory=list,
        description="Xabarlar ro'yxati"
    )
    # Jami xabarlar soni
    total_messages: int = Field(default=0, description="Jami xabarlar soni")


class HealthResponse(BaseModel):
    """
    Tizim holati tekshiruv javobi.
    /health endpoint da qaytariladi — monitoring tizimlar uchun.
    """

    # Umumiy holat
    status: str = Field(default="ok", description="Tizim holati")
    # LLM provider nomi
    llm_provider: str = Field(
        default="ollama",
        description="LLM provider: 'claude' yoki 'ollama'"
    )
    # LLM ulanishi (Claude yoki Ollama)
    llm_connected: bool = Field(
        default=False,
        description="LLM serverga ulanish holati"
    )
    # Ollama ulanishi (embedding uchun har doim kerak)
    ollama_connected: bool = Field(
        default=False,
        description="Ollama serverga ulanish holati (embedding uchun)"
    )
    # ChromaDB ulanishi
    chroma_connected: bool = Field(
        default=False,
        description="ChromaDB ulanish holati"
    )
    # Redis ulanishi
    redis_connected: bool = Field(
        default=False,
        description="Redis ulanish holati"
    )
    # Knowledge base da nechta chunk bor
    knowledge_base_chunks: int = Field(
        default=0,
        description="Knowledge base dagi chunklar soni"
    )
