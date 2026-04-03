"""
UzASBO 2.0 AI Assistant — Xato shablonlari (Error Patterns) parser

Bu skript backend koddagi AddError larni analiz qilib,
SHABLON + SABAB + YECHIM formatda knowledge base yaratadi.

Muammo:
    Koddagi ko'p xatolar dinamik — masalan:
    AddError($"{table.RowName} to'lov turi uchun ... kiritilmagan");
    Bu xabarni oldindan bilish mumkin emas chunki table.RowName bazadan keladi.

Yechim:
    Dinamik qismlarni {..} bilan almashtirib SHABLON yaratamiz:
    "{to'lov_turi} to'lov turi uchun ... kiritilmagan"
    Va har bir shablonga SABAB va YECHIM yozamiz.

Ishga tushirish:
    python scripts/parse_error_patterns.py --backend-path D:/Projects/IVC/UZASBO/uzasbo2_backend
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
import argparse


# ============================================================
# Xato shablonlari — qo'lda yoziladigan yechimlar
# Har bir noyob xato turi uchun sabab va yechim
# ============================================================

ERROR_SOLUTIONS = {
    # --- TO'LOV VA HISOBRAQAM XATOLARI ---
    "hisobraqam_kiritilmagan": {
        "pattern": "тўлов тури учун.*ҳисобрақамлар қисмига маълумот киритилмаган",
        "shablon": "{to'lov_turi} to'lov turi uchun hisobraqam ma'lumotlari kiritilmagan",
        "sabab": "Ushbu to'lov turi uchun pul o'tkaziladigan hisobraqam tizimga kiritilmagan.",
        "yechim": "1. Hujjatlar bo'limiga o'ting\n2. To'lov hujjatlari → To'lov turlari bo'limini tanlang\n3. Kerakli to'lov turini toping (masalan: Kasaba uyushmasi)\n4. 'Pul o'tkaziladigan hisobraqamlar' qismini to'ldiring\n5. Saqlang va hujjatni qaytadan tasdiqlang",
        "hujjat_turi": "Naqd pul olish so'rovnomasi, To'lov topshiriqnomasi",
    },
    "bank_topilmadi": {
        "pattern": "банк.*топилмади|bank.*null|банк коди.*бўйича",
        "shablon": "Bank ma'lumotlari topilmadi",
        "sabab": "Kontragent yoki tashkilot uchun bank rekvizitlari tizimga kiritilmagan.",
        "yechim": "1. Ma'lumotnomalar bo'limiga o'ting\n2. Bank rekvizitlari bo'limini tanlang\n3. Kerakli tashkilot/kontragent uchun bank ma'lumotlarini kiriting\n4. Bank nomi, MFO, hisobraqam maydonlarini to'ldiring\n5. Saqlang",
        "hujjat_turi": "To'lov topshiriqnomasi, To'lov reyestri",
    },
    "kontragent_hisobraqam_topilmadi": {
        "pattern": "контрагент ҳисоб рақами топилмади|контрагент.*счет.*не найден",
        "shablon": "Kontragent hisob raqami topilmadi",
        "sabab": "Tanlangan kontragent uchun hisob raqami tizimda mavjud emas.",
        "yechim": "1. Ma'lumotnomalar → Kontragentlar bo'limiga o'ting\n2. Kerakli kontragentni toping\n3. 'Hisob raqamlari' qismini oching\n4. Bank va hisob raqam ma'lumotlarini kiriting\n5. Saqlang",
        "hujjat_turi": "To'lov topshiriqnomasi",
    },

    # --- SUMMA XATOLARI ---
    "summa_manfiy": {
        "pattern": "сумма манфий бўлиши мумкин эмас|summa.*nol|сумма.*ноль",
        "shablon": "Hujjatda summa manfiy yoki nol bo'lishi mumkin emas",
        "sabab": "Hujjatdagi summa 0 dan katta bo'lishi kerak.",
        "yechim": "1. Hujjatni oching\n2. Summa maydonini tekshiring\n3. To'g'ri (musbat) summani kiriting\n4. Saqlang va qayta tasdiqlang",
        "hujjat_turi": "Barcha moliyaviy hujjatlar",
    },
    "summa_mos_emas": {
        "pattern": "сумма мос эмас|суммага мос келмайди|сумма.*ошиб кетяпти",
        "shablon": "Hujjatdagi summalar bir-biriga mos kelmaydi",
        "sabab": "Hujjat ichidagi summalar (ish haqi, ushlama, to'lov) bir-biriga mos kelmaydi.",
        "yechim": "1. Hujjatni oching\n2. Barcha qatorlardagi summalarni tekshiring\n3. Ish haqi to'lovi + Ushlama = Hisoblangan ish haqi ekanini tekshiring\n4. Noto'g'ri summani to'g'rilang\n5. Saqlang va qayta tasdiqlang",
        "hujjat_turi": "Naqd pul olish so'rovnomasi, Ish haqi hisob-kitobi",
    },

    # --- FOIZ XATOLARI ---
    "foiz_100_emas": {
        "pattern": "фоиз 100 га тенг бўлиши керак|foiz.*100|процент.*100",
        "shablon": "Jami foiz 100% ga teng bo'lishi kerak",
        "sabab": "To'lov turlari bo'yicha taqsimlangan foizlar yig'indisi 100% ga teng emas.",
        "yechim": "1. Hujjatni oching\n2. To'lov turlari bo'yicha foizlar qismini tekshiring\n3. Barcha foizlar yig'indisi 100% bo'lishini ta'minlang\n4. Saqlang va qayta tasdiqlang",
        "hujjat_turi": "Naqd pul olish so'rovnomasi",
    },

    # --- XARAJAT KODI XATOLARI ---
    "xarajat_kodi_taqiqlangan": {
        "pattern": "ушбу харажат кодидан фойдаланиш мумкин эмас|xarajat kod.*mumkin emas",
        "shablon": "{xarajat_kodi} xarajat kodidan foydalanish mumkin emas",
        "sabab": "Tanlangan xarajat kodi bu hujjat turi uchun ruxsat etilmagan.",
        "yechim": "1. Hujjatni oching\n2. Xarajat kodi maydonini tekshiring\n3. Ruxsat etilgan boshqa xarajat kodini tanlang\n4. Agar qaysi kodni tanlashni bilmasangiz, buxgalteriyaga murojaat qiling",
        "hujjat_turi": "Naqd pul olish so'rovnomasi, To'lov topshiriqnomasi",
    },
    "statiya_ushlama_yoq": {
        "pattern": "statiya uchun ushlama mavjud emas",
        "shablon": "{xarajat_kodi} statiya uchun ushlama mavjud emas",
        "sabab": "Tanlangan xarajat kodiga tegishli ushlama (ushlanma) ma'lumotlari topilmadi.",
        "yechim": "1. Xarajat kodi va ushlama turini tekshiring\n2. Ma'lumotnomalar → Ushlama turlari bo'limida kerakli ushlama mavjudligini tekshiring\n3. Agar mavjud bo'lmasa, yangi ushlama turini qo'shing\n4. Hujjatni qayta tasdiqlang",
        "hujjat_turi": "Naqd pul olish so'rovnomasi",
    },

    # --- INDEKSATSIYA XATOLARI ---
    "indeksatsiya_yoq": {
        "pattern": "индексация ҳужжати яратилмаган|индексация.*керак",
        "shablon": "{sana} davr uchun indeksatsiya hujjati yaratilmagan",
        "sabab": "Ish haqi indeksatsiya hujjati bu davr uchun yaratilmagan.",
        "yechim": "1. Ish haqi → Indeksatsiya bo'limiga o'ting\n2. Kerakli davr uchun indeksatsiya hujjati yarating\n3. Agar indeksatsiya kerak bo'lmasa, hujjatni shunchaki yaratib tasdiqlang\n4. So'rovnomani qayta tasdiqlang",
        "hujjat_turi": "Naqd pul olish so'rovnomasi",
    },

    # --- HUJJAT RAQAMI XATOLARI ---
    "raqam_mavjud": {
        "pattern": "рақам.*мавжуд|номер.*существует|raqam.*mavjud",
        "shablon": "Bu hujjat raqami allaqachon mavjud",
        "sabab": "Kiritilgan hujjat raqami boshqa hujjatda ishlatilgan.",
        "yechim": "1. Hujjat raqami maydonini o'zgartiring\n2. Yangi (takrorlanmaydigan) raqam kiriting\n3. Yoki avtomatik raqamlash tugmasini bosing",
        "hujjat_turi": "Barcha hujjatlar",
    },

    # --- BIILLING XATOLARI ---
    "billing_tekshirilmagan": {
        "pattern": "биллинг тизими орқали текширилмаган",
        "shablon": "To'lov billing tizimi orqali tekshirilmagan",
        "sabab": "To'lov turini tanlagan bo'lsangiz-da, billing tizimi orqali tekshirish bajarilmagan.",
        "yechim": "1. Hujjatni oching\n2. To'lov turi maydonini tekshiring\n3. 'Billing tekshirish' tugmasini bosing\n4. Tekshirish muvaffaqiyatli bo'lganidan keyin hujjatni tasdiqlang",
        "hujjat_turi": "To'lov topshiriqnomasi, To'lov reyestri",
    },

    # --- TO'LOV TURI XATOLARI ---
    "tolov_turi_mavjud": {
        "pattern": "тўлов тури мавжуд|to'lov turi mavjud",
        "shablon": "Bu to'lov turi allaqachon mavjud",
        "sabab": "Bunday nomdagi to'lov turi tizimda allaqachon yaratilgan.",
        "yechim": "1. Mavjud to'lov turlarini tekshiring\n2. Boshqa nom bilan yarating yoki mavjudini ishlating",
        "hujjat_turi": "Ma'lumotnomalar",
    },
    "tolov_turi_topilmadi": {
        "pattern": "тўлов тури топилмади|to'lov turi topilmadi|клон.*тўлов тури",
        "shablon": "To'lov turi topilmadi",
        "sabab": "Hujjatda ko'rsatilgan to'lov turi tizimda mavjud emas yoki o'chirilgan.",
        "yechim": "1. To'lov turi maydonini tekshiring\n2. Ma'lumotnomalar → To'lov turlari dan kerakli turni tanlang\n3. Agar to'lov turi yo'q bo'lsa, administrator bilan bog'laning",
        "hujjat_turi": "Barcha moliyaviy hujjatlar",
    },
    "bir_martalik_tolov_taqiq": {
        "pattern": "бир марталик тўлов қисмидан киритиш мумкин эмас",
        "shablon": "Bu to'lov turini bir martalik to'lov qismidan kiritish mumkin emas",
        "sabab": "Tanlangan to'lov turi doimiy to'lov hisoblanadi va bir martalik to'lovlar qismidan kiritib bo'lmaydi.",
        "yechim": "1. Hujjatni oching\n2. To'lov turini doimiy to'lovlar qismida kiriting\n3. Yoki boshqa to'lov turini tanlang",
        "hujjat_turi": "Ish haqi hisobi",
    },

    # --- INPS XATOLARI ---
    "inps_topilmadi": {
        "pattern": "ИНПС.*реестри.*топилмади|INPS.*topilmadi",
        "shablon": "INPS reyestri hujjati topilmadi",
        "sabab": "Ko'rsatilgan summaga teng INPS reyestri hujjati tizimda mavjud emas.",
        "yechim": "1. Ish haqi → INPS reyestri bo'limiga o'ting\n2. Kerakli summa uchun INPS reyestri yarating\n3. Reyestrini tasdiqlang\n4. So'rovnomani qayta tasdiqlang",
        "hujjat_turi": "Naqd pul olish so'rovnomasi",
    },

    # --- ESKI TIZIM XATOLARI ---
    "eski_tizim": {
        "pattern": "eski tizimdan kelgan|эски тизимдан",
        "shablon": "Eski tizimdan kelgan hujjatlar holatini o'zgartirib bo'lmaydi",
        "sabab": "Bu hujjat eski tizimdan ko'chirilgan va holatini o'zgartirish mumkin emas.",
        "yechim": "1. Bu hujjatni tahrirlash mumkin emas\n2. Yangi hujjat yarating\n3. Agar muammo davom etsa, Call-center (71) 202-07-12 ga murojaat qiling",
        "hujjat_turi": "Barcha hujjatlar",
    },

    # --- HISOBOT XATOLARI ---
    "hisobot_davr_yopiq": {
        "pattern": "хисобот қабул қилиш тўхтатилган|хисобот қайтариш тўхтатилган|отчёт.*приостановлен",
        "shablon": "Bu davr uchun hisobot qabul qilish/qaytarish to'xtatilgan",
        "sabab": "Bu davr uchun hisobotlar qabul qilish muddati tugagan.",
        "yechim": "1. Boshqa davr uchun hisobot yuboring\n2. Agar shu davr uchun zarur bo'lsa, yuqori tashkilotga murojaat qiling\n3. Call-center (71) 202-07-12 ga qo'ng'iroq qiling",
        "hujjat_turi": "Elektron hisobotlar",
    },
    "balans_toldirilmagan": {
        "pattern": "баланс.*тўлдиринг|баланс.*заполните|balans.*provedeno",
        "shablon": "Hisobotni yuborishdan oldin balans to'ldirilishi kerak",
        "sabab": "Elektron hisobotni yuborishdan oldin balans hisobotini tuzib, tasdiqlash kerak.",
        "yechim": "1. Hisobotlar → Balans bo'limiga o'ting\n2. Shu davr uchun balans hisobotini to'ldiring\n3. Balansni 'Tasdiqlangan' holatga keltiring\n4. Keyin kerakli hisobotni yuborishga harakat qiling",
        "hujjat_turi": "Elektron hisobotlar",
    },

    # --- DUPLIKAT XATOLARI ---
    "duplikat_tolov_turi": {
        "pattern": "тўлов тури икки марта|to'lov turi ikki marta|дубликат",
        "shablon": "Bir sinfga to'lov turi ikki marta kiritish mumkin emas",
        "sabab": "Bitta sinf yoki guruhga bir xil to'lov turi allaqachon kiritilgan.",
        "yechim": "1. Hujjatdagi to'lov turlari ro'yxatini tekshiring\n2. Takrorlangan to'lov turini o'chiring\n3. Saqlang va qayta tasdiqlang",
        "hujjat_turi": "Tabel (ta'lim)",
    },

    # --- SHTATLAR XATOLARI ---
    "shtat_yoq": {
        "pattern": "штат.*топилмади|shtat.*topilmadi|ставка.*не найден",
        "shablon": "Xodim uchun shtat birligi topilmadi",
        "sabab": "Xodimga tegishli shtat birligi tizimda mavjud emas yoki faol emas.",
        "yechim": "1. Ish haqi → Shtatlar jadvali bo'limiga o'ting\n2. Kerakli bo'lim va lavozimni tekshiring\n3. Shtat birligini yarating yoki faollashtiring\n4. Hujjatni qayta tasdiqlang",
        "hujjat_turi": "Naqd pul olish so'rovnomasi, Oylik hisobi",
    },

    # --- SANA XATOLARI ---
    "sana_notogrri": {
        "pattern": "сана.*мос эмас|дата.*не соответствует|сана.*нотўғри|davr.*mos emas",
        "shablon": "Hujjat sanasi yoki davr noto'g'ri",
        "sabab": "Hujjat sanasi yoki davr boshqa hujjatlar bilan mos kelmaydi.",
        "yechim": "1. Hujjat sanasini tekshiring\n2. Davr (oy/yil) to'g'ri ekanligini tekshiring\n3. Kerakli davr uchun to'g'ri sanani tanlang\n4. Saqlang va qayta tasdiqlang",
        "hujjat_turi": "Barcha hujjatlar",
    },

    # --- TRANSLATE TEXT XATOLARI ---
    "translate_text": {
        "pattern": "GetTranslateText|100105|tarjima",
        "shablon": "Tizim xato xabari (tarjima kodi)",
        "sabab": "Tizimda ichki xato yuz berdi.",
        "yechim": "1. Sahifani yangilang (F5)\n2. Qayta urinib ko'ring\n3. Xato davom etsa, Call-center (71) 202-07-12 ga murojaat qiling",
        "hujjat_turi": "Barcha hujjatlar",
    },
}


class ErrorPatternParser:
    """
    Backend koddagi AddError larni analiz qilib,
    dinamik xatolarni shablon formatga aylantiradi.
    """

    def __init__(self, backend_path: str):
        self.backend_path = Path(backend_path)
        self.services_path = self.backend_path / "services"

    def parse_all(self) -> list:
        """
        Barcha .cs fayllardan AddError larni topib,
        shablon + yechim formatga aylantiradi.
        """
        all_errors = []

        if not self.services_path.exists():
            print(f"  Papka topilmadi: {self.services_path}")
            return all_errors

        for cs_file in self.services_path.rglob("*.cs"):
            try:
                errors = self._parse_file(cs_file)
                all_errors.extend(errors)
            except Exception as e:
                pass

        print(f"  Jami {len(all_errors)} ta AddError topildi")
        return all_errors

    def _parse_file(self, file_path: Path) -> list:
        """Bitta fayldan AddError larni topish."""
        errors = []
        try:
            try:
                content = file_path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                content = file_path.read_text(encoding="latin-1")

            lines = content.split("\n")
            service_name = self._extract_service_name(file_path)

            for i, line in enumerate(lines):
                # Comment qilinganlarni o'tkazish
                stripped = line.strip()
                if stripped.startswith("//"):
                    continue
                if "AddError(" not in line and "AddError (" not in line:
                    continue

                # Xato xabarini olish
                error_msg = self._extract_full_error(line, lines, i)
                if not error_msg:
                    continue

                # Metod nomini topish
                method_name = self._find_method_name(lines, i)

                # Fayldan class nomini olish
                class_name = self._extract_class_name(content)

                errors.append({
                    "raw_message": error_msg,
                    "line_number": i + 1,
                    "service_name": service_name,
                    "class_name": class_name,
                    "method_name": method_name,
                    "is_dynamic": "{" in error_msg or "+" in error_msg,
                    "file_path": str(file_path.relative_to(self.backend_path)).replace("\\", "/"),
                })

        except Exception:
            pass

        return errors

    def _extract_full_error(self, line: str, lines: list, idx: int) -> str:
        """AddError ichidagi to'liq matnni olish."""
        combined = line.strip()
        for j in range(1, 8):
            if idx + j < len(lines):
                next_line = lines[idx + j].strip()
                combined += " " + next_line
                if ");" in next_line or ")" in next_line:
                    break

        # $"..." formatdagi xabarlar (interpolatsiya bilan)
        match = re.search(r'AddError\s*\(\s*\$?"((?:[^"\\]|\\.)*)"\s*(?:\+[^)]+)?\)', combined)
        if match:
            return match.group(1)

        # Variable orqali
        match = re.search(r'AddError\s*\(\s*(\w+)\s*\)', combined)
        if match:
            return f"[variable:{match.group(1)}]"

        # Oddiy string + concatenation
        match = re.search(r'AddError\s*\(\s*"((?:[^"\\]|\\.)*)"', combined)
        if match:
            return match.group(1)

        return None

    def _find_method_name(self, lines: list, error_idx: int) -> str:
        """AddError joylashgan metod nomini topish."""
        for i in range(error_idx, max(0, error_idx - 100), -1):
            line = lines[i].strip()
            # async Task<...> MethodName( yoki public void MethodName(
            match = re.search(r'(?:async\s+)?(?:Task[<\w>]*\s+|void\s+|IActionResult\s+|[\w<>]+\s+)(\w+)\s*\(', line)
            if match and match.group(1) not in ("if", "for", "while", "foreach", "switch", "catch"):
                return match.group(1)
        return "unknown"

    def _extract_service_name(self, file_path: Path) -> str:
        """Fayl yo'lidan servis nomini aniqlash."""
        parts = file_path.parts
        for i, part in enumerate(parts):
            if part == "services" and i + 1 < len(parts):
                return parts[i + 1]
        return "unknown"

    def _extract_class_name(self, content: str) -> str:
        """Fayldan class nomini olish."""
        match = re.search(r'class\s+(\w+)', content)
        return match.group(1) if match else "Unknown"

    def match_solution(self, error_msg: str) -> dict:
        """
        Xato xabariga mos yechimni topish.
        ERROR_SOLUTIONS dagi pattern lar bilan solishtiriladi.
        """
        for key, solution in ERROR_SOLUTIONS.items():
            if re.search(solution["pattern"], error_msg, re.IGNORECASE):
                return {
                    "solution_key": key,
                    **solution,
                }
        return None


