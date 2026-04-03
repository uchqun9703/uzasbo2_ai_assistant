# To'lov topshiriqnomasi — batafsil yo'riqnoma

## Umumiy ma'lumot

To'lov topshiriqnomasi — tashkilot hisobidan boshqa tashkilot yoki shaxsga pul o'tkazish uchun to'lov hujjati. G'aznachilik orqali to'lovlarni amalga oshirishda asosiy hujjat hisoblanadi.

API endpoint: /fin/PaymentOrder

### Uch tildagi nomi

| Til | Nomi |
|-----|------|
| O'zbek (lotin) | To'lov topshiriqnomasi |
| Ўзбек (кирилл) | Тўлов топшириқномаси |
| Русский | Платежное поручение |

## Qadamma-qadam yaratish

### 1-qadam: Sahifaga o'tish
Asosiy menyu → Moliya → To'lovlar → To'lov topshiriqnomasi

### 2-qadam: Yangi hujjat yaratish
"Yangi" ("+") tugmasini bosing. Yangi bo'sh shakl ochiladi.

### 3-qadam: Majburiy maydonlarni to'ldirish
- **To'lov turi** — ro'yxatdan to'lov turini tanlang (majburiy)
- **Hujjat raqami** — avtomatik yoki qo'lda raqam kiriting
- **Sana** — to'lov sanasi
- **Kontragent** — to'lov qabul qiluvchi tashkilot/shaxs
- **Summa** — to'lov summasi (so'mda)
- **Xarajat moddasi** — smeta bo'yicha xarajat moddasi

### 4-qadam: Saqlash
"Saqlash" tugmasini bosing. Hujjat "Yangi" holatda saqlanadi.

### 5-qadam: Tasdiqlash
Barcha ma'lumotlarni tekshirib, "Tasdiqlash" tugmasini bosing.

## Validatsiya qoidalari

Quyidagi hollarda xato chiqishi mumkin:
- To'lov turi ko'rsatilmagan — To'lov turini tanlash majburiy
- ShG'H topilmadi — Tashkilotning hisobraqami topilmadi
- Kassa subschyoti biriktirilmagan — ShG'H ga kassa subschyoti biriktirilmagan
- Hujjat raqami mavjud — Bu raqam bilan boshqa hujjat bor
- Tasdiqlash mumkin emas — Faqat yuborilgan hujjatni tasdiqlash mumkin

## Bog'liq hujjatlar

- **Shartnoma** — to'lov shartnomaga asoslangan bo'lishi mumkin
- **Smeta** — xarajat moddasi smeta bilan bog'liq
- **So'rovnoma** — naqd pul olish uchun so'rovnomaga bog'lanadi
- **O'tkazmalar** — buxgalteriya provodkasi avtomatik yaratiladi

## Ko'p uchraydigan muammolar

### Muammo: "ShG'H topilmadi" xatosi
**Sabab:** Tashkilotga Shaxsiy G'azna Hisobraqami biriktirilmagan.
**Yechim:** Administrator bilan bog'lanib, ShG'H ni tekshiring.

### Muammo: Tasdiqlash tugmasi ishlamayapti
**Sabab:** Hujjat to'g'ri holatda emas yoki majburiy maydonlar to'ldirilmagan.
**Yechim:** Barcha maydonlarni tekshiring va avval "Saqlash" tugmasini bosing.
