"""
UzASBO 2.0 AI Assistant — RAG Engine (Asosiy motor)

RAG = Retrieval-Augmented Generation
    Qidirish bilan kuchaytirilgan generatsiya.

Oddiy LLM muammosi:
    LLM faqat o'qitilgan ma'lumotlarni biladi.
    UzASBO 2.0 haqida hech narsa bilmaydi.
    Masalan: "To'lov topshiriqnomasi" nima ekanini bilmaydi.

RAG yechimi:
    1. RETRIEVAL (Qidirish): Savolga tegishli ma'lumotni Knowledge Base dan topamiz
    2. AUGMENTED (Kuchaytirilgan): Topilgan ma'lumotni LLM ga kontekst sifatida beramiz
    3. GENERATION (Generatsiya): LLM shu kontekst asosida javob yaratadi

Natija: LLM UzASBO haqida "bilgandek" javob beradi,
chunki biz unga kerakli ma'lumotni berib turganmiz.

Misol:
    Savol: "To'lov topshiriqnomasi qanday yaratiladi?"

    1. ChromaDB dan "To'lov topshiriqnomasi" haqidagi chunklar topiladi
    2. Chunklar + savol LLM ga yuboriladi:
       "Kontekst: To'lov topshiriqnomasi — bu... API: /fin/PaymentOrder...
        Savol: To'lov topshiriqnomasi qanday yaratiladi?"
    3. LLM kontekstga asoslangan javob beradi
"""

import chromadb
from chromadb.config import Settings as ChromaSettings
from loguru import logger
from typing import Optional, AsyncGenerator

from app.config import settings
from app.core.llm_client import LLMClient
from app.core.embeddings import EmbeddingService


class RAGEngine:
    """
    RAG (Retrieval-Augmented Generation) asosiy motori.

    Bu klass quyidagi vazifalarni bajaradi:
    1. ChromaDB dan tegishli ma'lumotlarni qidirish (retrieval)
    2. Topilgan ma'lumotlarni kontekst sifatida tayyorlash
    3. LLM orqali javob generatsiya qilish (generation)
    """

    # ============================================================
    # Singleton pattern — dastur davomida faqat bitta RAGEngine bo'ladi
    # Bu resurslarni tejaydi (har safar yangi ulanish ochmaslik uchun)
    # ============================================================
    _instance = None

    def __new__(cls):
        """
        Singleton: faqat bitta RAGEngine obyekti yaratiladi.
        Ikkinchi marta RAGEngine() chaqirilsa, avvalgi obyekt qaytariladi.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """RAG Engine komponentlarini yaratish."""
        if self._initialized:
            return  # Singleton — qayta ishga tushirmaslik

        # LLM klient — javob generatsiya qilish uchun
        self.llm = LLMClient()
        # Embedding servisi — matnni vektor ga aylantirish uchun
        self.embedding_service = EmbeddingService()
        # ChromaDB klient — vektorli qidirish uchun
        self.chroma_client = None
        # ChromaDB kolleksiya — ma'lumotlar to'plami
        self.collection = None

        self._initialized = True
        logger.info("RAG Engine yaratildi")

    async def initialize(self):
        """
        RAG Engine ni ishga tushirish.
        ChromaDB ga ulanish va kolleksiya yaratish/olish.
        Dastur boshlanishida bir marta chaqiriladi (main.py → lifespan).
        """
        try:
            # ChromaDB HTTP klient — alohida server sifatida ishlaydi
            self.chroma_client = chromadb.HttpClient(
                host=settings.chroma.host,
                port=settings.chroma.port,
                settings=ChromaSettings(
                    anonymized_telemetry=False,  # Telemetriya o'chirilgan
                ),
            )

            # Kolleksiya yaratish yoki mavjudini olish
            # Kolleksiya = oddiy DB dagi "jadval" ga o'xshash
            # get_or_create — bor bo'lsa oladi, yo'q bo'lsa yaratadi
            self.collection = self.chroma_client.get_or_create_collection(
                name=settings.chroma.collection,
                # Metadata — kolleksiya haqida ma'lumot
                metadata={
                    "description": "UzASBO 2.0 Knowledge Base",
                    "hnsw:space": "cosine",  # O'xshashlik o'lchash metodi
                    # cosine = burchak bo'yicha o'xshashlik (0-1)
                    # 1.0 = bir xil ma'no, 0.0 = hech qanday o'xshashlik
                },
            )

            chunk_count = self.collection.count()
            logger.info(
                f"ChromaDB ulandi. Kolleksiya: '{settings.chroma.collection}', "
                f"chunklar soni: {chunk_count}"
            )

        except Exception as e:
            logger.error(f"ChromaDB ulanishda xato: {e}")
            logger.warning(
                "ChromaDB ulana olmadi. 'docker-compose up chromadb' "
                "buyrug'i bilan ChromaDB ni ishga tushiring."
            )

    def _build_system_prompt(self, language: str) -> str:
        """
        System prompt yaratish.

        System prompt — AI ga "sen kimsan va qanday javob ber" degan ko'rsatma.
        Bu LLM ning xatti-harakatini belgilaydi.
        Yaxshi system prompt = yaxshi javoblar.

        Args:
            language: Foydalanuvchi tili ("uz_latn", "uz_cyrl", "ru")

        Returns:
            System prompt matni
        """
        # Til bo'yicha ko'rsatma
        language_instructions = {
            "uz_latn": "O'zbek tilida (lotin alifbosida) javob ber.",
            "uz_cyrl": "Ўзбек тилида (кирилл алифбосида) жавоб бер.",
            "ru": "Отвечай на русском языке.",
        }
        lang_instruction = language_instructions.get(
            language,
            "O'zbek tilida javob ber."
        )

        return f"""Sen UzASBO 2.0 tizimining sun'iy intellekt yordamchisisan.