class ErrorPatternKnowledgeBase:
    """
    Xato shablonlarini knowledge_base ga saqlaydi.
    AI uchun tushunarli formatda — shablon, sabab, yechim.
    """

    def __init__(self, output_path: str):
        self.output_path = Path(output_path)
        (self.output_path / "error_solutions").mkdir(parents=True, exist_ok=True)

    def save_solutions(self, errors: list, parser: ErrorPatternParser):
        """
        Xatolarni tahlil qilib, yechimlar bilan birga saqlash.
        """
        # 1. Barcha xatolarni yechimlar bilan moslashtirish
        matched = []
        unmatched = []

        for error in errors:
            solution = parser.match_solution(error["raw_message"])
            if solution:
                matched.append({**error, "solution": solution})
            else:
                unmatched.append(error)

        # 2. Yechimlar ro'yxatini saqlash (AI uchun asosiy ma'lumot)
        self._save_solution_guide()

        # 3. Moslanmagan xatolarni servis bo'yicha saqlash
        self._save_unmatched_errors(unmatched)

        # 4. Statistika
        print(f"\n  Yechimli xatolar: {len(matched)} ta")
        print(f"  Yechim topilmagan: {len(unmatched)} ta")
        print(f"  Yechim shablonlari: {len(ERROR_SOLUTIONS)} ta")

    def _save_solution_guide(self):
        """
        AI uchun xato yechimlar qo'llanmasini Markdown formatda saqlash.
        Bu fayl AI ga eng ko'p yordam beradi.
        """
        md_content = "# UzASBO 2.0 — Xato Xabarlari va Yechimlar\n\n"
        md_content += "Bu qo'llanmada tizimda chiqishi mumkin bo'lgan xatolar va ularning yechimlari keltirilgan.\n"
        md_content += "Foydalanuvchi xato haqida so'raganda, shu qo'llanmadan mos yechimni toping.\n\n"
        md_content += "---\n\n"

        # Kategoriyalar bo'yicha guruhlash
        categories = {
            "To'lov va Hisobraqam xatolari": [
                "hisobraqam_kiritilmagan", "bank_topilmadi",
                "kontragent_hisobraqam_topilmadi",
            ],
            "Summa xatolari": [
                "summa_manfiy", "summa_mos_emas", "foiz_100_emas",
            ],
            "Xarajat kodi xatolari": [
                "xarajat_kodi_taqiqlangan", "statiya_ushlama_yoq",
            ],
            "To'lov turi xatolari": [
                "tolov_turi_mavjud", "tolov_turi_topilmadi",
                "bir_martalik_tolov_taqiq", "duplikat_tolov_turi",
            ],
            "Hujjat xatolari": [
                "raqam_mavjud", "eski_tizim", "sana_notogrri",
            ],
            "Ish haqi xatolari": [
                "indeksatsiya_yoq", "inps_topilmadi", "shtat_yoq",
            ],
            "Billing va Hisobot xatolari": [
                "billing_tekshirilmagan", "hisobot_davr_yopiq",
                "balans_toldirilmagan",
            ],
            "Tizim xatolari": [
                "translate_text",
            ],
        }

        for category_name, keys in categories.items():
            md_content += f"## {category_name}\n\n"

            for key in keys:
                if key not in ERROR_SOLUTIONS:
                    continue
                sol = ERROR_SOLUTIONS[key]

                md_content += f"### {sol['shablon']}\n\n"
                md_content += f"**Sabab:** {sol['sabab']}\n\n"
                md_content += f"**Yechim:**\n{sol['yechim']}\n\n"
                md_content += f"**Tegishli hujjatlar:** {sol['hujjat_turi']}\n\n"
                md_content += "---\n\n"

        # Faylga saqlash
        file_path = self.output_path / "error_solutions" / "error_solutions_guide.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"  Saqlandi: error_solutions_guide.md ({len(ERROR_SOLUTIONS)} ta yechim)")

        # JSON formatda ham saqlash (dasturiy ishlatish uchun)
        json_path = self.output_path / "error_solutions" / "error_solutions.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(ERROR_SOLUTIONS, f, ensure_ascii=False, indent=2)
        print(f"  Saqlandi: error_solutions.json")

    def _save_unmatched_errors(self, errors: list):
        """Yechim topilmagan xatolarni saqlash — keyinchalik yechim qo'shish uchun."""
        by_service = defaultdict(list)
        for error in errors:
            service = error.get("service_name", "unknown")
            by_service[service].append({
                "message": error["raw_message"],
                "class": error["class_name"],
                "method": error["method_name"],
                "line": error["line_number"],
                "is_dynamic": error["is_dynamic"],
            })

        file_path = self.output_path / "error_solutions" / "unmatched_errors.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(dict(by_service), f, ensure_ascii=False, indent=2)
        print(f"  Saqlandi: unmatched_errors.json ({len(errors)} ta)")


