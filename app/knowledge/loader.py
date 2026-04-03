"""
UzASBO 2.0 AI Assistant — Knowledge Base yuklash moduli

Bu modul quyidagi vazifalarni bajaradi:
1. knowledge_base/ papkasidagi barcha fayllarni o'qish
2. Har bir faylni tegishli formatda chunklarga bo'lish
3. Chunklarni embedding (vektor) ga aylantirish
4. Vektorlarni ChromaDB ga saqlash

Ishlash tartibi:
    knowledge_base/
    ├── documents/*.md  → Markdown chunker → Embedding → ChromaDB
    ├── errors/*.json   → Error chunker   → Embedding → ChromaDB
    ├── faq/*.md        → FAQ chunker     → Embedding → ChromaDB
    └── navigation/*.json → Nav chunker   → Embedding → ChromaDB

Bu jarayon dastur birinchi marta ishga tushganda bajariladi.
Keyingi ishga tushirishlarda ChromaDB da ma'lumot bor bo'lsa, qayta yuklamaydi.
"""

import os
import json
from pathlib import Path
from loguru import logger
from typing import List

import chromadb
from chromadb.config import Settings as ChromaSettings

from app.config import settings
from app.knowledge.chunker import TextChunker
from app.core.embeddings import EmbeddingService


