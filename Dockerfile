# ============================================================
# UzASBO 2.0 AI Assistant — Docker image
#
# Bu Dockerfile FastAPI ilovasini konteynerga joylashtiradi.
# Multi-stage build — avval dependencies o'rnatiladi,
# keyin ilova kodi ko'chiriladi. Bu image hajmini kamaytiradi.
# ============================================================

# --- 1-BOSQICH: Base image ---
# Python 3.11 slim — kichik hajmli Python image
# slim = faqat kerakli paketlar (to'liq Ubuntu emas)
FROM python:3.11-slim AS base

# Muhit o'zgaruvchilari
# PYTHONDONTWRITEBYTECODE — .pyc fayllarni yaratmaslik (hajm tejash)
# PYTHONUNBUFFERED — stdout ni bufferlamaslik (loglar real-time ko'rinadi)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Ish papkasini belgilash
# Konteyner ichida barcha buyruqlar shu papkada bajariladi
WORKDIR /app

# --- 2-BOSQICH: Dependencies o'rnatish ---
# Avval faqat requirements.txt ni ko'chiramiz
# Docker cache — agar requirements o'zgarmasa, qayta o'rnatmaydi
COPY requirements.txt .

# pip bilan kutubxonalarni o'rnatish
# --no-cache-dir — pip cache ni saqlamamaslik (hajm tejash)
# --upgrade — pip ni yangilash
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# --- 3-BOSQICH: Ilova kodini ko'chirish ---
# Barcha loyiha fayllarini konteynerga ko'chirish
COPY . .

# Logs papkasini yaratish
RUN mkdir -p logs

# --- 4-BOSQICH: Port va ishga tushirish ---
# FastAPI 8100 portda ishlaydi
EXPOSE 8100

# Health check — Docker konteyner sog'ligini tekshirish
# Har 30 soniyada /health endpoint ga so'rov yuboriladi
# Agar 3 marta ketma-ket muvaffaqiyatsiz bo'lsa, konteyner "unhealthy"
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8100/health')" || exit 1

# Dasturni ishga tushirish buyrug'i
# uvicorn — ASGI server
# app.main:app — ilova joylashuvi (app/main.py dagi app obyekti)
# --host 0.0.0.0 — barcha interfeyslarda tinglash
# --port 8100 — port raqami
# --workers 2 — 2 ta worker process (parallel so'rovlar uchun)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8100", "--workers", "2"]
