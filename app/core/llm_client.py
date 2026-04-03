"""
UzASBO 2.0 AI Assistant — LLM Client (Claude + Ollama)

Bu modul LLM (Large Language Model) dan javob olish uchun ishlatiladi.
Ikki provider qo'llab-quvvatlanadi:
    - Claude (Anthropic API) — bulutli, sifatli, tez
    - Ollama — mahalliy, bepul, internet kerak emas

.env dagi LLM_PROVIDER sozlamasi orqali tanlanadi:
    LLM_PROVIDER=claude   → Claude API ishlatiladi
    LLM_PROVIDER=ollama   → Ollama server ishlatiladi
"""

import anthropic
from ollama import AsyncClient as OllamaAsyncClient
from loguru import logger
from typing import AsyncGenerator, Optional

from app.config import settings


class LLMClient:
    """
    LLM bilan ishlash uchun universal klient.
    Claude va Ollama ni bir xil interfeys orqali ishlatadi.

    Asosiy metodlar:
        generate()        — To'liq javob olish (bir marta)
        stream_generate() — Streaming javob (token-by-token)
        check_connection() — Serverga ulanishni tekshirish
    """

    def __init__(self):
        """
        LLM Client ni sozlash.
        .env dagi LLM_PROVIDER ga qarab Claude yoki Ollama tanlanadi.
        """
        # Qaysi provider ishlatiladi — "claude" yoki "ollama"
        self.provider = settings.llm.provider.lower()

        # Temperature — javobning "tasodifiylik" darajasi
        self.temperature = settings.rag.temperature

        if self.provider == "claude":
            # --- Claude API sozlash ---
            self.claude_client = anthropic.AsyncAnthropic(
                api_key=settings.claude.api_key,
            )
            self.model = settings.claude.model
            self.max_tokens = settings.claude.max_tokens
            logger.info(
                f"LLM Client yaratildi: provider=Claude, model={self.model}, "
                f"temperature={self.temperature}"
            )
        else:
            # --- Ollama sozlash ---
            self.ollama_client = OllamaAsyncClient(
                host=settings.ollama.base_url
            )
            self.model = settings.ollama.model
            logger.info(
                f"LLM Client yaratildi: provider=Ollama, model={self.model}, "
                f"temperature={self.temperature}"
            )

    # ============================================================
    # TO'LIQ JAVOB OLISH
    # ============================================================

    async def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> str:
        """
        LLM dan to'liq javob olish.
        REST API (/api/chat/message) uchun ishlatiladi.

        Args:
            prompt: Foydalanuvchi savoli + kontekst
            system_prompt: Tizim ko'rsatmalari

        Returns:
            AI javob matni (string)
        """
        if self.provider == "claude":
            return await self._claude_generate(prompt, system_prompt)
        else:
            return await self._ollama_generate(prompt, system_prompt)

    async def _claude_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> str:
        """Claude API orqali to'liq javob olish."""
        try:
            logger.debug(f"Claude ga so'rov: {prompt[:100]}...")

            # Claude API ga so'rov yuborish
            message = await self.claude_client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                # System prompt — alohida parametr sifatida
                system=system_prompt or "",
                messages=[
                    {"role": "user", "content": prompt}
                ],
            )

            # Javob matnini olish
            answer = message.content[0].text
            logger.debug(f"Claude javob: {answer[:100]}...")
            return answer

        except Exception as e:
            logger.error(f"Claude javob generatsiyada xato: {e}")
            raise

    async def _ollama_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> str:
        """Ollama orqali to'liq javob olish."""
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

            logger.debug(f"Ollama ga so'rov: {prompt[:100]}...")

            response = await self.ollama_client.chat(
                model=self.model,
                messages=messages,
                options={
                    "temperature": self.temperature,
                    "num_predict": 1024,
                },
            )

            answer = response["message"]["content"]
            logger.debug(f"Ollama javob: {answer[:100]}...")
            return answer

        except Exception as e:
            logger.error(f"Ollama javob generatsiyada xato: {e}")
            raise

    # ============================================================
    # STREAMING JAVOB OLISH (token-by-token)
    # ============================================================

    async def stream_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> AsyncGenerator[str, None]:
        """
        LLM dan streaming javob olish (token-by-token).
        WebSocket orqali foydalanuvchiga "yozilayotgan" effekt berish uchun.

        Args:
            prompt: Foydalanuvchi savoli + kontekst
            system_prompt: Tizim ko'rsatmalari

        Yields:
            Har bir yangi token alohida qaytariladi
        """
        if self.provider == "claude":
            async for token in self._claude_stream(prompt, system_prompt):
                yield token
        else:
            async for token in self._ollama_stream(prompt, system_prompt):
                yield token

    async def _claude_stream(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> AsyncGenerator[str, None]:
        """Claude API orqali streaming javob."""
        try:
            logger.debug(f"Claude streaming so'rov: {prompt[:100]}...")

            # Claude streaming — async context manager
            async with self.claude_client.messages.stream(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=system_prompt or "",
                messages=[
                    {"role": "user", "content": prompt}
                ],
            ) as stream:
                # Har bir token kelganda yield qilamiz
                async for text in stream.text_stream:
                    if text:
                        yield text

        except Exception as e:
            logger.error(f"Claude streaming xato: {e}")
            raise

    async def _ollama_stream(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> AsyncGenerator[str, None]:
        """Ollama orqali streaming javob."""
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

            logger.debug(f"Ollama streaming so'rov: {prompt[:100]}...")

            response_stream = await self.ollama_client.chat(
                model=self.model,
                messages=messages,
                stream=True,
                options={
                    "temperature": self.temperature,
                    "num_predict": 1024,
                },
            )

            async for chunk in response_stream:
                token = chunk["message"]["content"]
                if token:
                    yield token

        except Exception as e:
            logger.error(f"Ollama streaming xato: {e}")
            raise

    # ============================================================
    # ULANISH TEKSHIRISH
    # ============================================================

    async def check_connection(self) -> bool:
        """
        LLM serverga ulanishni tekshirish.

        Returns:
            True — server ishlayapti
            False — server ishlamayapti
        """
        if self.provider == "claude":
            return await self._check_claude()
        else:
            return await self._check_ollama()

    async def _check_claude(self) -> bool:
        """Claude API ulanishini tekshirish."""
        try:
            if not settings.claude.api_key:
                logger.warning("Claude API kaliti sozlanmagan")
                return False

            # Kichik test so'rov yuborish
            message = await self.claude_client.messages.create(
                model=self.model,
                max_tokens=10,
                messages=[
                    {"role": "user", "content": "ping"}
                ],
            )
            logger.debug(f"Claude ulanish OK, model='{self.model}'")
            return True

        except Exception as e:
            logger.error(f"Claude ulanish xatosi: {e}")
            return False

    async def _check_ollama(self) -> bool:
        """Ollama serverga ulanishni tekshirish."""
        try:
            models_response = await self.ollama_client.list()

            model_names = []
            for m in getattr(models_response, "models", []):
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