class KnowledgeBaseLoader:
    """
    Knowledge Base (bilimlar bazasi) yuklash va boshqarish.

    Fayl tizimidagi hujjatlarni o'qib, ChromaDB ga yuklaydi.
    """

    def __init__(self):
        """
        Loader ni sozlash.
        """
        # Knowledge base papkasi yo'li
        # Bu papka loyiha ildizida joylashgan
        self.kb_path = Path(__file__).parent.parent.parent / "knowledge_base"

        # Chunker — matnni bo'laklash uchun
        self.chunker = TextChunker(
            chunk_size=settings.rag.chunk_size,
            chunk_overlap=settings.rag.chunk_overlap,
        )

        # Embedding servisi — matnni vektor ga aylantirish uchun
        self.embedding_service = EmbeddingService()

        # ChromaDB klient va kolleksiya
        self.chroma_client = None
        self.collection = None

        logger.info(f"KnowledgeBaseLoader yaratildi: kb_path={self.kb_path}")

    async def initialize(self):
        """
        ChromaDB ga ulanish va kolleksiya yaratish.
        """
        try:
            self.chroma_client = chromadb.HttpClient(
                host=settings.chroma.host,
                port=settings.chroma.port,
                settings=ChromaSettings(anonymized_telemetry=False),
            )

            self.collection = self.chroma_client.get_or_create_collection(
                name=settings.chroma.collection,
                metadata={
                    "description": "UzASBO 2.0 Knowledge Base",
                    "hnsw:space": "cosine",
                },
            )

            logger.info(
                f"ChromaDB ulandi. Mavjud chunklar: {self.collection.count()}"
            )
        except Exception as e:
            logger.error(f"ChromaDB ulanishda xato: {e}")
            raise

    async def load_all(self, force_reload: bool = False):
        """
        Barcha knowledge base fayllarini yuklash.

        Bu asosiy metod — barcha papkalarni ketma-ket yuklaydi.

        Args:
            force_reload: True bo'lsa, mavjud ma'lumotlarni o'chirib qayta yuklaydi.
                          False bo'lsa, faqat yangi fayllarni yuklaydi.
        """
        if not self.collection:
            await self.initialize()

        # Agar force_reload bo'lsa yoki kolleksiya bo'sh bo'lsa — yuklash
        current_count = self.collection.count()

        if current_count > 0 and not force_reload:
            logger.info(
                f"Knowledge base da {current_count} chunk mavjud. "
                "Qayta yuklash shart emas. force_reload=True bilan chaqiring."
            )
            return

        if force_reload and current_count > 0:
            # Eski ma'lumotlarni o'chirish
            logger.warning("Knowledge base tozalanmoqda (force_reload)...")
            self.chroma_client.delete_collection(settings.chroma.collection)
            self.collection = self.chroma_client.get_or_create_collection(
                name=settings.chroma.collection,
                metadata={
                    "description": "UzASBO 2.0 Knowledge Base",
                    "hnsw:space": "cosine",
                },
            )

        logger.info("=" * 50)
        logger.info("Knowledge Base yuklash boshlandi...")
        logger.info("=" * 50)

        total_chunks = 0

        # 1. Hujjat dokumentatsiyalarni yuklash (documents/*.md)
        doc_chunks = await self._load_documents()
        total_chunks += doc_chunks

        # 2. Xato xabarlarini yuklash (errors/*.json)
        error_chunks = await self._load_errors()
        total_chunks += error_chunks

        # 3. FAQ yuklash (faq/*.md)
        faq_chunks = await self._load_faq()
        total_chunks += faq_chunks

        # 4. Navigatsiya yuklash (navigation/*.json)
        nav_chunks = await self._load_navigation()
        total_chunks += nav_chunks

        logger.info("=" * 50)
        logger.info(f"Knowledge Base yuklandi! Jami: {total_chunks} chunk")
        logger.info("=" * 50)

    async def _load_documents(self) -> int:
        """
        Hujjat dokumentatsiyalarini yuklash.

        knowledge_base/documents/ papkasidagi .md fayllarni o'qib,
        chunklarga bo'lib, ChromaDB ga saqlaydi.

        Returns:
            Yuklangan chunklar soni
        """
        docs_path = self.kb_path / "documents"
        if not docs_path.exists():
            logger.warning(f"Documents papka topilmadi: {docs_path}")
            return 0

        total = 0
        # .md fayllarni topish
        for md_file in docs_path.glob("*.md"):
            try:
                # Faylni o'qish
                text = md_file.read_text(encoding="utf-8")
                # Chunklarga bo'lish
                chunks = self.chunker.chunk_markdown(text, source=md_file.name)
                # ChromaDB ga saqlash
                saved = await self._save_chunks(chunks)
                total += saved
                logger.info(f"  ✓ {md_file.name}: {saved} chunk yuklandi")
            except Exception as e:
                logger.error(f"  ✗ {md_file.name} yuklashda xato: {e}")

        logger.info(f"Documents: jami {total} chunk yuklandi")
        return total

    async def _load_errors(self) -> int:
        """
        Xato xabarlarini yuklash.

        knowledge_base/errors/ papkasidagi .json fayllarni o'qib,
        har bir xato uchun alohida chunk yaratib, ChromaDB ga saqlaydi.

        JSON format:
        [
            {
                "document_type": "paymentorder",
                "error_message": "To'lov turi ko'rsatilmagan",
                "condition": "paymentOrderType == null",
                "field": "PaymentOrderType",
                "explanation": "To'lov turini tanlash majburiy",
                "solution": "To'lov turi maydonini to'ldiring"
            }
        ]

        Returns:
            Yuklangan chunklar soni
        """
        errors_path = self.kb_path / "errors"
        if not errors_path.exists():
            logger.warning(f"Errors papka topilmadi: {errors_path}")
            return 0

        total = 0
        for json_file in errors_path.glob("*.json"):
            try:
                # JSON faylni o'qish
                with open(json_file, "r", encoding="utf-8") as f:
                    errors_data = json.load(f)

                # Chunklarga bo'lish
                chunks = self.chunker.chunk_errors_json(
                    errors_data, source=json_file.name
                )
                # ChromaDB ga saqlash
                saved = await self._save_chunks(chunks)
                total += saved
                logger.info(f"  ✓ {json_file.name}: {saved} error chunk yuklandi")
            except Exception as e:
                logger.error(f"  ✗ {json_file.name} yuklashda xato: {e}")

        logger.info(f"Errors: jami {total} chunk yuklandi")
        return total

    async def _load_faq(self) -> int:
        """
        FAQ (Tez-tez beriladigan savollar) yuklash.

        knowledge_base/faq/ papkasidagi .md fayllarni o'qib,
        har bir savol-javob juftligi alohida chunk sifatida saqlanadi.

        Returns:
            Yuklangan chunklar soni
        """
        faq_path = self.kb_path / "faq"
        if not faq_path.exists():
            logger.warning(f"FAQ papka topilmadi: {faq_path}")
            return 0

        total = 0
        for md_file in faq_path.glob("*.md"):
            try:
                text = md_file.read_text(encoding="utf-8")
                chunks = self.chunker.chunk_faq(text, source=md_file.name)
                saved = await self._save_chunks(chunks)
                total += saved
                logger.info(f"  ✓ {md_file.name}: {saved} FAQ chunk yuklandi")
            except Exception as e:
                logger.error(f"  ✗ {md_file.name} yuklashda xato: {e}")

        logger.info(f"FAQ: jami {total} chunk yuklandi")
        return total

    async def _load_navigation(self) -> int:
        """
        Navigatsiya yo'riqnomalarini yuklash.

        knowledge_base/navigation/ papkasidagi .json fayllarni o'qib,
        har bir menyu elementi uchun chunk yaratadi.

        Returns:
            Yuklangan chunklar soni
        """
        nav_path = self.kb_path / "navigation"
        if not nav_path.exists():
            logger.warning(f"Navigation papka topilmadi: {nav_path}")
            return 0

        total = 0
        for json_file in nav_path.glob("*.json"):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    nav_data = json.load(f)

                chunks = self.chunker.chunk_navigation(
                    nav_data, source=json_file.name
                )
                saved = await self._save_chunks(chunks)
                total += saved
                logger.info(f"  ✓ {json_file.name}: {saved} nav chunk yuklandi")
            except Exception as e:
                logger.error(f"  ✗ {json_file.name} yuklashda xato: {e}")

        logger.info(f"Navigation: jami {total} chunk yuklandi")
        return total

    async def _save_chunks(self, chunks: List[dict]) -> int:
        """
        Chunklarni ChromaDB ga saqlash.

        Har bir chunk uchun:
        1. Matnni embedding (vektor) ga aylantirish
        2. Vektor + matn + metadata ni ChromaDB ga yozish

        Args:
            chunks: Chunklar ro'yxati
                [{"text": "...", "metadata": {...}}, ...]

        Returns:
            Saqlangan chunklar soni
        """
        if not chunks or not self.collection:
            return 0

        # ChromaDB ga saqlash uchun ma'lumotlarni tayyorlash
        ids = []          # Har bir chunk uchun unikal ID
        documents = []    # Matnlar
        metadatas = []    # Metadata lar
        embeddings = []   # Vektorlar

        for i, chunk in enumerate(chunks):
            text = chunk["text"]
            metadata = chunk.get("metadata", {})

            # Unikal ID yaratish: manba_turi_tartib_raqami
            source = metadata.get("source", "unknown")
            chunk_id = f"{source}_{metadata.get('type', 'doc')}_{i}"

            try:
                # Matnni vektor ga aylantirish
                embedding = await self.embedding_service.embed_text(text)

                ids.append(chunk_id)
                documents.append(text)
                metadatas.append(metadata)
                embeddings.append(embedding)

            except Exception as e:
                logger.warning(f"Chunk embedding xatosi (o'tkazildi): {e}")
                continue

        if not ids:
            return 0

        try:
            # ChromaDB ga birdaniga saqlash (batch upsert)
            # upsert = insert + update: bor bo'lsa yangilaydi, yo'q bo'lsa qo'shadi
            self.collection.upsert(
                ids=ids,
                documents=documents,
                metadatas=metadatas,
                embeddings=embeddings,
            )
            return len(ids)

        except Exception as e:
            logger.error(f"ChromaDB ga saqlashda xato: {e}")
            return 0