def main():
    parser = argparse.ArgumentParser(
        description="UzASBO2 xato shablonlarini parse qilish va yechimlar yaratish"
    )
    parser.add_argument(
        "--backend-path",
        default=str(Path(__file__).parent.parent.parent / "uzasbo2_backend"),
        help="uzasbo2_backend papkasi yo'li"
    )
    parser.add_argument(
        "--output-path",
        default=str(Path(__file__).parent.parent / "knowledge_base"),
        help="knowledge_base papkasi yo'li"
    )
    args = parser.parse_args()

    print("=" * 60)
    print("UzASBO 2.0 — Error Patterns Parser")
    print(f"Backend: {args.backend_path}")
    print(f"Output:  {args.output_path}")
    print("=" * 60)

    if not Path(args.backend_path).exists():
        print(f"\nBackend papka topilmadi: {args.backend_path}")
        return

    # 1. Xatolarni parse qilish
    print("\n1/2: AddError larni parsing qilish...")
    error_parser = ErrorPatternParser(args.backend_path)
    errors = error_parser.parse_all()

    # 2. Knowledge base yaratish
    print("\n2/2: Yechimlar bilan knowledge base yaratish...")
    kb = ErrorPatternKnowledgeBase(args.output_path)
    kb.save_solutions(errors, error_parser)

    print("\n" + "=" * 60)
    print("Tugadi!")
    print(f"\nKeyingi qadam:")
    print("  python scripts/load_knowledge_base.py --force")
    print("=" * 60)


if __name__ == "__main__":
    main()
