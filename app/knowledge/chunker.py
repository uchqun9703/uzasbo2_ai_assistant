"""
UzASBO 2.0 AI Assistant — Matn bo'laklash (Chunking) moduli

Chunking nima?
    Katta matnni kichik bo'laklarga (chunk) bo'lish.
    LLM bir vaqtda cheklangan miqdorda matn o'qiy oladi.
    Shuning uchun matnni kichik qismlarga bo'lib,
    faqat keraklisini beramiz.

Nima uchun chunk kerak?
    1. LLM kontekst oynasi cheklangan (4K-128K token)
    2. Kichik chunk = aniqroq qidiruv natijasi
    3. Katta chunk = ko'proq kontekst, lekin shovqin (irrelevant ma'lumot)

Optimal chunk hajmi: 500-1000 belgi (UzASBO uchun 800 tanlangan)

Overlap nima?
    Ikki qo'shni chunk orasidagi takrorlanish.
    Chunk 1: "...to'lov topshiriqnomasi yaratish uchun shartnoma kerak."
    Chunk 2: "Shartnoma kerak. Shartnoma yaratish uchun kontragent tanlang..."
    "shartnoma kerak" — overlap qism. Bu kontekstning uzilmasligini ta'minlaydi.
"""

from loguru import logger
from typing import List, Optional
import re
import json


