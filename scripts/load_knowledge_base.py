"""
UzASBO 2.0 AI Assistant — Knowledge Base yuklash skripti

Bu skript knowledge_base/ papkasidagi barcha fayllarni o'qib,
chunklarga bo'lib, ChromaDB ga yuklaydi.

Ishga tushirish:
    python scripts/load_knowledge_base.py

Qayta yuklash (eski ma'lumotlarni o'chirib):
    python scripts/load_knowledge_base.py --force

Talablar:
    - ChromaDB ishlayotgan bo'lishi kerak (docker-compose up chromadb)
    - Ollama ishlayotgan bo'lishi kerak (embedding uchun)
"""

import asyncio
import sys
import os
from pathlib import Path

# Loyiha ildiz papkasini Python path ga qo'shish
# Bu app/ paketi importlarini ishlashini ta'minlaydi
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from loguru import logger
from app.knowledge.loader import KnowledgeBaseLoader


async def main():
    """
    Asosiy funksiya — Knowledge Base ni yuklash.
    """
    # --force argumenti bormi tekshirish
    force_reload = "--force" in sys.argv

    logger.info("=" * 60)
    logger.info("UzASBO 2.0 AI Assistant — Knowledge Base yuklash")
    logger.info(f"Force reload: {force_reload}")
    logger.info("=" * 60)

    try:
        # Loader ni yaratish va ishga tushirish
        loader = KnowledgeBaseLoader()
        await loader.initialize()

        # Barcha fayllarni yuklash
        await loader.load_all(force_reload=force_reload)

        logger.info("Knowledge Base muvaffaqiyatli yuklandi!")

    except Exception as e:
        logger.error(f"Knowledge Base yuklashda xato: {e}")
        logger.error(
            "ChromaDB va Ollama ishlayotganini tekshiring:\n"
            "  docker-compose up -d chromadb ollama\n"
            "  docker exec -it ollama ollama pull nomic-embed-text"
        )
        sys.exit(1)


if __name__ == "__main__":
    # Asinxron funksiyani ishga tushirish
    asyncio.run(main())
