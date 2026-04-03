"""
UzASBO 2.0 AI Assistant — Markaziy konfiguratsiya fayli

Bu fayl barcha sozlamalarni .env fayldan o'qiydi va
dasturning boshqa qismlariga taqdim etadi.
Pydantic Settings yordamida validatsiya ham qilinadi.
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List


class LLMProviderSettings(BaseSettings):
    """
    LLM provider tanlash sozlamalari.
    "claude" — Anthropic Claude API (bulutli, sifatli, tez)
    "ollama" — mahalliy Ollama server (bepul, internet kerak emas)
    """

    # LLM provider — "claude" yoki "ollama"
    provider: str = Field(
        default="ollama",
        description="LLM provider: 'claude' yoki 'ollama'"
    )

    class Config:
        env_prefix = "LLM_"


class ClaudeSettings(BaseSettings):
    """
    Anthropic Claude API sozlamalari.
    Claude — Anthropic kompaniyasining bulutli AI modeli.
    Sifati yuqori, tez ishlaydi, lekin pullik va internet kerak.
    """

    # Anthropic API kalit — https://console.anthropic.com dan olinadi
    api_key: str = Field(
        default="",
        description="Anthropic API kaliti"
    )
    # Model nomi
    # claude-sonnet-4-6 — tez va sifatli (tavsiya etiladi)
    # claude-haiku-4-5-20251001 — arzon va tez
    model: str = Field(
        default="claude-sonnet-4-6",
        description="Claude model nomi"
    )
    # Maksimal javob uzunligi (tokenlarda)
    max_tokens: int = Field(
        default=1024,
        description="Maksimal javob token soni"
    )

    class Config:
        env_prefix = "CLAUDE_"


class OllamaSettings(BaseSettings):
    """
    Ollama (mahalliy LLM) sozlamalari.
    Ollama — bu LLM modellarni mahalliy serverda ishga tushirish uchun vosita.
    """

    # Ollama server manzili
    base_url: str = Field(
        default="http://localhost:11434",
        description="Ollama API server manzili"
    )
    # Javob generatsiya qilish uchun model
    model: str = Field(
        default="llama3.1:8b",
        description="Asosiy LLM model nomi"
    )
    # Embedding model — ChromaDB uchun (har doim Ollama orqali)
    embed_model: str = Field(
        default="nomic-embed-text",
        description="Embedding model nomi"
    )

    class Config:
        env_prefix = "OLLAMA_"


class ChromaSettings(BaseSettings):
    """
    ChromaDB (vektorli ma'lumotlar bazasi) sozlamalari.
    ChromaDB — matnlarni vektor shaklida saqlash va qidirish uchun DB.
    RAG tizimda "eng o'xshash matn"ni topish uchun ishlatiladi.
    """

    host: str = Field(default="localhost", description="ChromaDB server manzili")
    port: int = Field(default=8000, description="ChromaDB server porti")
    # Kolleksiya = oddiy DB dagi "jadval" ga o'xshash tushuncha
    collection: str = Field(
        default="uzasbo2_knowledge",
        description="ChromaDB kolleksiya nomi"
    )

    class Config:
        env_prefix = "CHROMA_"


class RedisSettings(BaseSettings):
    """
    Redis sozlamalari.
    Redis — tezkor in-memory cache va ma'lumotlar saqlash.
    Biz chat tarixini saqlash uchun ishlatamiz.
    """

    host: str = Field(default="localhost", description="Redis server manzili")
    port: int = Field(default=6379, description="Redis server porti")
    password: str = Field(default="", description="Redis parol")
    db: int = Field(default=0, description="Redis DB raqami (0-15)")

    class Config:
        env_prefix = "REDIS_"


class RAGSettings(BaseSettings):
    """
    RAG (Retrieval-Augmented Generation) sozlamalari.
    RAG = Qidirish + Generatsiya: avval tegishli ma'lumotni topamiz,
    keyin shu ma'lumot asosida javob generatsiya qilamiz.
    """

    # Similarity search dan nechta eng yaqin chunk qaytarilsin
    # Ko'proq chunk = ko'proq kontekst, lekin sekinroq
    top_k: int = Field(
        default=5,
        description="Nechta eng o'xshash chunk olinadi"
    )
    # Temperature — javobning "ijodiylik" darajasi
    # 0.0 = har doim bir xil javob, 1.0 = har safar boshqacha
    # AI assistant uchun 0.1-0.3 optimal (aniq javoblar kerak)
    temperature: float = Field(
        default=0.2,
        description="LLM temperature (0.0-1.0)"
    )
    # Chunk hajmi — matnni necha belgili bo'laklarga bo'lamiz
    # 800 belgi = taxminan 1 paragraf
    chunk_size: int = Field(
        default=800,
        description="Chunk hajmi (belgilar soni)"
    )
    # Overlap — ikki chunk orasidagi takrorlanish
    # Bu kontekstning uzilmasligini ta'minlaydi
    chunk_overlap: int = Field(
        default=200,
        description="Chunklar orasidagi overlap"
    )

    class Config:
        env_prefix = "RAG_"


class ChatSettings(BaseSettings):
    """
    Chat sozlamalari.
    Foydalanuvchi bilan suhbat parametrlari.
    """

    # Chat tarix saqlash muddati (Redis da)
    # 86400 soniya = 24 soat = 1 kun
    history_ttl: int = Field(
        default=86400,
        description="Chat tarix saqlash muddati (soniyalarda)"
    )
    # Bitta sessiyada maksimal xabarlar soni
    # Xotira va performance uchun chegaralash kerak
    max_messages: int = Field(
        default=50,
        description="Bitta sessiyada maksimal xabarlar"
    )

    class Config:
        env_prefix = "CHAT_"


class AppSettings(BaseSettings):
    """
    Asosiy dastur sozlamalari.
    Bu klass barcha sozlamalarni birlashtirib,
    dasturning boshqa qismlariga yagona nuqta orqali taqdim etadi.
    """

    # Server porti
    port: int = Field(default=8100, description="FastAPI server porti")
    # Debug rejim — ishlab chiqish vaqtida True, productionda False
    debug: bool = Field(default=True, description="Debug rejim")
    # CORS — qaysi domenlardan so'rov kelishiga ruxsat berish
    # Frontend va backend turli portlarda ishlasa, CORS kerak
    cors_origins: str = Field(
        default="http://localhost:3000,http://localhost:8080",
        description="CORS ruxsat berilgan domenlar"
    )

    # Ichki sozlamalar guruhlari
    llm: LLMProviderSettings = LLMProviderSettings()
    claude: ClaudeSettings = ClaudeSettings()
    ollama: OllamaSettings = OllamaSettings()
    chroma: ChromaSettings = ChromaSettings()
    redis: RedisSettings = RedisSettings()
    rag: RAGSettings = RAGSettings()
    chat: ChatSettings = ChatSettings()

    class Config:
        env_prefix = "APP_"
        env_file = ".env"  # .env fayldan o'qish
        extra = "ignore"  # .env dagi qo'shimcha o'zgaruvchilarni e'tiborsiz qoldirish

    def get_cors_origins_list(self) -> List[str]:
        """
        CORS origins ni ro'yxat (list) shaklida qaytaradi.
        .env da vergul bilan yozilgan stringni list ga aylantiradi.
        Masalan: "http://localhost:3000,http://localhost:8080"
        → ["http://localhost:3000", "http://localhost:8080"]
        """
        return [origin.strip() for origin in self.cors_origins.split(",")]


# ============================================================
# Global settings obyekti
# Dasturning istalgan joyida import qilib ishlatish mumkin:
#   from app.config import settings
#   print(settings.ollama.model)  # "llama3.1:8b"
# ============================================================
settings = AppSettings()