class TextChunker:
    """
    Matnni bo'laklash (chunking) uchun klass.

    Turli formatdagi matnlarni (Markdown, JSON, oddiy matn)
    ma'noli bo'laklarga bo'ladi.
    """

    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 200):
        """
        Chunker ni sozlash.

        Args:
            chunk_size: Har bir chunk ning maksimal hajmi (belgilarda)
            chunk_overlap: Ikki chunk orasidagi takrorlanish hajmi
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        logger.info(
            f"TextChunker yaratildi: chunk_size={chunk_size}, "
            f"overlap={chunk_overlap}"
        )

    def chunk_markdown(self, text: str, source: str = "") -> List[dict]:
        """
        Markdown formatdagi matnni bo'laklash.

        Markdown da sarlavhalar (##, ###) bo'yicha ajratadi.
        Har bir bo'lim alohida chunk bo'ladi.
        Agar bo'lim juda katta bo'lsa, paragraflar bo'yicha bo'linadi.

        Args:
            text: Markdown matn
            source: Manba fayl nomi (metadata uchun)

        Returns:
            Chunklar ro'yxati, har biri dict:
            [
                {
                    "text": "Chunk matni...",
                    "metadata": {
                        "source": "paymentorder.md",
                        "section": "Validatsiya qoidalari",
                        "document_type": "paymentorder",
                    }
                },
                ...
            ]
        """
        chunks = []

        # Markdown ni sarlavhalar bo'yicha bo'laklarga ajratish
        # ## yoki ### bilan boshlanuvchi qatorlar — bo'lim boshi
        sections = re.split(r'\n(?=#{1,3}\s)', text)

        for section in sections:
            section = section.strip()
            if not section:
                continue

            # Sarlavhani ajratib olish (birinchi qator)
            lines = section.split('\n')
            section_title = lines[0].strip('#').strip() if lines else ""

            # Hujjat turini sarlavhadan aniqlash
            doc_type = self._extract_document_type(section_title, source)

            # Agar bo'lim chunk_size dan kichik bo'lsa — to'liq chunk
            if len(section) <= self.chunk_size:
                chunks.append({
                    "text": section,
                    "metadata": {
                        "source": source,
                        "section": section_title,
                        "document_type": doc_type,
                        "type": "markdown",
                    }
                })
            else:
                # Katta bo'limni paragraflar bo'yicha bo'lish
                sub_chunks = self._split_by_size(section, section_title)
                for i, sub_text in enumerate(sub_chunks):
                    chunks.append({
                        "text": sub_text,
                        "metadata": {
                            "source": source,
                            "section": f"{section_title} (qism {i + 1})",
                            "document_type": doc_type,
                            "type": "markdown",
                        }
                    })

        logger.info(f"Markdown chunking: {source} → {len(chunks)} chunk")
        return chunks

    def chunk_errors_json(self, errors_data: list, source: str = "") -> List[dict]:
        """
        AddError (xato xabarlari) JSON ni bo'laklash.

        Har bir xato xabari alohida chunk bo'ladi.
        Bu eng muhim chunk turi — foydalanuvchilar ko'pincha
        "Nima uchun bu xato chiqyapti?" deb so'rashadi.

        Args:
            errors_data: Xato xabarlari ro'yxati
                [
                    {
                        "document_type": "paymentorder",
                        "error_message": "To'lov turi ko'rsatilmagan",
                        "condition": "paymentOrderType == null",
                        "field": "PaymentOrderType",
                        "explanation": "To'lov turini tanlash majburiy"
                    },
                    ...
                ]
            source: Manba fayl nomi

        Returns:
            Chunklar ro'yxati
        """
        chunks = []

        for error in errors_data:
            # Har bir xato uchun tushunarli matn yaratish
            error_text = self._format_error_chunk(error)
            doc_type = error.get("document_type", "unknown")

            chunks.append({
                "text": error_text,
                "metadata": {
                    "source": source,
                    "section": f"Xato: {error.get('error_message', '')}",
                    "document_type": doc_type,
                    "type": "error",
                    # Qo'shimcha metadata — aniqroq qidirish uchun
                    "error_message": error.get("error_message", ""),
                    "field": error.get("field", ""),
                }
            })

        logger.info(f"Error chunking: {source} → {len(chunks)} chunk")
        return chunks

    def chunk_faq(self, faq_text: str, source: str = "") -> List[dict]:
        """
        FAQ (Tez-tez beriladigan savollar) ni bo'laklash.

        Har bir savol-javob juftligi alohida chunk.
        FAQ formati:
            ## Savol matni?
            Javob matni...

        Args:
            faq_text: FAQ Markdown matni
            source: Manba fayl nomi

        Returns:
            Chunklar ro'yxati
        """
        chunks = []

        # "## " bilan boshlanuvchi savollar bo'yicha bo'lish
        qa_pairs = re.split(r'\n(?=##\s)', faq_text)

        for qa in qa_pairs:
            qa = qa.strip()
            if not qa or not qa.startswith('#'):
                continue

            # Savol matnini ajratish
            lines = qa.split('\n')
            question = lines[0].strip('#').strip()

            chunks.append({
                "text": qa,
                "metadata": {
                    "source": source,
                    "section": question,
                    "document_type": "faq",
                    "type": "faq",
                    "question": question,
                }
            })

        logger.info(f"FAQ chunking: {source} → {len(chunks)} chunk")
        return chunks

    def chunk_navigation(self, nav_data: list, source: str = "") -> List[dict]:
        """
        Navigatsiya yo'riqnomasini bo'laklash.

        Foydalanuvchi "Shartnoma qayerda?", "Oylik hisobi qanday topaman?"
        degan savollarga javob berish uchun.

        Args:
            nav_data: Navigatsiya elementlari ro'yxati
                [
                    {
                        "title": "To'lov topshiriqnomasi",
                        "path": "Moliya → To'lovlar → To'lov topshiriqnomasi",
                        "url": "/document/finance/paymentorder",
                        "description": "G'aznachilik orqali to'lov hujjati"
                    },
                    ...
                ]
            source: Manba fayl nomi

        Returns:
            Chunklar ro'yxati
        """
        chunks = []

        for item in nav_data:
            # Navigatsiya ma'lumotini matn shaklida yaratish
            nav_text = (
                f"Hujjat: {item.get('title', '')}\n"
                f"Joylashuvi: {item.get('path', '')}\n"
                f"Sahifa manzili: {item.get('url', '')}\n"
                f"Tavsif: {item.get('description', '')}"
            )

            chunks.append({
                "text": nav_text,
                "metadata": {
                    "source": source,
                    "section": item.get("title", ""),
                    "document_type": "navigation",
                    "type": "navigation",
                    "url": item.get("url", ""),
                }
            })

        logger.info(f"Navigation chunking: {source} → {len(chunks)} chunk")
        return chunks

    # ============================================================
    # Yordamchi (private) metodlar
    # ============================================================

    def _split_by_size(self, text: str, section_title: str = "") -> List[str]:
        """
        Katta matnni chunk_size bo'yicha bo'lish.

        Paragraflar chegarasida bo'lishga harakat qiladi.
        Agar paragraf ham katta bo'lsa, gap chegarasida bo'ladi.

        Args:
            text: Bo'linadigan matn
            section_title: Bo'lim sarlavhasi (kontekst uchun)

        Returns:
            Bo'laklar ro'yxati
        """
        chunks = []
        # Paragraflar bo'yicha ajratish (ikki yangi qator)
        paragraphs = text.split('\n\n')

        current_chunk = ""
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            # Agar joriy chunk + yangi paragraf sig'sa — qo'shamiz
            if len(current_chunk) + len(para) + 2 <= self.chunk_size:
                current_chunk += ("\n\n" + para if current_chunk else para)
            else:
                # Sig'masa — joriy chunk ni saqlab, yangi boshlaymiz
                if current_chunk:
                    chunks.append(current_chunk)
                    # Overlap — oldingi chunk ning oxirgi qismini
                    # yangi chunk boshiga qo'shish
                    overlap_text = current_chunk[-self.chunk_overlap:]
                    current_chunk = overlap_text + "\n\n" + para
                else:
                    # Bitta paragraf ham chunk_size dan katta bo'lsa
                    # Gaplar bo'yicha bo'lamiz
                    sentences = re.split(r'(?<=[.!?])\s+', para)
                    current_chunk = ""
                    for sentence in sentences:
                        if len(current_chunk) + len(sentence) + 1 <= self.chunk_size:
                            current_chunk += (" " + sentence if current_chunk else sentence)
                        else:
                            if current_chunk:
                                chunks.append(current_chunk)
                            current_chunk = sentence

        # Oxirgi chunk ni saqlash
        if current_chunk:
            chunks.append(current_chunk)

        return chunks

    def _format_error_chunk(self, error: dict) -> str:
        """
        Xato xabarini tushunarli matn formatiga aylantirish.

        Args:
            error: Xato ma'lumotlari dict

        Returns:
            Formatlangan matn

        Misol natija:
            "Hujjat turi: To'lov topshiriqnomasi
             Xato xabari: To'lov turi ko'rsatilmagan
             Sababi: paymentOrderType == null
             Maydon: PaymentOrderType
             Tushuntirish: To'lov turini tanlash majburiy"
        """
        parts = []

        if error.get("document_type"):
            parts.append(f"Hujjat turi: {error['document_type']}")
        if error.get("error_message"):
            parts.append(f"Xato xabari: {error['error_message']}")
        if error.get("condition"):
            parts.append(f"Sababi: {error['condition']}")
        if error.get("field"):
            parts.append(f"Maydon: {error['field']}")
        if error.get("explanation"):
            parts.append(f"Tushuntirish: {error['explanation']}")
        if error.get("solution"):
            parts.append(f"Yechim: {error['solution']}")

        return "\n".join(parts)

    def _extract_document_type(self, title: str, source: str) -> str:
        """
        Sarlavha yoki fayl nomidan hujjat turini aniqlash.

        Misol:
            "To'lov topshiriqnomasi" → "paymentorder"
            "paymentorder_guide.md" → "paymentorder"

        Args:
            title: Bo'lim sarlavhasi
            source: Manba fayl nomi

        Returns:
            Hujjat turi (kichik harflarda)
        """
        # Avval fayl nomidan aniqlash
        if source:
            # "paymentorder_guide.md" → "paymentorder"
            name = source.split('.')[0]        # ".md" ni olib tashlash
            name = name.split('_')[0]          # "_guide" ni olib tashlash
            if name:
                return name.lower()

        # Sarlavhadan aniqlash
        if title:
            return title.lower().replace(' ', '_')[:50]

        return "general"
