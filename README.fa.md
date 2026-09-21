<div align="center">

# ربات جنگ کشورها
# 🤖🌍⚔️

### ربات استراتژی فارسی برای روبیکا

یک ربات ناهمگام استراتژی ملی در روبیکا: بازیکن کشور می‌سازد، اقتصاد را رشد می‌دهد، اتحاد می‌بندد و در جدول رقابت می‌کند — با ذخیرهٔ پایدار JSON و رابط دکمه‌ای کامل.

<br>

# 👨‍💻 **صدرا حاتمی**

### *توسعه‌دهنده • مهندس نرم‌افزار • سازنده*

<br>

[🌐 پروفایل گیت‌هاب](https://github.com/sadra-hatami)
•
[📘 English README](README.md)
•
[📧 ایمیل](mailto:sadra.hatami.1732@gmail.com)

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Rubka](https://img.shields.io/badge/Rubka-Rubika%20Bot-8E44AD?style=for-the-badge)](https://pypi.org/)
[![AsyncIO](https://img.shields.io/badge/AsyncIO-Asynchronous-2C3E50?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/asyncio.html)
[![JSON](https://img.shields.io/badge/Storage-JSON-003B57?style=for-the-badge)](#-architecture)
[![Persian](https://img.shields.io/badge/Language-Persian-success?style=for-the-badge)](https://en.wikipedia.org/wiki/Persian_language)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
![GitHub](https://img.shields.io/badge/Open_Source-Project-black?style=for-the-badge&logo=github)

<br>

</div>

---

# 📖 درباره پروژه

**Countries War Bot** یک ربات استراتژی فارسی برای پلتفرم روبیکا است.

هر بازیکن یک کشور ثبت می‌کند، بعد منابع، رتبه، ساختمان، تحقیق و دیپلماسی را از طریق کیپد مدیریت می‌کند. پیشرفت روی دیسک می‌ماند تا کشور، اتحاد و رتبه بعد از ری‌استارت حفظ شود.

کد یک برنامهٔ ناهمگام است (`bot.py`) و با `rubka` نوشته شده. برای رزومه نشان می‌دهد که یک ربات پیام‌رسان می‌تواند حلقهٔ کامل بازی داشته باشد: وضعیت، منو، اقتصاد و رقابت چندنفره.

> **جمله کوتاه:** *ربات استراتژی روبیکا که در آن بازیکن یک کشور را اداره می‌کند، اقتصاد می‌سازد و با کشورهای دیگر رقابت می‌کند.*

---

# 🔗 مخازن مرتبط

| مخزن | نقش |
|------|------|
| **[Countries War Bot](https://github.com/sadra-hatami/Countries-War-Bot)** | بازی استراتژی ملی (همین مخزن) |
| **[Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot)** | ربات سبک قفل گروه |
| **[Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot)** | پلتفرم کامل مدیریت گروه |
| **[Telegram Rubika Account Panel](https://github.com/sadra-hatami/Telegram-Rubika-Account-Panel)** | پنل تلگرام برای حساب کاربری روبیکا |

ربات‌های گروه با `rubka` و توکن ربات کار می‌کنند. پنل حساب با تلگرام و `rubpy` است. این مخزن **ربات بازی** است، نه مدیر گروه.

---

# 🚀 چرا این پروژه؟

بیشتر ربات‌ها یک دستور جواب می‌دهند و تمام می‌شوند.

اینجا یک دنیای جاری می‌ماند:

- هر بازیکن کشور نام‌دار دارد
- اقتصاد و رتبه در زمان تغییر می‌کند
- بازیکنان با چالش، اتحاد و کلن به هم می‌رسند
- حلقهٔ روزانه مأموریت و پاداش را نو می‌کند
- اپراتور می‌تواند پایگاه بازیکنان را ببیند

---

# ✨ قابلیت‌ها

- 🏛️ ثبت کشور و پروفایل
- 💰 رشد منابع و رتبه
- 🛒 اقتصاد، فروشگاه و ارتقا
- 🏗️ ساختمان و تحقیق
- 🐾 همراهان قابل جمع‌آوری
- 🎖️ دستاورد
- 🤝 اتحاد و کلن
- ⚔️ چالش بین بازیکنان
- 📜 مأموریت روزانه و هفتگی
- 🏆 جدول برترین‌ها
- 🎛️ رابط فارسی مبتنی بر کیپد
- 💾 ذخیرهٔ JSON
- 🛡️ ابزار اپراتور برای نمونهٔ در حال اجرا

---

# 🏗️ معماری

```text
بازیکن
 └─ چت روبیکا + کیپد
     └─ bot.py
         └─ فایل ذخیره JSON
```

شناسه دکمه‌ها به سیستم‌های بازی می‌روند. رکورد بازیکن در JSON محلی است. تسک پس‌زمینه ریست روزانه را انجام می‌دهد. رمز و توکن باید در محیط باشند، نه داخل فایل.

---

# 📁 ساختار

```text
Countries-War-Bot/
├── bot.py
└── README.md
```

`bot.py` خود برنامه است. فایل JSON هنگام اجرا ساخته می‌شود و نباید به گیت برود.

---

# 🛠️ فناوری‌ها

- Python 3.8+
- `rubka`
- asyncio
- ذخیره JSON

---

# 🚀 نصب

```bash
git clone https://github.com/sadra-hatami/Countries-War-Bot.git
cd Countries-War-Bot
pip install rubka
python bot.py
```

---

# ⚙️ پیکربندی

توکن را در متغیر محیطی بگذار:

```text
RUBIKA_BOT_TOKEN
ADMIN_PASSWORD
```

در `.gitignore`:

```text
.env
*.json
__pycache__/
```

---

# ▶️ استفاده

1. توکن را در محیط بگذار.
2. `bot.py` را اجرا کن.
3. ربات را در روبیکا باز کن.
4. کشور بساز و از منوی دکمه‌ای استفاده کن.

---

# 🎓 مخاطب

- جامعه‌های روبیکا که بازی استراتژی طولانی می‌خواهند
- توسعه‌دهندگانی که ربات بزرگ کیپد محور می‌خوانند
- کسانی که نمونه کار بازی یا بک‌اند می‌سازند

---

# ❓ پرسش‌ها

### آیا این ربات قفل گروه است؟

نه. ابزار گروه در مخازن Group Bot و Advanced Group Bot است.

### آیا پیشرفت بعد از خاموش شدن می‌ماند؟

بله، اگر فایل JSON روی دیسک بماند.

### آیا توکن را در مخزن بگذارم؟

نه. فقط متغیر محیطی.

---

# 🔐 امنیت

توکن زنده و رمز ادمین را commit نکن. اگر قبلاً جایی پیست شده، عوضش کن. فایل ذخیره را هم عمومی نگذار.

---

# 📬 تماس

### صدرا حاتمی

📧 [ایمیل](mailto:sadra.hatami.1732@gmail.com)

🌐 [گیت‌هاب](https://github.com/sadra-hatami)

---

# 📄 مجوز

این پروژه تحت مجوز **MIT** است.

---

<div align="center">

## طراحی و توسعه با ❤️ برای جامعهٔ برنامه‌نویسان ایران و جهان توسط **صدرا حاتمی**

</div>
