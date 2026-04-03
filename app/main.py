"""
UzASBO 2.0 AI Assistant — Asosiy dastur fayli (Entry Point)

Bu fayl FastAPI ilovasini yaratadi va barcha komponentlarni birlashtiradi.
Dastur ishga tushganda shu fayl birinchi bajariladi.

Ishga tushirish:
    uvicorn app.main:app --host 0.0.0.0 --port 8100 --reload

Yoki:
    python -m uvicorn app.main:app --host 0.0.0.0 --port 8100 --reload
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
import sys

from app.config import settings
from app.api.routes import router as api_router, health_router
from app.api.websocket import ws_router
from app.core.rag_engine import RAGEngine


# ============================================================
# Logging sozlash
# Loguru — standart logging dan ko'ra chiroyliroq va qulayroq
# ============================================================
logger.remove()  # Standart handler ni olib tashlash
logger.add(
    sys.stdout,
    # Log formati: vaqt | daraja | modul:funksiya:qator | xabar
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
           "<level>{message}</level>",
    level="DEBUG" if settings.debug else "INFO",
)
# Log faylga ham yozish (kunlik rotatsiya)
logger.add(
    "logs/ai_assistant_{time:YYYY-MM-DD}.log",
    rotation="1 day",      # Har kuni yangi fayl
    retention="30 days",    # 30 kundan eski loglar o'chiriladi
    compression="zip",      # Eski loglar siqiladi
    level="DEBUG",
)


# ============================================================
# Lifespan — dastur boshlanish va tugash hodisalari
# Dastur ishga tushganda va to'xtaganda bajariladigan amallar
# ============================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Dastur hayot sikli (lifecycle) boshqaruvchisi.

    yield dan oldingi kod — dastur ISHGA TUSHGANDA bajariladi:
      - RAG Engine ni ishga tushirish
      - Knowledge Base ni yuklash
      - Ulanishlarni tekshirish

    yield dan keyingi kod — dastur TO'XTAGANDA bajariladi:
      - Ulanishlarni yopish
      - Resurslarni tozalash
    """
    # === DASTUR BOSHLANGANDA ===
    logger.info("=" * 60)
    logger.info("UzASBO 2.0 AI Assistant ishga tushmoqda...")
    logger.info(f"Ollama model: {settings.ollama.model}")
    logger.info(f"Embedding model: {settings.ollama.embed_model}")
    logger.info(f"ChromaDB: {settings.chroma.host}:{settings.chroma.port}")
    logger.info(f"Redis: {settings.redis.host}:{settings.redis.port}")
    logger.info("=" * 60)

    # RAG Engine ni ishga tushirish va Knowledge Base ni yuklash
    try:
        rag_engine = RAGEngine()
        await rag_engine.initialize()
        logger.info("RAG Engine muvaffaqiyatli ishga tushdi")
    except Exception as e:
        logger.warning(
            f"RAG Engine ishga tushishda xato: {e}. "
            "Dastur ishlaydi, lekin AI javob bera olmaydi."
        )

    # Boshqaruvni FastAPI ga beramiz (dastur ishlaydi)
    yield

    # === DASTUR TO'XTAGANDA ===
    logger.info("UzASBO 2.0 AI Assistant to'xtatilmoqda...")
    logger.info("Barcha resurslar tozalandi. Xayr!")


# ============================================================
# FastAPI ilovasi yaratish
# ============================================================
app = FastAPI(
    title="UzASBO 2.0 AI Assistant",
    description=(
        "UzASBO 2.0 tizimining sun'iy intellekt yordamchisi. "
        "RAG (Retrieval-Augmented Generation) texnologiyasi asosida "
        "foydalanuvchilarga yordam beradi."
    ),
    version="1.0.0",
    # Swagger UI manzili: http://localhost:8100/docs
    docs_url="/docs",
    # ReDoc manzili: http://localhost:8100/redoc
    redoc_url="/redoc",
    # Lifespan — dastur hayot sikli
    lifespan=lifespan,
)


# ============================================================
# CORS middleware — Cross-Origin Resource Sharing
#
# Frontend (Nuxt.js, port 3000) va Backend (FastAPI, port 8100)
# turli portlarda ishlaydi. Brauzer xavfsizlik sababli
# turli portlar orasidagi so'rovlarni bloklaydi.
# CORS middleware bu cheklovni olib tashlaydi.
# ============================================================
app.add_middleware(
    CORSMiddleware,
    # Qaysi domenlardan so'rov kelishiga ruxsat berish
    allow_origins=settings.get_cors_origins_list(),
    # Cookie va autentifikatsiya headerlarini qo'llab-quvvatlash
    allow_credentials=True,
    # Barcha HTTP metodlarga ruxsat (GET, POST, DELETE, ...)
    allow_methods=["*"],
    # Barcha headerlarga ruxsat
    allow_headers=["*"],
)


# ============================================================
# Routerlarni ulash
# Har bir router o'z endpointlarini olib keladi
# ============================================================

# REST API endpointlar (/api/chat/message, /api/feedback, ...)
app.include_router(api_router)

# WebSocket endpoint (/ws/chat)
app.include_router(ws_router)

# Health check endpoint (/health)
app.include_router(health_router)


# ============================================================
# Root endpoint — asosiy sahifa
# ============================================================

@app.get("/", tags=["Root"])
async def root():
    """
    Asosiy sahifa. Dastur ishlayotganini tekshirish uchun.
    Brauzerda http://localhost:8100/ ochsangiz shu javob ko'rinadi.
    """
    return {
        "name": "UzASBO 2.0 AI Assistant",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",           # Swagger UI manzili
        "health": "/health",       # Health check manzili
    }


# ============================================================
# Dasturni to'g'ridan-to'g'ri ishga tushirish
# python app/main.py buyrug'i bilan
# ============================================================
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",        # Ilova joylashuvi
        host="0.0.0.0",        # Barcha interfeyslarda tinglash
        port=settings.port,     # Port raqami (.env dan)
        reload=settings.debug,  # Debug rejimda auto-reload
        log_level="debug" if settings.debug else "info",
    )
