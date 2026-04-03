"""
UzASBO 2.0 AI Assistant — Ollama LLM Client

Bu modul Ollama server bilan bog'lanib, LLM (Large Language Model) dan
javob olish uchun ishlatiladi.

Ollama nima?
    Ollama — bu LLM modellarni (Llama, Mistral va boshqalar)
    mahalliy kompyuterda ishga tushirish uchun vosita.
    ChatGPT ga o'xshash, lekin internet kerak emas — hammasi lokalda.

Ishlash tartibi:
    1. LLMClient Ollama serverga HTTP so'rov yuboradi
    2. Ollama model orqali javob generatsiya qiladi
    3. Javob to'liq yoki streaming (token-by-token) qaytariladi
"""

import ollama
from ollama import AsyncClient
from loguru import logger
from typing import AsyncGenerator, Optional

from app.config import settings


class LLMClient:
    """
    Ollama LLM bilan ishlash uchun klient.

    Asosiy metodlar:
        generate()        — To'liq javob olish (bir marta)
        stream_generate() — Streaming javob (token-by-token)
        check_connection() — Serverga ulanishni tekshirish
    """

    def __init__(self):
        """
        LLM Client ni sozlash.
        Ollama server manzili va model nomi config dan olinadi.
        """
        # Ollama asinxron klient — async/await bilan ishlaydi
        # Bu serverning boshqa so'rovlarni bloklamasligini ta'minlaydi
        self.client = AsyncClient(host=settings.ollama.base_url)

        # Model nomi — masalan: "llama3.1:8b"
        self.model = settings.ollama.model

        # Temperature — javobning "tasodifiylik" darajasi
        # 0.0 = har doim bir xil javob (deterministic)
        # 1.0 = har safar boshqacha, ijodiy javob
        # AI assistant uchun 0.1-0.3 optimal
        self.temperature = settings.rag.temperature

        logger.info(
            f"LLM Client yaratildi: model={self.model}, "
            f"temperature={self.temperature}"
        )

    async def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> str:
        """
        LLM dan to'liq javob olish.

        Bu metod butun javobni kutadi va birdaniga qaytaradi.
        REST API (/api/chat/message) uchun ishlatiladi.

        Args:
            prompt: Foydalanuvchi savoli + kontekst
            system_prompt: Tizim ko'rsatmalari (AI qanday javob berishini belgilaydi)

        Returns:
            AI javob matni (string)

        Misol:
            answer = await llm.generate(
                prompt="To'lov topshiriqnomasi nima?",
                system_prompt="Sen UzASBO yordamchisisan..."
            )
        """
        try:
            # Xabarlar ro'yxati — Ollama ga yuboradigan formatda
            messages = []

            # System prompt — AI ga "sen kimsan va qanday javob ber" degan ko'rsatma
            if system_prompt:
                messages.append({
                    "role": "system",      # Tizim xabari — foydalanuvchiga ko'rinmaydi
                    "content": system_prompt,
                })

            # Foydalanuvchi xabari
            messages.append({
                "role": "user",
                "content": prompt,
            })

            logger.debug(f"LLM ga so'rov: {prompt[:100]}...")

            # Ollama API ga so'rov yuborish
            response = await self.client.chat(
                model=self.model,
                messages=messages,
                options={
                    "temperature": self.temperature,
                    # num_predict — maksimal token soni (javob uzunligi)
                    # 1 token ≈ 0.75 so'z (ingliz tilida)
                    # O'zbek tilida kamroq, chunki tokenizer ingliz tiliga optimallashtirilgan
                    "num_predict": 1024,
                },
            )

            # Javob matnini olish
            answer = response["message"]["content"]
            logger.debug(f"LLM javob: {answer[:100]}...")
            return answer

        except Exception as e:
            logger.error(f"LLM javob generatsiyada xato: {e}")
            raise

    async def stream_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> AsyncGenerator[str, None]:
        """
        LLM dan streaming javob olish (token-by-token).

        Bu metod generator — har bir token tayyor bo'lganda
        uni darhol qaytaradi (yield). WebSocket orqali
        foydalanuvchiga "yozilayotgan" effekt berish uchun.

        Args:
            prompt: Foydalanuvchi savoli + kontekst
            system_prompt: Tizim ko'rsatmalari

        Yields:
            Har bir yangi token (so'z bo'lagi) alohida qaytariladi

        Misol:
            async for token in llm.stream_generate("Savol"):
                print(token, end="")  # "To'" → "lov" → " topshiriq" → "nomasi"
        """
        try:
            messages = []
            if system_prompt:
                messages.append({
                    "role": "system",
                    "content": system_prompt,
                })
            messages.append({
                "role": "user",
                "content": prompt,
            })

            logger.debug(f"LLM streaming so'rov: {prompt[:100]}...")

            # stream=True — javobni bo'laklab olish
            response_stream = await self.client.chat(
                model=self.model,
                messages=messages,
                stream=True,  # Streaming rejim yoqildi
                options={
                    "temperature": self.temperature,
                    "num_predict": 1024,
                },
            )

            # Har bir chunk (bo'lak) kelganda yield qilamiz
            # yield = return ga o'xshash, lekin funksiya davom etadi
            async for chunk in response_stream:
                # chunk["message"]["content"] — bitta token matni
                token = chunk["message"]["content"]
                if token:
                    yield token

        except Exception as e:
            logger.error(f"LLM streaming xato: {e}")
            raise

    async def check_connection(self) -> bool:
        """
        Ollama serverga ulanishni tekshirish.
        Health check va diagnostika uchun.

        Returns:
            True — server ishlayapti va model mavjud
            False — server ishlamayapti yoki model topilmadi
        """
        try:
            # Ollama serverda mavjud modellar ro'yxatini so'rash
            models_response = await self.client.list()

            # Yangi Ollama SDK da models — obyektlar ro'yxati (.model atributi)
            # Eski SDK da — dict ro'yxati ("name" kaliti)
            model_names = []
            for m in getattr(models_response, "models", []):
                # Yangi SDK: m.model yoki m.name
                name = getattr(m, "model", None) or getattr(m, "name", None)
                if name:
                    model_names.append(name)

            if self.model in model_names:
                logger.debug(f"Ollama ulanish OK, model '{self.model}' mavjud")
                return True
            else:
                logger.warning(
                    f"Ollama server ishlayapti, lekin '{self.model}' model topilmadi. "
                    f"Mavjud modellar: {model_names}"
                )
                return False
        except Exception as e:
            logger.error(f"Ollama ulanish xatosi: {e}")
            return False