Vazifang — foydalanuvchilarga tizimdan foydalanishda yordam berish.

QOIDALAR:
1. Faqat berilgan kontekst asosida javob ber
2. Bilmagan narsangni to'qib chiqarma — "Bu haqida ma'lumotim yo'q" de
3. {lang_instruction}
4. Qisqa, aniq va tushunarli javob ber
5. Agar xatolik (error) haqida so'ralsa, sababini va yechimini tushuntir
6. Hujjat yaratish haqida so'ralsa, qadamma-qadam ko'rsatma ber
7. Texnik atamalarni oddiy tilda tushuntir
8. Agar javob bera olmasang, "Operator bilan bog'laning" deb maslahat ber

KONTEKST HAQIDA:
- Kontekstda hujjat turlari, xato xabarlari va yo'riqnomalar bor
- Kontekstda "API endpoint" degan ma'lumot — dasturchilar uchun, oddiy foydalanuvchiga aytish shart emas
- "AddError" — bu tizim ko'rsatadigan xato xabarlari
- "Bog'liq hujjatlar" — boshqa tegishli hujjatlar ro'yxati
"""

    def _build_context_prompt(
        self,
        question: str,
        context_chunks: list,
        current_page: Optional[str] = None,
    ) -> str:
        """
        Foydalanuvchi savoli va topilgan kontekstni birlashtirish.

        Bu funksiya LLM ga yuboriladigan yakuniy promptni yaratadi.
        Prompt = Kontekst + Sahifa ma'lumoti + Savol

        Args:
            question: Foydalanuvchi savoli
            context_chunks: ChromaDB dan topilgan tegishli matn bo'laklari
            current_page: Foydalanuvchi joriy sahifasi (ixtiyoriy)

        Returns:
            LLM ga yuboriladigan prompt matni
        """
        # Kontekst chunklarni bitta matnga birlashtirish
        # Har bir chunk raqamlanadi (oson ko'rish uchun)
        if context_chunks:
            context_text = "\n\n".join([
                f"--- Ma'lumot #{i + 1} ---\n{chunk}"
                for i, chunk in enumerate(context_chunks)
            ])
        else:
            context_text = "Tegishli ma'lumot topilmadi."

        # Sahifa konteksti — AI ga foydalanuvchi qayerda turganini aytish
        page_context = ""
        if current_page:
            page_context = f"\nFoydalanuvchi hozir quyidagi sahifada: {current_page}\n"

        return f"""KONTEKST (quyidagi ma'lumotlar asosida javob ber):
{context_text}
{page_context}
FOYDALANUVCHI SAVOLI: {question}

JAVOB:"""

    async def _retrieve_context(
        self,
        question: str,
        current_page: Optional[str] = None,
    ) -> dict:
        """
        ChromaDB dan savolga tegishli ma'lumotlarni qidirish.

        Bu RAG ning "Retrieval" (Qidirish) bosqichi.
        Savol vektori bilan Knowledge Base vektorlarini taqqoslaydi
        va eng o'xshash chunklar ni qaytaradi.

        Args:
            question: Foydalanuvchi savoli
            current_page: Joriy sahifa (qo'shimcha filtr uchun)

        Returns:
            dict: {
                "chunks": [matn1, matn2, ...],  — topilgan matnlar
                "sources": [manba1, manba2, ...], — manbalar
                "distances": [0.1, 0.2, ...],     — masofa (kichik = yaqin)
            }
        """
        if not self.collection:
            logger.warning("ChromaDB kolleksiya mavjud emas")
            return {"chunks": [], "sources": [], "distances": []}

        try:
            # 1-qadam: Savol matnini vektor ga aylantirish
            question_embedding = await self.embedding_service.embed_text(question)

            # 2-qadam: Qidirish parametrlarini tayyorlash
            query_params = {
                "query_embeddings": [question_embedding],
                # n_results — nechta eng yaqin chunk qaytarilsin
                "n_results": settings.rag.top_k,
            }

            # Agar foydalanuvchi ma'lum sahifada bo'lsa,
            # avval shu sahifaga tegishli chunklar qidiriladi
            if current_page:
                # current_page dan hujjat turini ajratib olish
                # Masalan: "/document/finance/paymentorder/edit/123"
                # → "paymentorder"
                page_parts = current_page.strip("/").split("/")
                # Sahifaga tegishli chunklar uchun metadata filtr
                # (ixtiyoriy — agar metadata bo'lmasa, umumiy qidirish)
                if len(page_parts) >= 3:
                    doc_type = page_parts[-1] if len(page_parts) == 3 else page_parts[2]
                    query_params["where"] = {
                        "document_type": {"$eq": doc_type}
                    }

            # 3-qadam: ChromaDB dan qidirish
            try:
                results = self.collection.query(**query_params)
            except Exception:
                # Metadata filtr bilan topilmasa, filtrsiz qayta qidirish
                if "where" in query_params:
                    del query_params["where"]
                    results = self.collection.query(**query_params)
                else:
                    raise

            # 4-qadam: Natijalarni formatlash
            chunks = results.get("documents", [[]])[0]
            metadatas = results.get("metadatas", [[]])[0]
            distances = results.get("distances", [[]])[0]

            # Manbalar ro'yxati — har bir chunk qaysi fayldan olinganini ko'rsatish
            sources = []
            for meta in metadatas:
                if meta and "source" in meta:
                    source = meta["source"]
                    if source not in sources:
                        sources.append(source)

            logger.debug(
                f"Qidiruv natijasi: {len(chunks)} chunk topildi, "
                f"manbalar: {sources}"
            )

            return {
                "chunks": chunks,
                "sources": sources,
                "distances": distances,
            }

        except Exception as e:
            logger.error(f"Kontekst qidirishda xato: {e}")
            return {"chunks": [], "sources": [], "distances": []}

    def _calculate_confidence(self, distances: list) -> float:
        """
        Javob ishonch darajasini hisoblash.

        ChromaDB qaytargan masofa (distance) asosida hisoblanadi.
        Masofa kichik = kontekst savol ga yaqin = ishonch yuqori.

        Cosine distance: 0.0 = bir xil, 2.0 = butunlay farqli
        Biz buni 0.0-1.0 oraliqqa aylantiramiz.

        Args:
            distances: ChromaDB qaytargan masofalar ro'yxati

        Returns:
            Ishonch darajasi (0.0 — 1.0)
        """
        if not distances:
            return 0.0

        # O'rtacha masofani hisoblash
        avg_distance = sum(distances) / len(distances)
        # Masofani ishonch darajasiga aylantirish
        # distance=0 → confidence=1.0, distance=2 → confidence=0.0
        confidence = max(0.0, min(1.0, 1.0 - (avg_distance / 2.0)))
        return round(confidence, 2)

    async def get_answer(
        self,
        question: str,
        current_page: Optional[str] = None,
        language: str = "uz_latn",
        session_id: Optional[str] = None,
    ) -> dict:
        """
        Foydalanuvchi savoliga javob berish (to'liq RAG pipeline).

        Bu asosiy metod — REST API dan chaqiriladi.
        Barcha RAG bosqichlarini ketma-ket bajaradi:
        1. Retrieval — tegishli ma'lumot topish
        2. Augmentation — kontekst tayyorlash
        3. Generation — javob yaratish

        Args:
            question: Foydalanuvchi savoli
            current_page: Joriy sahifa URL i
            language: Javob tili
            session_id: Sessiya ID si

        Returns:
            dict: {
                "answer": "Javob matni...",
                "sources": ["manba1.md", "manba2.json"],
                "confidence": 0.87
            }
        """
        logger.info(f"RAG savol: '{question[:80]}...' (til={language})")

        # 1-BOSQICH: RETRIEVAL — ChromaDB dan tegishli ma'lumotlar topish
        context_data = await self._retrieve_context(question, current_page)
        chunks = context_data["chunks"]
        sources = context_data["sources"]
        distances = context_data["distances"]

        # 2-BOSQICH: AUGMENTATION — promptni tayyorlash
        system_prompt = self._build_system_prompt(language)
        user_prompt = self._build_context_prompt(question, chunks, current_page)

        # 3-BOSQICH: GENERATION — LLM dan javob olish
        try:
            answer = await self.llm.generate(
                prompt=user_prompt,
                system_prompt=system_prompt,
            )
        except Exception as e:
            logger.error(f"LLM javob berishda xato: {e}")
            # LLM ishlamasa, foydalanuvchiga tushunarli xabar
            answer = (
                "Kechirasiz, hozir javob bera olmayapman. "
                "Iltimos, keyinroq qayta urinib ko'ring yoki "
                "operator bilan bog'laning."
            )

        # 4-BOSQICH: Ishonch darajasini hisoblash
        confidence = self._calculate_confidence(distances)

        logger.info(
            f"RAG javob tayyor: ishonch={confidence}, "
            f"manbalar={sources}, javob_uzunligi={len(answer)}"
        )

        return {
            "answer": answer,
            "sources": sources,
            "confidence": confidence,
        }

    async def stream_answer(
        self,
        question: str,
        current_page: Optional[str] = None,
        language: str = "uz_latn",
        session_id: Optional[str] = None,
    ) -> AsyncGenerator[dict, None]:
        """
        Foydalanuvchi savoliga streaming javob (WebSocket uchun).

        get_answer() ga o'xshash, lekin javobni token-by-token qaytaradi.
        Foydalanuvchi har bir so'zni yozilayotganini ko'radi.

        Args:
            question: Foydalanuvchi savoli
            current_page: Joriy sahifa
            language: Javob tili
            session_id: Sessiya ID

        Yields:
            dict: {"type": "token", "content": "So'z"}  — har bir token
            dict: {"type": "metadata", "sources": [...], "confidence": 0.87}
        """
        logger.info(f"RAG streaming: '{question[:80]}...'")

        # 1. Kontekst topish (bir xil get_answer bilan)
        context_data = await self._retrieve_context(question, current_page)
        chunks = context_data["chunks"]
        sources = context_data["sources"]
        distances = context_data["distances"]

        # 2. Prompt tayyorlash
        system_prompt = self._build_system_prompt(language)
        user_prompt = self._build_context_prompt(question, chunks, current_page)

        # 3. LLM dan streaming javob
        try:
            async for token in self.llm.stream_generate(
                prompt=user_prompt,
                system_prompt=system_prompt,
            ):
                # Har bir tokenni yield qilamiz
                yield {"type": "token", "content": token}

        except Exception as e:
            logger.error(f"Streaming xato: {e}")
            yield {
                "type": "token",
                "content": "Kechirasiz, javob berish imkoni bo'lmadi."
            }

        # 4. Metadata (manbalar va ishonch) — oxirida yuboriladi
        confidence = self._calculate_confidence(distances)
        yield {
            "type": "metadata",
            "sources": sources,
            "confidence": confidence,
        }

    # ============================================================
    # Health check metodlari — monitoring uchun
    # ============================================================

    async def check_ollama_connection(self) -> bool:
        """Ollama server ulanishini tekshirish."""
        return await self.llm.check_connection()

    async def check_chroma_connection(self) -> bool:
        """ChromaDB ulanishini tekshirish."""
        try:
            if self.chroma_client:
                # Heartbeat — server ishlayotganini tekshirish
                self.chroma_client.heartbeat()
                return True
            return False
        except Exception as e:
            logger.error(f"ChromaDB tekshiruvida xato: {e}")
            return False

    async def get_knowledge_base_count(self) -> int:
        """Knowledge Base dagi chunklar sonini qaytarish."""
        try:
            if self.collection:
                return self.collection.count()
            return 0
        except Exception:
            return 0
