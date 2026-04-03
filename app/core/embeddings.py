"""
UzASBO 2.0 AI Assistant — Embedding (vektorlashtirish) moduli

Embedding nima?
    Matnni raqamlar ro'yxatiga (vektor) aylantirish.
    Masalan: "To'lov topshiriqnomasi" → [0.12, -0.45, 0.78, ..., 0.33]
    Bu vektor matnning "ma'nosi"ni ifodalaydi.

Nima uchun kerak?
    Ikki matnning o'xshashligini hisoblash uchun.
    Misol: "To'lov hujjati" va "Platezhnoe poruchenie" vektorlari
    bir-biriga yaqin bo'ladi, chunki ma'nolari o'xshash.

RAG tizimda qo'llanilishi:
    1. Knowledge Base dagi barcha matnlar embedding ga aylantiriladi
    2. Foydalanuvchi savoli ham embedding ga aylantiriladi
    3. Savol vektori va KB vektorlari o'rtasidagi masofa hisoblanadi
    4. Eng yaqin vektorlar = eng tegishli ma'lumotlar
"""

from ollama import AsyncClient
from loguru import logger
from typing import List

from app.config import settings


class EmbeddingService:
    """
    Matnni vektor (embedding) ga aylantirish servisi.

    Ollama ning nomic-embed-text modeli ishlatiladi.
    Bu model 768 o'lchamli vektor qaytaradi
    (har bir matn 768 ta raqam bilan ifodalanadi).
    """

    def __init__(self):
        """
        Embedding servisini sozlash.
        """
        # Ollama asinxron klient
        self.client = AsyncClient(host=settings.ollama.base_url)
        # Embedding model nomi
        self.model = settings.ollama.embed_model
        logger.info(f"Embedding servisi yaratildi: model={self.model}")

    async def embed_text(self, text: str) -> List[float]:
        """
        Bitta matnni vektor ga aylantirish.

        Args:
            text: Vektorlashtirilishi kerak bo'lgan matn
                  Masalan: "To'lov topshiriqnomasi qanday yaratiladi?"

        Returns:
            Vektor — raqamlar ro'yxati [0.12, -0.45, 0.78, ...]
            Uzunligi model ga bog'liq (nomic-embed-text: 768)

        Misol:
            vector = await embedding.embed_text("To'lov topshiriqnomasi")
            print(len(vector))  # 768
        """
        try:
            # Ollama embedding API ga so'rov
            response = await self.client.embeddings(
                model=self.model,
                prompt=text,
            )
            # Javobdan vektor ni olish
            embedding = response["embedding"]
            logger.debug(
                f"Embedding yaratildi: matn={text[:50]}..., "
                f"vektor_uzunligi={len(embedding)}"
            )
            return embedding

        except Exception as e:
            logger.error(f"Embedding yaratishda xato: {e}")
            raise

    async def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Bir nechta matnni birdaniga vektorlashtirish.

        Knowledge Base yuklashda ishlatiladi — minglab matnni
        bir-bir emas, to'plab vektorlashtiramiz.

        Args:
            texts: Matnlar ro'yxati
                   ["To'lov topshiriqnomasi", "Shartnoma", "Smeta"]

        Returns:
            Vektorlar ro'yxati — har bir matnga bitta vektor
            [[0.12, ...], [0.34, ...], [0.56, ...]]

        Misol:
            vectors = await embedding.embed_texts([
                "To'lov topshiriqnomasi",
                "Shartnoma",
                "Smeta"
            ])
            print(len(vectors))     # 3
            print(len(vectors[0]))  # 768
        """
        try:
            embeddings = []
            # Har bir matnni alohida vektorlashtiramiz
            # TODO: Ollama batch embedding qo'llab-quvvatlasa, optimizatsiya qilish
            for i, text in enumerate(texts):
                embedding = await self.embed_text(text)
                embeddings.append(embedding)

                # Har 100 ta matnda progress log yozamiz
                if (i + 1) % 100 == 0:
                    logger.info(f"Embedding progress: {i + 1}/{len(texts)}")

            logger.info(f"Jami {len(embeddings)} ta embedding yaratildi")
            return embeddings

        except Exception as e:
            logger.error(f"Batch embedding yaratishda xato: {e}")
            raise

    async def check_model(self) -> bool:
        """
        Embedding model mavjudligini tekshirish.
        Oddiy matn bilan sinab ko'radi.

        Returns:
            True — model ishlayapti
            False — model topilmadi yoki ishlamayapti
        """
        try:
            # Test embedding — ishlashini tekshirish uchun
            test_embedding = await self.embed_text("test")
            if test_embedding and len(test_embedding) > 0:
                logger.debug(
                    f"Embedding model OK: '{self.model}', "
                    f"vektor_uzunligi={len(test_embedding)}"
                )
                return True
            return False
        except Exception as e:
            logger.error(f"Embedding model tekshiruvida xato: {e}")
            return False
