"""
UzASBO 2.0 AI Assistant — Backend kod parser

Bu skript uzasbo2_backend kodini analiz qilib,
AI uchun knowledge base avtomatik yaratadi.

Nima qiladi:
    1. Barcha .cs fayllardan AddError xabarlarini topadi (6000+ ta)
    2. Controller fayllardan API endpoint larni ajratadi (550+ ta)
    3. i18n (RESX) fayllardan tarjima matnlarini o'qiydi
    4. Hammani JSON formatda knowledge_base/ papkaga saqlaydi

Ishga tushirish:
    python scripts/parse_backend.py

    yoki maxsus backend yo'l bilan:
    python scripts/parse_backend.py --backend-path D:/Projects/IVC/UZASBO/uzasbo2_backend
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict
import argparse


# ============================================================
# 1. AddError Parser
# Backend dagi barcha AddError xabarlarini topadi
# ============================================================

class AddErrorParser:
    """
    C# fayllardan AddError(...) chaqiruvlarini parsing qiladi.

    AddError — bu UzASBO backend da foydalanuvchiga xato ko'rsatish uchun
    ishlatiladigan metod. Masalan:
        if (dto.Amount <= 0)
            AddError("Summa 0 dan katta bo'lishi kerak");

    Parser quyidagilarni topadi:
        - Xato xabari matni
        - Qaysi fayl va qatorda
        - if sharti (agar bor bo'lsa)
        - Qaysi servis/hujjatga tegishli
    """

    def __init__(self, backend_path: str):
        """
        Args:
            backend_path: uzasbo2_backend papkasi yo'li
        """
        self.backend_path = Path(backend_path)
        # services/ papkasi — barcha mikroservislar shu yerda
        self.services_path = self.backend_path / "services"
        # libs/ papkasi — umumiy kutubxonalar
        self.libs_path = self.backend_path / "libs"

    def parse_all(self) -> list:
        """
        Barcha .cs fayllardan AddError larni topish.

        Returns:
            Xato xabarlari ro'yxati:
            [
                {
                    "error_message": "Summa 0 dan katta bo'lishi kerak",
                    "file_path": "finance-service/.../PaymentOrderService.cs",
                    "line_number": 45,
                    "condition": "dto.Amount <= 0",
                    "service_name": "finance-service",
                    "document_type": "paymentorder",
                    "class_name": "PaymentOrderService"
                },
                ...
            ]
        """
        all_errors = []

        # services/ papkasidagi barcha .cs fayllarni topish
        search_paths = [self.services_path, self.libs_path]

        for search_path in search_paths:
            if not search_path.exists():
                print(f"  ⚠ Papka topilmadi: {search_path}")
                continue

            # Rekursiv .cs fayllarni topish
            for cs_file in search_path.rglob("*.cs"):
                try:
                    errors = self._parse_file(cs_file)
                    all_errors.extend(errors)
                except Exception as e:
                    print(f"  ✗ Xato: {cs_file.name} — {e}")

        print(f"  ✓ Jami {len(all_errors)} ta AddError topildi")
        return all_errors

    def _parse_file(self, file_path: Path) -> list:
        """
        Bitta .cs fayldan AddError larni topish.

        C# da AddError quyidagi formatlarda bo'lishi mumkin:
            AddError("oddiy string");
            AddError($"interpolatsiya {variable}");
            AddError("qo'shish " + variable + " davomi");

        Args:
            file_path: .cs fayl yo'li

        Returns:
            Shu fayldagi xatolar ro'yxati
        """
        errors = []

        try:
            # Faylni o'qish (UTF-8 yoki Latin-1 kodlash)
            try:
                content = file_path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                content = file_path.read_text(encoding="latin-1")

            lines = content.split("\n")

            # Servis nomini fayl yo'lidan aniqlash
            # Masalan: services/finance-service/src/... → "finance-service"
            service_name = self._extract_service_name(file_path)

            # Hujjat turini fayl nomidan aniqlash
            # Masalan: PaymentOrderService.cs → "paymentorder"
            document_type = self._extract_document_type(file_path)

            # Klass nomini aniqlash
            class_name = self._extract_class_name(content)

            # Har bir qatorni tekshirish
            for i, line in enumerate(lines):
                # AddError ni qidirish
                if "AddError(" not in line and "AddError (" not in line:
                    continue

                # Xato xabar matnini ajratish
                error_message = self._extract_error_message(line, lines, i)
                if not error_message:
                    continue

                # if shartini topish (AddError dan yuqoridagi qatorlardan)
                condition = self._extract_condition(lines, i)

                # Fayl yo'lini qisqartirish (backend_path dan boshlab)
                try:
                    relative_path = str(file_path.relative_to(self.backend_path))
                except ValueError:
                    relative_path = str(file_path)

                errors.append({
                    "error_message": error_message,
                    "file_path": relative_path.replace("\\", "/"),
                    "line_number": i + 1,
                    "condition": condition,
                    "service_name": service_name,
                    "document_type": document_type,
                    "class_name": class_name,
                })

        except Exception as e:
            # Faylni o'qib bo'lmasa, o'tkazib yuboramiz
            pass

        return errors

    def _extract_error_message(self, line: str, lines: list, line_idx: int) -> str:
        """
        AddError(...) ichidagi xato xabar matnini ajratish.

        Turli formatlarni qo'llab-quvvatlaydi:
            AddError("oddiy matn")           → "oddiy matn"
            AddError($"matn {var}")           → "matn {var}"
            AddError("matn" + var)            → "matn..."
            AddError(\n  "ko'p qatorli")      → "ko'p qatorli"

        Args:
            line: AddError bo'lgan qator
            lines: Barcha qatorlar
            line_idx: Joriy qator indeksi

        Returns:
            Xato xabar matni yoki None
        """
        # Bir nechta qatorni birlashtirish (ko'p qatorli AddError uchun)
        combined = line.strip()
        # Agar qator ")" bilan tugamasa, keyingi qatorlarni qo'shish
        for j in range(1, 5):  # Maksimal 5 ta keyingi qator
            if line_idx + j < len(lines):
                next_line = lines[line_idx + j].strip()
                combined += " " + next_line
                if ")" in next_line:
                    break

        # Regex bilan xabar matnini topish
        # Pattern 1: AddError("...") yoki AddError($"...")
        match = re.search(r'AddError\s*\(\s*\$?"([^"]*)"', combined)
        if match:
            message = match.group(1)
            # Interpolatsiya belgilarini tozalash: {variable} → [...]
            message = re.sub(r'\{[^}]+\}', '[...]', message)
            return message.strip()

        # Pattern 2: AddError(variable) — o'zgaruvchi orqali
        match = re.search(r'AddError\s*\(\s*(\w+)\s*\)', combined)
        if match:
            return f"[dynamic: {match.group(1)}]"

        # Pattern 3: AddError("..." + ...) — qo'shish orqali
        match = re.search(r'AddError\s*\(\s*"([^"]*)"', combined)
        if match:
            return match.group(1).strip() + "..."

        return None

    def _extract_condition(self, lines: list, error_line_idx: int) -> str:
        """
        AddError dan oldingi if shartini topish.

        Misol:
            if (dto.Amount <= 0)        ← shu qatorni topamiz
            {
                AddError("Summa...");   ← AddError shu qatorda
            }

        Args:
            lines: Barcha qatorlar
            error_line_idx: AddError qatori indeksi

        Returns:
            if sharti matni yoki bo'sh string
        """
        # AddError dan yuqoriga 10 qatorgacha if ni qidirish
        for i in range(error_line_idx - 1, max(0, error_line_idx - 10), -1):
            line = lines[i].strip()

            # if (...) shaklini topish
            if line.startswith("if ") or line.startswith("if("):
                # if ichidagi shartni ajratish
                match = re.search(r'if\s*\((.+)\)', line)
                if match:
                    condition = match.group(1).strip()
                    # Juda uzun shartlarni qisqartirish
                    if len(condition) > 200:
                        condition = condition[:200] + "..."
                    return condition

            # Boshqa AddError yoki metod boshiga yetsa, to'xtatish
            if "AddError" in line or line.startswith("public ") or line.startswith("private "):
                break

        return ""

    def _extract_service_name(self, file_path: Path) -> str:
        """
        Fayl yo'lidan servis nomini aniqlash.
        Masalan: services/finance-service/src/... → "finance-service"
        """
        parts = file_path.parts
        for i, part in enumerate(parts):
            if part == "services" and i + 1 < len(parts):
                return parts[i + 1]
        return "unknown"

    def _extract_document_type(self, file_path: Path) -> str:
        """
        Fayl nomidan hujjat turini aniqlash.
        Masalan: PaymentOrderService.cs → "paymentorder"
                 ContractRepository.cs → "contract"
        """
        name = file_path.stem  # .cs ni olib tashlash
        # Service, Repository, Controller qo'shimchalarini olib tashlash
        for suffix in ["Service", "Repository", "Controller", "JobService",
                       "ReportService", "DlService", "BizService"]:
            name = name.replace(suffix, "")
        return name.lower().strip()

    def _extract_class_name(self, content: str) -> str:
        """
        C# fayldan klass nomini topish.
        Masalan: public class PaymentOrderService → "PaymentOrderService"
        """
        match = re.search(r'class\s+(\w+)', content)
        return match.group(1) if match else "Unknown"


# ============================================================
# 2. Controller Parser
# Backend dagi barcha API endpointlarni topadi
# ============================================================

class ControllerParser:
    """
    C# Controller fayllardan API endpoint ma'lumotlarini parsing qiladi.

    Har bir controller uchun topadi:
        - Route (URL yo'li)
        - HTTP metod (GET, POST, PUT, DELETE)
        - Permission kodi
        - Metod nomi va return turi
    """

    def __init__(self, backend_path: str):
        self.backend_path = Path(backend_path)
        self.services_path = self.backend_path / "services"

    def parse_all(self) -> list:
        """
        Barcha Controller fayllarni parsing qilish.

        Returns:
            Endpointlar ro'yxati:
            [
                {
                    "controller_name": "PaymentOrderController",
                    "route": "PaymentOrder/[action]",
                    "service_name": "finance-service",
                    "methods": [
                        {
                            "name": "GetListAsync",
                            "http_method": "POST",
                            "permission": "PaymentOrderView",
                            "return_type": "PagedResult<PaymentOrderListDto>"
                        }
                    ]
                },
                ...
            ]
        """
        all_controllers = []

        if not self.services_path.exists():
            print(f"  ⚠ Services papka topilmadi: {self.services_path}")
            return all_controllers

        # Controller fayllarni topish
        for cs_file in self.services_path.rglob("*Controller.cs"):
            # obj/ va bin/ papkalarni o'tkazib yuborish
            if "\\obj\\" in str(cs_file) or "/obj/" in str(cs_file):
                continue
            if "\\bin\\" in str(cs_file) or "/bin/" in str(cs_file):
                continue

            try:
                controller = self._parse_controller(cs_file)
                if controller:
                    all_controllers.append(controller)
            except Exception as e:
                print(f"  ✗ Xato: {cs_file.name} — {e}")

        print(f"  ✓ Jami {len(all_controllers)} ta Controller topildi")
        return all_controllers

    def _parse_controller(self, file_path: Path) -> dict:
        """
        Bitta Controller faylni parsing qilish.

        C# Controller formati:
            [Authorize]
            [ApiController]
            [Route("[controller]/[action]")]
            public class PaymentOrderController : WebaseController
            {
                [HttpPost]
                [Authorize(PermissionCode.PaymentOrderView)]
                public async Task<PagedResult<T>> GetListAsync(...)
            }
        """
        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = file_path.read_text(encoding="latin-1")

        # Klass nomini topish
        class_match = re.search(
            r'public\s+class\s+(\w+Controller)\s*:\s*(\w+)',
            content
        )
        if not class_match:
            return None

        controller_name = class_match.group(1)

        # Route ni topish — [Route("...")]
        route_match = re.search(r'\[Route\("([^"]+)"\)\]', content)
        route = route_match.group(1) if route_match else controller_name.replace("Controller", "")

        # Servis nomini aniqlash
        service_name = self._extract_service_name(file_path)

        # Metodlarni topish
        methods = self._parse_methods(content)

        return {
            "controller_name": controller_name,
            "route": route,
            "service_name": service_name,
            "methods": methods,
            "file_path": str(file_path.relative_to(self.backend_path)).replace("\\", "/"),
        }

    def _parse_methods(self, content: str) -> list:
        """
        Controller ichidagi barcha public metodlarni topish.

        Har bir metod uchun:
            - HTTP metod (GET, POST, PUT, DELETE)
            - Permission kodi
            - Metod nomi
            - UserAction (agar mavjud bo'lsa)
        """
        methods = []
        lines = content.split("\n")

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # HttpPost, HttpGet, HttpPut, HttpDelete ni qidirish
            http_match = re.search(r'\[Http(Post|Get|Put|Delete)', line)
            if http_match:
                http_method = http_match.group(1).upper()

                # Atrofidagi atributlarni yig'ish (yuqoriga va pastga)
                permission = ""
                user_action = ""

                # Yuqoriga va pastga 5 qatordan atributlar qidirish
                for j in range(max(0, i - 3), min(len(lines), i + 5)):
                    attr_line = lines[j].strip()

                    # Permission topish — [Authorize(PermissionCode.XXX)]
                    perm_match = re.search(
                        r'\[Authorize\(PermissionCode\.(\w+)\)\]',
                        attr_line
                    )
                    if perm_match:
                        permission = perm_match.group(1)

                    # UserAction topish — [UserAction("...")]
                    action_match = re.search(r'\[UserAction\("([^"]+)"\)\]', attr_line)
                    if action_match:
                        user_action = action_match.group(1)

                    # Public metod deklaratsiyasini topish
                    method_match = re.search(
                        r'public\s+async\s+Task<(.+?)>\s+(\w+)\s*\(',
                        attr_line
                    )
                    if not method_match:
                        method_match = re.search(
                            r'public\s+(?:async\s+)?(?:Task<)?(.+?)>?\s+(\w+)\s*\(',
                            attr_line
                        )

                    if method_match and "class " not in attr_line:
                        return_type = method_match.group(1)
                        method_name = method_match.group(2)

                        methods.append({
                            "name": method_name,
                            "http_method": http_method,
                            "permission": permission,
                            "return_type": return_type,
                            "user_action": user_action,
                        })
                        break

            i += 1

        return methods

    def _extract_service_name(self, file_path: Path) -> str:
        """Fayl yo'lidan servis nomini aniqlash."""
        parts = file_path.parts
        for i, part in enumerate(parts):
            if part == "services" and i + 1 < len(parts):
                return parts[i + 1]
        return "unknown"


# ============================================================
# 3. i18n (RESX) Parser
# Tarjima fayllardan matnlarni o'qiydi
# ============================================================

class I18nParser:
    """
    .resx (XML Resource) fayllardan tarjima matnlarini o'qiydi.

    RESX formati:
        <data name="100137" xml:space="preserve">
            <value>Xatolik Kodi 100137: Ma'lumot topilmadi</value>
        </data>
    """

    def __init__(self, backend_path: str):
        self.backend_path = Path(backend_path)

    def parse_all(self) -> dict:
        """
        Barcha .resx fayllarni o'qish.

        Returns:
            Til bo'yicha guruhlangan tarjimalar:
            {
                "uz_latn": {"100137": "Xatolik Kodi...", ...},
                "uz_cyrl": {"100137": "Хатолик Коди...", ...},
                "ru": {"100137": "Ошибка...", ...}
            }
        """
        translations = defaultdict(dict)

        # Barcha .resx fayllarni topish
        for resx_file in self.backend_path.rglob("*.resx"):
            # obj/ va bin/ papkalarni o'tkazib yuborish
            if "\\obj\\" in str(resx_file) or "\\bin\\" in str(resx_file):
                continue
            if "/obj/" in str(resx_file) or "/bin/" in str(resx_file):
                continue

            try:
                # Til nomini fayl nomidan aniqlash
                # Resource-uz-latn.resx → "uz_latn"
                lang = self._extract_language(resx_file)
                if not lang:
                    continue

                # RESX (XML) ni parsing qilish
                entries = self._parse_resx(resx_file)
                translations[lang].update(entries)

            except Exception as e:
                print(f"  ✗ RESX xato: {resx_file.name} — {e}")

        total = sum(len(v) for v in translations.values())
        print(f"  ✓ Jami {total} ta tarjima topildi ({len(translations)} til)")
        return dict(translations)

    def _parse_resx(self, file_path: Path) -> dict:
        """
        Bitta .resx faylni XML sifatida parsing qilish.

        Returns:
            {"kalit": "qiymat", ...}
        """
        entries = {}
        try:
            tree = ET.parse(str(file_path))
            root = tree.getroot()

            # <data> elementlarini topish
            for data_elem in root.findall("data"):
                name = data_elem.get("name", "")
                value_elem = data_elem.find("value")
                if value_elem is not None and value_elem.text:
                    entries[name] = value_elem.text.strip()

        except ET.ParseError as e:
            print(f"  ⚠ XML parse xato: {file_path.name}")

        return entries

    def _extract_language(self, file_path: Path) -> str:
        """
        Fayl nomidan tilni aniqlash.
        Resource-uz-latn.resx → "uz_latn"
        Resource-uz-cyrl.resx → "uz_cyrl"
        Resource-ru.resx → "ru"
        """
        name = file_path.stem.lower()  # .resx ni olib tashlash

        if "uz-latn" in name or "uz_latn" in name:
            return "uz_latn"
        elif "uz-cyrl" in name or "uz_cyrl" in name:
            return "uz_cyrl"
        elif "-ru" in name or "_ru" in name or name.endswith("ru"):
            return "ru"
        elif "-en" in name or "_en" in name:
            return "en"

        return None


# ============================================================
# 4. Knowledge Base Generator
# Parsing natijalarini knowledge_base/ ga saqlaydi
# ============================================================

class KnowledgeBaseGenerator:
    """
    Parser natijalarini AI uchun knowledge base formatiga aylantiradi
    va knowledge_base/ papkaga JSON/MD fayllar sifatida saqlaydi.
    """

    def __init__(self, output_path: str):
        """
        Args:
            output_path: knowledge_base/ papka yo'li
        """
        self.output_path = Path(output_path)
        # Papkalar mavjudligini ta'minlash
        (self.output_path / "errors").mkdir(parents=True, exist_ok=True)
        (self.output_path / "documents").mkdir(parents=True, exist_ok=True)
        (self.output_path / "navigation").mkdir(parents=True, exist_ok=True)

    def save_errors(self, errors: list):
        """
        AddError larni servis bo'yicha guruhlash va JSON ga saqlash.

        Har bir servis uchun alohida fayl yaratiladi:
            errors/finance-service_errors.json
            errors/hrm-service_errors.json
            ...
        """
        # Servis bo'yicha guruhlash
        by_service = defaultdict(list)
        for error in errors:
            service = error.get("service_name", "unknown")
            by_service[service].append(error)

        total_saved = 0
        for service_name, service_errors in by_service.items():
            # Fayl nomi: finance-service_errors.json
            file_name = f"{service_name}_errors.json"
            file_path = self.output_path / "errors" / file_name

            # JSON ga saqlash (chiroyli formatda)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(service_errors, f, ensure_ascii=False, indent=2)

            total_saved += len(service_errors)
            print(f"  💾 {file_name}: {len(service_errors)} ta xato")

        print(f"  ✅ Jami {total_saved} ta xato saqlandi")

    def save_controllers(self, controllers: list):
        """
        Controller ma'lumotlarini hujjat formatida saqlash.

        Har bir servis uchun API hujjat yaratiladi:
            documents/finance-service_api.md
            documents/hrm-service_api.md
        """
        # Servis bo'yicha guruhlash
        by_service = defaultdict(list)
        for ctrl in controllers:
            service = ctrl.get("service_name", "unknown")
            by_service[service].append(ctrl)

        for service_name, service_controllers in by_service.items():
            # Markdown hujjat yaratish
            md_content = self._generate_api_doc(service_name, service_controllers)

            file_name = f"{service_name}_api.md"
            file_path = self.output_path / "documents" / file_name

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(md_content)

            print(f"  💾 {file_name}: {len(service_controllers)} ta controller")

        # Controller larni navigation JSON ga ham saqlash
        nav_data = self._generate_navigation(controllers)
        nav_path = self.output_path / "navigation" / "api_endpoints.json"
        with open(nav_path, "w", encoding="utf-8") as f:
            json.dump(nav_data, f, ensure_ascii=False, indent=2)

        print(f"  ✅ Jami {len(controllers)} ta controller saqlandi")

    def save_translations(self, translations: dict):
        """
        Tarjimalarni JSON ga saqlash.
        AI xato xabarlarini tarjima qilish uchun ishlatadi.
        """
        file_path = self.output_path / "errors" / "translations.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(translations, f, ensure_ascii=False, indent=2)

        total = sum(len(v) for v in translations.values())
        print(f"  💾 translations.json: {total} ta tarjima")

    def _generate_api_doc(self, service_name: str, controllers: list) -> str:
        """
        Servis uchun API Markdown hujjat yaratish.

        Misol natija:
            # finance-service API
            ## PaymentOrderController
            Route: PaymentOrder/[action]
            ### GetListAsync [POST]
            Permission: PaymentOrderView
        """
        lines = [f"# {service_name} — API Endpointlar\n"]

        for ctrl in controllers:
            lines.append(f"\n## {ctrl['controller_name']}")
            lines.append(f"Route: `{ctrl['route']}`\n")

            for method in ctrl.get("methods", []):
                # Metod nomi va HTTP metodi
                lines.append(
                    f"### {method['name']} [{method['http_method']}]"
                )
                if method.get("permission"):
                    lines.append(f"- Permission: `{method['permission']}`")
                if method.get("return_type"):
                    lines.append(f"- Return: `{method['return_type']}`")
                if method.get("user_action"):
                    lines.append(f"- Tavsif: {method['user_action']}")
                lines.append("")

        return "\n".join(lines)

    def _generate_navigation(self, controllers: list) -> list:
        """
        Controller lardan navigatsiya JSON yaratish.
        AI "bu endpoint qayerda?" savollariga javob berish uchun.
        """
        nav_items = []
        for ctrl in controllers:
            route = ctrl.get("route", "")
            # [controller] va [action] ni haqiqiy nomlarga almashtirish
            controller_name = ctrl["controller_name"].replace("Controller", "")
            clean_route = route.replace("[controller]", controller_name)

            nav_items.append({
                "title": controller_name,
                "path": f"{ctrl['service_name']} → {controller_name}",
                "url": f"/{clean_route}",
                "description": f"{controller_name} API endpoint ({ctrl['service_name']})",
                "methods_count": len(ctrl.get("methods", [])),
            })

        return nav_items


# ============================================================
# MAIN — Asosiy ishga tushirish
# ============================================================

def main():
    """Asosiy funksiya — barcha parser larni ketma-ket ishga tushiradi."""

    # Argumentlarni o'qish
    parser = argparse.ArgumentParser(
        description="UzASBO2 Backend kodni parsing qilib knowledge base yaratish"
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

    backend_path = args.backend_path
    output_path = args.output_path

    print("=" * 60)
    print("UzASBO 2.0 — Backend Code Parser")
    print(f"Backend: {backend_path}")
    print(f"Output:  {output_path}")
    print("=" * 60)

    # Backend papka mavjudligini tekshirish
    if not Path(backend_path).exists():
        print(f"\n❌ Backend papka topilmadi: {backend_path}")
        print("--backend-path argumenti bilan to'g'ri yo'lni ko'rsating")
        return

    # Knowledge Base generator
    generator = KnowledgeBaseGenerator(output_path)

    # --- 1. AddError parsing ---
    print("\n📋 1/3: AddError larni parsing qilish...")
    error_parser = AddErrorParser(backend_path)
    errors = error_parser.parse_all()
    generator.save_errors(errors)

    # --- 2. Controller parsing ---
    print("\n📋 2/3: Controller larni parsing qilish...")
    ctrl_parser = ControllerParser(backend_path)
    controllers = ctrl_parser.parse_all()
    generator.save_controllers(controllers)

    # --- 3. i18n parsing ---
    print("\n📋 3/3: i18n (tarjima) fayllarni parsing qilish...")
    i18n_parser = I18nParser(backend_path)
    translations = i18n_parser.parse_all()
    generator.save_translations(translations)

    # Natija
    print("\n" + "=" * 60)
    print("✅ Backend parsing tugadi!")
    print(f"   AddError lar:   {len(errors)} ta")
    print(f"   Controller lar: {len(controllers)} ta")
    print(f"   Tarjimalar:     {sum(len(v) for v in translations.values())} ta")
    print(f"\nNatijalar: {output_path}")
    print("\nKeyingi qadam — ChromaDB ga yuklash:")
    print("   python scripts/load_knowledge_base.py --force")
    print("=" * 60)


if __name__ == "__main__":
    main()
