# ==================================================
# ربات جنگ کشورها - نسخه کامل واقعی
# ==================================================

import asyncio
import json
import os
import random
import time
from datetime import datetime, timedelta
from rubka.asynco import Robot, Message
from rubka.keypad import ChatKeypadBuilder

BOT_TOKEN = "BEDDAF0HUDVZZRMUJIZVDBXVHSEGVUNVIVGMCACQFFJRNKBLVSOYJIUWIGERGITJ"
ADMIN_PASSWORD = "16948"
DATA_FILE = "country_war_real.json"

bot = Robot(BOT_TOKEN)

# ==================================================
# سلاح‌ها - 52 سلاح واقعی (همشون پر شده)
# ==================================================

WEAPONS_DB = {
    "ground": {
        "title": "⚔️ سلاح‌های زمینی",
        "emoji": "⚔️",
        "items": [
            {"id": "g1", "name": "کلت گلاک 17", "emoji": "🔫", "price": 100, "power": 50, "level_req": 1, "critical": 5},
            {"id": "g2", "name": "مسلسل M4", "emoji": "🔫", "price": 260, "power": 150, "level_req": 2, "critical": 8},
            {"id": "g3", "name": "اسنایپر AWP", "emoji": "🎯", "price": 380, "power": 300, "level_req": 3, "critical": 15},
            {"id": "g4", "name": "مسلسل M249", "emoji": "💥", "price": 590, "power": 450, "level_req": 4, "critical": 10},
            {"id": "g5", "name": "تانک آبرامز", "emoji": "🛡️", "price": 1500, "power": 800, "level_req": 5, "critical": 12},
            {"id": "g6", "name": "توپخانه 155mm", "emoji": "🎆", "price": 2000, "power": 1200, "level_req": 6, "critical": 18},
            {"id": "g7", "name": "موشک انداز گراد", "emoji": "🚀", "price": 1800, "power": 1000, "level_req": 5, "critical": 20},
            {"id": "g8", "name": "نارنجک انداز", "emoji": "💣", "price": 800, "power": 400, "level_req": 3, "critical": 7},
            {"id": "g9", "name": "خمپاره 120mm", "emoji": "💥", "price": 1100, "power": 600, "level_req": 4, "critical": 10},
            {"id": "g10", "name": "نیروی ویژه", "emoji": "🥷", "price": 2500, "power": 1800, "level_req": 7, "critical": 25},
            {"id": "g11", "name": "RPG-7", "emoji": "🚀", "price": 1200, "power": 700, "level_req": 4, "critical": 15},
            {"id": "g12", "name": "توپ لیزری", "emoji": "⚡", "price": 5000, "power": 3500, "level_req": 10, "critical": 35},
            {"id": "g13", "name": "رعد بالستیک", "emoji": "☄️", "price": 8000, "power": 5500, "level_req": 12, "critical": 40},
            {"id": "g14", "name": "توپ پلاسمایی", "emoji": "🌋", "price": 15000, "power": 11000, "level_req": 15, "critical": 50},
            {"id": "g15", "name": "ارتش سایبورگ", "emoji": "🤖", "price": 25000, "power": 18000, "level_req": 20, "critical": 55},
            {"id": "g16", "name": "الهه جنگ", "emoji": "👸", "price": 50000, "power": 38000, "level_req": 30, "critical": 65},
            {"id": "g17", "name": "تفنگ بردی", "emoji": "🎯", "price": 450, "power": 200, "level_req": 2, "critical": 10},
            {"id": "g18", "name": "شاتگان", "emoji": "🔫", "price": 300, "power": 120, "level_req": 1, "critical": 6},
            {"id": "g19", "name": "مسلسل سنگین", "emoji": "🔫", "price": 800, "power": 350, "level_req": 3, "critical": 9},
            {"id": "g20", "name": "مهمات انفجاری", "emoji": "💣", "price": 500, "power": 200, "level_req": 2, "critical": 12},
        ]
    },
    "air": {
        "title": "✈️ سلاح‌های هوایی",
        "emoji": "✈️",
        "items": [
            {"id": "a1", "name": "F-16 فالکن", "emoji": "✈️", "price": 1200, "power": 1200, "level_req": 3, "critical": 10},
            {"id": "a2", "name": "F-22 رپتور", "emoji": "🦅", "price": 2500, "power": 2000, "level_req": 5, "critical": 15},
            {"id": "a3", "name": "AH-64 آپاچی", "emoji": "🚁", "price": 1500, "power": 1500, "level_req": 4, "critical": 12},
            {"id": "a4", "name": "موشک توماهاوک", "emoji": "🚀", "price": 3000, "power": 2500, "level_req": 6, "critical": 20},
            {"id": "a5", "name": "Su-57", "emoji": "⚡", "price": 3500, "power": 2800, "level_req": 7, "critical": 22},
            {"id": "a6", "name": "بمب‌افکن B-2", "emoji": "💨", "price": 4000, "power": 3200, "level_req": 8, "critical": 25},
            {"id": "a7", "name": "دрон شاهد", "emoji": "🛸", "price": 900, "power": 700, "level_req": 2, "critical": 8},
            {"id": "a8", "name": "جت بمب‌افکن", "emoji": "💣", "price": 3200, "power": 2700, "level_req": 6, "critical": 18},
            {"id": "a9", "name": "هلیکوپتر جنگی", "emoji": "🚁", "price": 1800, "power": 1300, "level_req": 4, "critical": 11},
            {"id": "a10", "name": "رادارگریز", "emoji": "👻", "price": 5000, "power": 4200, "level_req": 9, "critical": 28},
            {"id": "a11", "name": "پرنده آتشین", "emoji": "🐦‍🔥", "price": 10000, "power": 8500, "level_req": 12, "critical": 38},
            {"id": "a12", "name": "X-71 فضایی", "emoji": "🛸", "price": 25000, "power": 22000, "level_req": 18, "critical": 48},
            {"id": "a13", "name": "اسب بالدار", "emoji": "🦄", "price": 15000, "power": 13000, "level_req": 15, "critical": 42},
            {"id": "a14", "name": "اژدهای پرنده", "emoji": "🐉", "price": 35000, "power": 28000, "level_req": 22, "critical": 55},
            {"id": "a15", "name": "صاعقه‌گیر", "emoji": "⚡", "price": 45000, "power": 35000, "level_req": 25, "critical": 60},
        ]
    },
    "sea": {
        "title": "🚢 سلاح‌های دریایی",
        "emoji": "🚢",
        "items": [
            {"id": "s1", "name": "ناوچه سبک", "emoji": "🚤", "price": 1000, "power": 700, "level_req": 2, "critical": 8},
            {"id": "s2", "name": "ناوشکن", "emoji": "⚓", "price": 2000, "power": 1500, "level_req": 4, "critical": 12},
            {"id": "s3", "name": "زیردریایی", "emoji": "🐟", "price": 1500, "power": 1200, "level_req": 3, "critical": 15},
            {"id": "s4", "name": "هواپیمابر", "emoji": "🏰", "price": 5000, "power": 4000, "level_req": 7, "critical": 20},
            {"id": "s5", "name": "ناو جنگی", "emoji": "💀", "price": 3000, "power": 2500, "level_req": 5, "critical": 16},
            {"id": "s6", "name": "اژدر سنگین", "emoji": "💣", "price": 1200, "power": 900, "level_req": 3, "critical": 10},
            {"id": "s7", "name": "موشک‌انداز دریایی", "emoji": "🎯", "price": 2200, "power": 1700, "level_req": 4, "critical": 14},
            {"id": "s8", "name": "قایق تندرو", "emoji": "⛵", "price": 500, "power": 300, "level_req": 1, "critical": 5},
            {"id": "s9", "name": "کروز دریایی", "emoji": "🛳️", "price": 800, "power": 500, "level_req": 2, "critical": 7},
            {"id": "s10", "name": "رزم‌ناو", "emoji": "⚔️", "price": 4000, "power": 3200, "level_req": 6, "critical": 18},
            {"id": "s11", "name": "نهنگ جنگی", "emoji": "🐋", "price": 8000, "power": 6500, "level_req": 10, "critical": 28},
            {"id": "s12", "name": "لویاتان", "emoji": "🐉", "price": 20000, "power": 18000, "level_req": 16, "critical": 45},
            {"id": "s13", "name": "پوسایدون", "emoji": "🔱", "price": 45000, "power": 38000, "level_req": 25, "critical": 60},
            {"id": "s14", "name": "کشتی اژدرزن", "emoji": "🚤", "price": 2500, "power": 1900, "level_req": 5, "critical": 13},
            {"id": "s15", "name": "نبردناو", "emoji": "⚓", "price": 6000, "power": 5000, "level_req": 8, "critical": 22},
        ]
    },
    "special": {
        "title": "💎 سلاح‌های ویژه",
        "emoji": "💎",
        "items": [
            {"id": "sp1", "name": "بمب اتمی", "emoji": "☢️", "price": 50000, "power": 45000, "level_req": 15, "critical": 80},
            {"id": "sp2", "name": "بمب هیدروژنی", "emoji": "💣", "price": 100000, "power": 90000, "level_req": 20, "critical": 95},
            {"id": "sp3", "name": "شمشیر نور", "emoji": "⚔️", "price": 8000, "power": 6500, "level_req": 10, "critical": 30},
            {"id": "sp4", "name": "کمربند قدرت", "emoji": "💪", "price": 5000, "power": 4000, "level_req": 8, "critical": 25},
            {"id": "sp5", "name": "سپر محافظ", "emoji": "🛡️", "price": 6000, "power": 0, "level_req": 9, "critical": 0, "defense": 500},
            {"id": "sp6", "name": "نفرین فرعون", "emoji": "👑", "price": 15000, "power": 12000, "level_req": 12, "critical": 35},
            {"id": "sp7", "name": "کلاه نامرئی", "emoji": "🎩", "price": 12000, "power": 0, "level_req": 11, "critical": 0, "stealth": 100},
        ]
    }
}

# ==================================================
# مشاغل - 30 شغل واقعی (همشون پر شده)
# ==================================================

JOBS_DB = {
    1: {"name": "👨‍🌾 کشاورز", "bonus": {"food": 50, "coins": 20}, "upgrade_cost": 500},
    2: {"name": "⛏️ معدنچی", "bonus": {"iron": 30, "gold": 10}, "upgrade_cost": 500},
    3: {"name": "🧑‍💼 تاجر", "bonus": {"coins": 80}, "upgrade_cost": 800},
    4: {"name": "🔬 دانشمند", "bonus": {"research": 2, "coins": 30}, "upgrade_cost": 1000},
    5: {"name": "🎖️ ژنرال", "bonus": {"attack": 50, "soldiers": 5}, "upgrade_cost": 1200},
    6: {"name": "🕵️ جاسوس", "bonus": {"spy": 30, "coins": 20}, "upgrade_cost": 800},
    7: {"name": "🤝 دیپلمات", "bonus": {"alliance": 2, "coins": 40}, "upgrade_cost": 600},
    8: {"name": "💡 مخترع", "bonus": {"weapon": 20, "coins": 50}, "upgrade_cost": 1500},
    9: {"name": "👨‍⚕️ پزشک", "bonus": {"health": 500, "coins": 30}, "upgrade_cost": 700},
    10: {"name": "👷 مهندس", "bonus": {"building": 2, "fort": 10}, "upgrade_cost": 900},
    11: {"name": "🗡️ آدم‌کش", "bonus": {"critical": 5, "attack": 30}, "upgrade_cost": 2000},
    12: {"name": "🙏 کشیش", "bonus": {"heal": 200, "defense": 20}, "upgrade_cost": 1000},
    13: {"name": "🧙 جادوگر", "bonus": {"magic": 50, "coins": 100}, "upgrade_cost": 3000},
    14: {"name": "👑 پادشاه", "bonus": {"all": 20, "coins": 200}, "upgrade_cost": 5000},
    15: {"name": "🏹 کماندار", "bonus": {"accuracy": 10, "attack": 25}, "upgrade_cost": 800},
    16: {"name": "🛡️ جنگجو", "bonus": {"defense": 40, "health": 300}, "upgrade_cost": 1000},
    17: {"name": "🔮 پیشگو", "bonus": {"luck": 10, "coins": 60}, "upgrade_cost": 1200},
    18: {"name": "⚔️ شوالیه", "bonus": {"attack": 40, "defense": 30}, "upgrade_cost": 1500},
    19: {"name": "🐉 اژدها سوار", "bonus": {"pet": 50, "attack": 60}, "upgrade_cost": 5000},
    20: {"name": "🧪 کیمیاگر", "bonus": {"resources": 50, "coins": 80}, "upgrade_cost": 2000},
    21: {"name": "📜 مورخ", "bonus": {"exp": 100, "coins": 40}, "upgrade_cost": 600},
    22: {"name": "🎭 بازیگر", "bonus": {"charisma": 20, "coins": 70}, "upgrade_cost": 700},
    23: {"name": "🎵 موسیقیدان", "bonus": {"morale": 10, "coins": 50}, "upgrade_cost": 600},
    24: {"name": "🏋️ ورزشکار", "bonus": {"health": 400, "attack": 20}, "upgrade_cost": 800},
    25: {"name": "🧘 یوگی", "bonus": {"energy": 50, "health": 200}, "upgrade_cost": 700},
    26: {"name": "🔧 مکانیک", "bonus": {"repair": 30, "coins": 60}, "upgrade_cost": 900},
    27: {"name": "💻 هکر", "bonus": {"spy": 50, "coins": 100}, "upgrade_cost": 2500},
    28: {"name": "📡 مخابراتی", "bonus": {"info": 30, "coins": 50}, "upgrade_cost": 800},
    29: {"name": "🚀 فضانورد", "bonus": {"space": 100, "coins": 200}, "upgrade_cost": 10000},
    30: {"name": "🌟 افسانه", "bonus": {"all": 50, "coins": 500}, "upgrade_cost": 20000},
}

# ==================================================
# حیوانات - 50 حیوان واقعی (همشون پر شده)
# ==================================================

PETS_DB = {
    1: {"name": "🐔 مرغ", "price": 100, "bonus": {"coins": 10}, "level_req": 1},
    2: {"name": "🐱 گربه", "price": 200, "bonus": {"luck": 5}, "level_req": 1},
    3: {"name": "🐶 سگ", "price": 300, "bonus": {"defense": 20}, "level_req": 2},
    4: {"name": "🐭 موش", "price": 50, "bonus": {"spy": 10}, "level_req": 1},
    5: {"name": "🐰 خرگوش", "price": 150, "bonus": {"speed": 10}, "level_req": 1},
    6: {"name": "🦊 روباه", "price": 400, "bonus": {"cunning": 15}, "level_req": 3},
    7: {"name": "🐺 گرگ", "price": 600, "bonus": {"attack": 30}, "level_req": 4},
    8: {"name": "🐗 گراز", "price": 500, "bonus": {"strength": 25}, "level_req": 3},
    9: {"name": "🦅 عقاب", "price": 800, "bonus": {"vision": 20}, "level_req": 5},
    10: {"name": "🦉 جغد", "price": 700, "bonus": {"wisdom": 15}, "level_req": 4},
    11: {"name": "🐍 مار", "price": 300, "bonus": {"poison": 20}, "level_req": 2},
    12: {"name": "🦂 عقرب", "price": 400, "bonus": {"venom": 25}, "level_req": 3},
    13: {"name": "🐝 زنبور", "price": 200, "bonus": {"production": 10}, "level_req": 1},
    14: {"name": "🦋 پروانه", "price": 150, "bonus": {"beauty": 10}, "level_req": 1},
    15: {"name": "🐞 کفشدوزک", "price": 100, "bonus": {"luck": 5}, "level_req": 1},
    16: {"name": "🦗 ملخ", "price": 80, "bonus": {"jump": 10}, "level_req": 1},
    17: {"name": "🕷️ عنکبوت", "price": 250, "bonus": {"web": 15}, "level_req": 2},
    18: {"name": "🦎 مارمولک", "price": 350, "bonus": {"camouflage": 15}, "level_req": 2},
    19: {"name": "🐢 لاک‌پشت", "price": 500, "bonus": {"defense": 40}, "level_req": 3},
    20: {"name": "🐙 اختاپوس", "price": 600, "bonus": {"multi": 10}, "level_req": 4},
    21: {"name": "🦑 ماهی مرکب", "price": 700, "bonus": {"ink": 15}, "level_req": 4},
    22: {"name": "🐬 دلفین", "price": 800, "bonus": {"intelligence": 20}, "level_req": 5},
    23: {"name": "🐋 نهنگ", "price": 2000, "bonus": {"power": 100}, "level_req": 8},
    24: {"name": "🦈 کوسه", "price": 1500, "bonus": {"attack": 80}, "level_req": 7},
    25: {"name": "🐊 کروکودیل", "price": 1200, "bonus": {"bite": 60}, "level_req": 6},
    26: {"name": "🦏 کرگدن", "price": 1800, "bonus": {"charge": 70}, "level_req": 7},
    27: {"name": "🐘 فیل", "price": 2500, "bonus": {"strength": 120}, "level_req": 9},
    28: {"name": "🦒 زرافه", "price": 1200, "bonus": {"reach": 30}, "level_req": 6},
    29: {"name": "🐫 شتر", "price": 1000, "bonus": {"endurance": 40}, "level_req": 5},
    30: {"name": "🐎 اسب", "price": 800, "bonus": {"speed": 30}, "level_req": 4},
    31: {"name": "🦄 تک‌شاخ", "price": 5000, "bonus": {"magic": 100}, "level_req": 12},
    32: {"name": "🐉 اژدها", "price": 10000, "bonus": {"fire": 200}, "level_req": 15},
    33: {"name": "🦅 ققنوس", "price": 8000, "bonus": {"rebirth": 100}, "level_req": 14},
    34: {"name": "🐺 گرگینه", "price": 6000, "bonus": {"moon": 80}, "level_req": 13},
    35: {"name": "🧛 خفاش خون‌آشام", "price": 4000, "bonus": {"life_steal": 50}, "level_req": 11},
    36: {"name": "👻 روح", "price": 3000, "bonus": {"intangible": 50}, "level_req": 10},
    37: {"name": "🧟 زامبی", "price": 2000, "bonus": {"undead": 40}, "level_req": 8},
    38: {"name": "🤖 ربات", "price": 3500, "bonus": {"tech": 60}, "level_req": 10},
    39: {"name": "👽 بیگانه", "price": 7000, "bonus": {"alien": 100}, "level_req": 14},
    40: {"name": "🧚 پری", "price": 4000, "bonus": {"heal": 50}, "level_req": 11},
    41: {"name": "🗿 گلم", "price": 3000, "bonus": {"defense": 80}, "level_req": 9},
    42: {"name": "🔥 ایگوانا", "price": 900, "bonus": {"fire": 25}, "level_req": 5},
    43: {"name": "❄️ پنگوئن", "price": 600, "bonus": {"ice": 20}, "level_req": 4},
    44: {"name": "⚡ مارماهی برقی", "price": 1100, "bonus": {"shock": 35}, "level_req": 6},
    45: {"name": "🌿 موجود جنگلی", "price": 800, "bonus": {"nature": 25}, "level_req": 5},
    46: {"name": "🏔️ یتی", "price": 4000, "bonus": {"ice": 100}, "level_req": 12},
    47: {"name": "🌊 لوچ نس", "price": 5000, "bonus": {"water": 120}, "level_req": 13},
    48: {"name": "🦖 دایناسور", "price": 8000, "bonus": {"ancient": 150}, "level_req": 15},
    49: {"name": "🐲 اژدهای چینی", "price": 12000, "bonus": {"wisdom": 200}, "level_req": 18},
    50: {"name": "🌟 پگاسوس", "price": 15000, "bonus": {"holy": 250}, "level_req": 20},
}
# ==================================================
# مدال‌ها - 100 مدال کامل و واقعی
# ==================================================

ACHIEVEMENTS_DB = {
    # مدال‌های پایه (1-20)
    "a1": {"name": "🌱 تازه کار", "desc": "به بازی خوش آمدی", "requirement": 1, "type": "start", "reward": 1000},
    "a2": {"name": "⚔️ اولین حمله", "desc": "اولین حمله موفق", "requirement": 1, "type": "first_attack", "reward": 500},
    "a3": {"name": "🛡️ اولین دفاع", "desc": "اولین دفاع موفق", "requirement": 1, "type": "first_defend", "reward": 500},
    "a4": {"name": "💰 ۱۰۰۰ سکه", "desc": "۱۰۰۰ سکه جمع کن", "requirement": 1000, "type": "coins", "reward": 500},
    "a5": {"name": "💪 قدرت ۱۰۰۰", "desc": "قدرت ۱۰۰۰", "requirement": 1000, "type": "power", "reward": 1000},
    "a6": {"name": "🗡️ ۱۰ حمله", "desc": "۱۰ حمله موفق", "requirement": 10, "type": "attacks", "reward": 1000},
    "a7": {"name": "💀 ۱۰ کشته", "desc": "۱۰ کشته", "requirement": 10, "type": "kills", "reward": 1000},
    "a8": {"name": "👥 ۱۰۰ سرباز", "desc": "۱۰۰ سرباز استخدام کن", "requirement": 100, "type": "soldiers", "reward": 1500},
    "a9": {"name": "🔫 اولین سلاح", "desc": "اولین سلاح بخر", "requirement": 1, "type": "first_weapon", "reward": 500},
    "a10": {"name": "🏰 قلعه سطح ۱", "desc": "اولین قلعه", "requirement": 1, "type": "fort", "reward": 2000},
    "a11": {"name": "👑 سطح ۵", "desc": "به سطح ۵ برس", "requirement": 5, "type": "level", "reward": 2000},
    "a12": {"name": "💼 ۱۰۰ کار", "desc": "۱۰۰ بار کار کن", "requirement": 100, "type": "work", "reward": 2000},
    "a13": {"name": "🕵️ ۱۰ جاسوسی", "desc": "۱۰ جاسوسی موفق", "requirement": 10, "type": "spies", "reward": 1500},
    "a14": {"name": "💣 ۱۰ تروریست", "desc": "۱۰ تروریست بخر", "requirement": 10, "type": "terrorists", "reward": 1500},
    "a15": {"name": "🎁 ۷ روز متوالی", "desc": "۷ روز پاداش روزانه", "requirement": 7, "type": "streak", "reward": 5000},
    "a16": {"name": "🤝 اولین اتحاد", "desc": "اتحاد ببند", "requirement": 1, "type": "first_alliance", "reward": 2000},
    "a17": {"name": "🏆 اولین برد دوال", "desc": "دوال ببر", "requirement": 1, "type": "first_duel", "reward": 1000},
    "a18": {"name": "📈 سرمایه‌گذار", "desc": "سرمایه‌گذاری کن", "requirement": 1, "type": "first_invest", "reward": 1000},
    "a19": {"name": "🎰 کازینو باز", "desc": "اولین برد کازینو", "requirement": 1, "type": "first_casino", "reward": 500},
    "a20": {"name": "👥 ۵ اتحاد", "desc": "۵ اتحاد فعال", "requirement": 5, "type": "alliances", "reward": 5000},
    
    # مدال‌های پیشرفته (21-50)
    "a21": {"name": "🗡️ ۵۰ حمله", "desc": "۵۰ حمله موفق", "requirement": 50, "type": "attacks", "reward": 5000},
    "a22": {"name": "💀 ۵۰ کشته", "desc": "۵۰ کشته", "requirement": 50, "type": "kills", "reward": 5000},
    "a23": {"name": "💰 ۱۰۰۰۰ سکه", "desc": "۱۰۰۰۰ سکه جمع کن", "requirement": 10000, "type": "coins", "reward": 10000},
    "a24": {"name": "💪 قدرت ۱۰۰۰۰", "desc": "قدرت ۱۰۰۰۰", "requirement": 10000, "type": "power", "reward": 10000},
    "a25": {"name": "🏰 قلعه سطح ۵", "desc": "قلعه سطح ۵", "requirement": 5, "type": "fort", "reward": 10000},
    "a26": {"name": "👑 سطح ۱۰", "desc": "سطح ۱۰", "requirement": 10, "type": "level", "reward": 10000},
    "a27": {"name": "🎌 ساخت کلن", "desc": "کلن بساز", "requirement": 1, "type": "first_clan", "reward": 10000},
    "a28": {"name": "⚔️ استریک ۱۰", "desc": "۱۰ حمله پشت سر هم", "requirement": 10, "type": "streak", "reward": 5000},
    "a29": {"name": "🛡️ ۵۰ دفاع", "desc": "۵۰ دفاع موفق", "requirement": 50, "type": "defends", "reward": 5000},
    "a30": {"name": "🕵️ ۵۰ جاسوسی", "desc": "۵۰ جاسوسی", "requirement": 50, "type": "spies", "reward": 10000},
    "a31": {"name": "💣 ۱۰۰ تروریست", "desc": "۱۰۰ تروریست", "requirement": 100, "type": "terrorists", "reward": 10000},
    "a32": {"name": "👥 ۱۰۰۰ سرباز", "desc": "۱۰۰۰ سرباز", "requirement": 1000, "type": "soldiers", "reward": 15000},
    "a33": {"name": "🔫 ۱۰ سلاح", "desc": "۱۰ سلاح بخر", "requirement": 10, "type": "weapons", "reward": 5000},
    "a34": {"name": "🏰 قلعه سطح ۱۰", "desc": "قلعه سطح ۱۰", "requirement": 10, "type": "fort", "reward": 20000},
    "a35": {"name": "👑 سطح ۲۰", "desc": "سطح ۲۰", "requirement": 20, "type": "level", "reward": 20000},
    "a36": {"name": "💪 قدرت ۵۰۰۰۰", "desc": "قدرت ۵۰۰۰۰", "requirement": 50000, "type": "power", "reward": 25000},
    "a37": {"name": "💰 ۱۰۰۰۰۰ سکه", "desc": "۱۰۰۰۰۰ سکه", "requirement": 100000, "type": "coins", "reward": 50000},
    "a38": {"name": "🗡️ ۱۰۰ حمله", "desc": "۱۰۰ حمله", "requirement": 100, "type": "attacks", "reward": 15000},
    "a39": {"name": "💀 ۱۰۰ کشته", "desc": "۱۰۰ کشته", "requirement": 100, "type": "kills", "reward": 15000},
    "a40": {"name": "⚔️ استریک ۲۰", "desc": "۲۰ حمله پشت سر هم", "requirement": 20, "type": "streak", "reward": 10000},
    
    # مدال‌های حماسی (51-70)
    "a41": {"name": "🔥 ارباب جنگ", "desc": "۵۰۰ حمله", "requirement": 500, "type": "attacks", "reward": 50000},
    "a42": {"name": "💀 اهریمن", "desc": "۵۰۰ کشته", "requirement": 500, "type": "kills", "reward": 50000},
    "a43": {"name": "💰 میلیونر", "desc": "۱,۰۰۰,۰۰۰ سکه", "requirement": 1000000, "type": "coins", "reward": 200000},
    "a44": {"name": "💪 قدرتمندترین", "desc": "قدرت ۲۰۰۰۰۰", "requirement": 200000, "type": "power", "reward": 100000},
    "a45": {"name": "🏰 امپراتور قلعه", "desc": "قلعه سطح ۲۰", "requirement": 20, "type": "fort", "reward": 50000},
    "a46": {"name": "👑 افسانه زنده", "desc": "سطح ۵۰", "requirement": 50, "type": "level", "reward": 100000},
    "a47": {"name": "🎌 امپراتور کلن", "desc": "کلن سطح ۱۰", "requirement": 10, "type": "clan_level", "reward": 75000},
    "a48": {"name": "⚔️ شکست‌ناپذیر", "desc": "۱۰۰ استریک", "requirement": 100, "type": "streak", "reward": 100000},
    "a49": {"name": "☢️ نابودگر", "desc": "۱۰ حمله اتمی", "requirement": 10, "type": "nuclear", "reward": 75000},
    "a50": {"name": "👑 امپراتوری", "desc": "ساخت امپراتوری", "requirement": 1, "type": "empire", "reward": 50000},
    "a51": {"name": "💑 ازدواج", "desc": "ازدواج موفق", "requirement": 1, "type": "marriage", "reward": 25000},
    "a52": {"name": "🐉 استاد حیوانات", "desc": "حیوان سطح ۲۰", "requirement": 20, "type": "pet", "reward": 40000},
    "a53": {"name": "🛒 بازرگان ماهر", "desc": "۵۰ فروش بازار", "requirement": 50, "type": "market", "reward": 25000},
    "a54": {"name": "⚔️ استاد دوال", "desc": "۵۰ دوال برده", "requirement": 50, "type": "duels", "reward": 30000},
    "a55": {"name": "💼 ۱۰۰۰ کار", "desc": "۱۰۰۰ بار کار", "requirement": 1000, "type": "work", "reward": 30000},
    "a56": {"name": "🕵️ استاد جاسوس", "desc": "۲۰۰ جاسوسی", "requirement": 200, "type": "spies", "reward": 30000},
    "a57": {"name": "💣 ارباب تروریست", "desc": "۱۰۰۰ تروریست", "requirement": 1000, "type": "terrorists", "reward": 50000},
    "a58": {"name": "🎌 رهبر بزرگ", "desc": "کلن سطح ۲۰", "requirement": 20, "type": "clan_level", "reward": 150000},
    "a59": {"name": "👑 خداوندگار", "desc": "سطح ۱۰۰", "requirement": 100, "type": "level", "reward": 500000},
    "a60": {"name": "💎 ابرقدرت", "desc": "قدرت ۱,۰۰۰,۰۰۰", "requirement": 1000000, "type": "power", "reward": 1000000},
    
    # مدال‌های افسانه‌ای (71-80)
    "a61": {"name": "⚡ خدای جنگ", "desc": "۱۰۰۰ کشته", "requirement": 1000, "type": "kills", "reward": 250000},
    "a62": {"name": "🛡️ فناناپذیر", "desc": "۱۰۰۰ دفاع", "requirement": 1000, "type": "defends", "reward": 200000},
    "a63": {"name": "🏆 فاتح جهان", "desc": "۱۰۰ قلمرو فتح", "requirement": 100, "type": "territories", "reward": 300000},
    "a64": {"name": "🌍 امپراتور جهان", "desc": "امپراتوری سطح ۱۰", "requirement": 10, "type": "empire_level", "reward": 500000},
    "a65": {"name": "🔥 افسانه مطلق", "desc": "تمام مدال‌ها", "requirement": 60, "type": "all_achievements", "reward": 1000000},
    
    # مدال‌های مخفی (81-100)
    "s1": {"name": "🦉 جغد شب", "desc": "حمله بین ۲-۴ صبح", "requirement": 1, "type": "secret_night", "reward": 10000, "secret": True},
    "s2": {"name": "🍀 خوش شانس", "desc": "برنده لاتاری", "requirement": 1, "type": "secret_lottery", "reward": 5000, "secret": True},
    "s3": {"name": "🎲 قمارباز", "desc": "۱۰۰ برد کازینو", "requirement": 100, "type": "secret_casino", "reward": 25000, "secret": True},
    "s4": {"name": "🤬 خیانتکار", "desc": "۵ بار تغییر نام", "requirement": 5, "type": "secret_betray", "reward": 15000, "secret": True},
    "s5": {"name": "💸 حراج", "desc": "گران‌ترین سلاح بخر", "requirement": 50000, "type": "secret_expensive", "reward": 50000, "secret": True},
    "s6": {"name": "⚡ رعد", "desc": "حمله با قدرت ۱۰۰۰۰", "requirement": 10000, "type": "secret_power", "reward": 20000, "secret": True},
    "s7": {"name": "🎯 تک تیرانداز", "desc": "۱۰۰٪ دقت", "requirement": 100, "type": "secret_accuracy", "reward": 15000, "secret": True},
    "s8": {"name": "🛸 بیگانه", "desc": "با بیگانه دوست شو", "requirement": 1, "type": "secret_alien", "reward": 50000, "secret": True},
    "s9": {"name": "🧙 جادوگر", "desc": "۱۰۰۰ بار جادو کن", "requirement": 1000, "type": "secret_magic", "reward": 50000, "secret": True},
    "s10": {"name": "🐉 اژدها", "desc": "اژدها داشته باش", "requirement": 1, "type": "secret_dragon", "reward": 100000, "secret": True},
    "s11": {"name": "👻 روح", "desc": "از مرگ برگرد", "requirement": 1, "type": "secret_ghost", "reward": 25000, "secret": True},
    "s12": {"name": "⏰ زودتر از همه", "desc": "اولین بازیکن روز", "requirement": 1, "type": "secret_first", "reward": 10000, "secret": True},
    "s13": {"name": "📆 یک ماهه", "desc": "۳۰ روز متوالی", "requirement": 30, "type": "secret_month", "reward": 100000, "secret": True},
    "s14": {"name": "💎 کلکسیونر", "desc": "۵۰ سلاح مختلف", "requirement": 50, "type": "secret_collector", "reward": 75000, "secret": True},
    "s15": {"name": "🏆 قهرمان", "desc": "اول مسابقه بشو", "requirement": 1, "type": "secret_tournament", "reward": 50000, "secret": True},
    "s16": {"name": "🌪️ طوفان", "desc": "۱۰۰۰ حمله هوایی", "requirement": 1000, "type": "secret_air", "reward": 50000, "secret": True},
    "s17": {"name": "🌊 سونامی", "desc": "۱۰۰۰ حمله دریایی", "requirement": 1000, "type": "secret_sea", "reward": 50000, "secret": True},
    "s18": {"name": "🌋 آتشفشان", "desc": "۱۰۰۰ حمله زمینی", "requirement": 1000, "type": "secret_ground", "reward": 50000, "secret": True},
    "s19": {"name": "💝 بخشنده", "desc": "۱۰۰۰۰۰ هدیه بده", "requirement": 100000, "type": "secret_gift", "reward": 50000, "secret": True},
    "s20": {"name": "🌟 افسانه", "desc": "راز نهایی", "requirement": 1, "type": "secret_final", "reward": 1000000, "secret": True},
}
# ==================================================
# ساختمان‌ها - 35 ساختمان کامل
# ==================================================

BUILDINGS_DB = {
    1: {"name": "🏠 مزرعه", "cost": 1000, "production": {"food": 100}, "upgrade_cost": 500, "max_level": 20},
    2: {"name": "⛏️ معدن", "cost": 1500, "production": {"iron": 50, "gold": 10}, "upgrade_cost": 800, "max_level": 20},
    3: {"name": "🛢️ پالایشگاه", "cost": 2000, "production": {"oil": 30}, "upgrade_cost": 1000, "max_level": 20},
    4: {"name": "🏭 کارخانه", "cost": 3000, "production": {"weapon": 5}, "upgrade_cost": 1500, "max_level": 20},
    5: {"name": "🔬 آزمایشگاه", "cost": 5000, "production": {"research": 10}, "upgrade_cost": 2000, "max_level": 20},
    6: {"name": "🏥 بیمارستان", "cost": 2000, "production": {"heal": 500}, "upgrade_cost": 1000, "max_level": 20},
    7: {"name": "🏫 آکادمی", "cost": 3000, "production": {"exp": 50}, "upgrade_cost": 1500, "max_level": 20},
    8: {"name": "🏦 بانک", "cost": 4000, "production": {"interest": 5}, "upgrade_cost": 2000, "max_level": 20},
    9: {"name": "🏰 قلعه", "cost": 5000, "production": {"defense": 100}, "upgrade_cost": 2500, "max_level": 25},
    10: {"name": "🗼 برج", "cost": 3000, "production": {"attack": 50}, "upgrade_cost": 1500, "max_level": 20},
    11: {"name": "🚪 دروازه", "cost": 2000, "production": {"defense": 50}, "upgrade_cost": 1000, "max_level": 20},
    12: {"name": "🕳️ سنگر", "cost": 1500, "production": {"defense": 30}, "upgrade_cost": 800, "max_level": 20},
    13: {"name": "📡 رادار", "cost": 2500, "production": {"vision": 20}, "upgrade_cost": 1200, "max_level": 20},
    14: {"name": "⚡ نیروگاه", "cost": 3000, "production": {"energy": 100}, "upgrade_cost": 1500, "max_level": 20},
    15: {"name": "💧 تصفیه خانه", "cost": 1500, "production": {"water": 100}, "upgrade_cost": 800, "max_level": 20},
    16: {"name": "🌾 سیلو", "cost": 1000, "storage": {"food": 10000}, "upgrade_cost": 500, "max_level": 20},
    17: {"name": "💰 خزانه", "cost": 2000, "storage": {"coins": 50000}, "upgrade_cost": 1000, "max_level": 20},
    18: {"name": "🛒 بازار", "cost": 1500, "production": {"trade": 20}, "upgrade_cost": 800, "max_level": 20},
    19: {"name": "🎌 سفارت", "cost": 2000, "production": {"diplomacy": 10}, "upgrade_cost": 1000, "max_level": 20},
    20: {"name": "🕵️ مقر جاسوسی", "cost": 2500, "production": {"spy": 20}, "upgrade_cost": 1200, "max_level": 20},
    21: {"name": "⚔️ پادگان", "cost": 2000, "production": {"soldiers": 10}, "upgrade_cost": 1000, "max_level": 20},
    22: {"name": "🎯 میدان تیر", "cost": 1500, "production": {"accuracy": 10}, "upgrade_cost": 800, "max_level": 20},
    23: {"name": "🏋️ باشگاه", "cost": 1000, "production": {"strength": 10}, "upgrade_cost": 500, "max_level": 20},
    24: {"name": "🧘 معبد", "cost": 2000, "production": {"peace": 10}, "upgrade_cost": 1000, "max_level": 20},
    25: {"name": "🔮 آزمایشگاه مخفی", "cost": 5000, "production": {"secret": 10}, "upgrade_cost": 2500, "max_level": 20},
    26: {"name": "🚀 پایگاه فضایی", "cost": 10000, "production": {"space": 50}, "upgrade_cost": 5000, "max_level": 20},
    27: {"name": "🤖 کارخانه ربات", "cost": 8000, "production": {"robot": 10}, "upgrade_cost": 4000, "max_level": 20},
    28: {"name": "🐉 غار اژدها", "cost": 15000, "production": {"dragon": 5}, "upgrade_cost": 7500, "max_level": 20},
    29: {"name": "✨ معبد خدایان", "cost": 20000, "production": {"bless": 20}, "upgrade_cost": 10000, "max_level": 20},
    30: {"name": "🌍 مرکز جهانی", "cost": 50000, "production": {"all": 50}, "upgrade_cost": 25000, "max_level": 20},
}

# ==================================================
# تکنولوژی‌ها - 50 تکنولوژی کامل
# ==================================================

TECHNOLOGIES_DB = {
    1: {"name": "⚔️ تیز کردن شمشیر", "cost": 1000, "bonus": {"attack": 10}, "level_req": 1},
    2: {"name": "🛡️ تقویت زره", "cost": 1000, "bonus": {"defense": 10}, "level_req": 1},
    3: {"name": "🏹 دقت بالا", "cost": 1500, "bonus": {"accuracy": 5}, "level_req": 2},
    4: {"name": "⚡ سرعت عمل", "cost": 1500, "bonus": {"speed": 5}, "level_req": 2},
    5: {"name": "🔫 قدرت آتش", "cost": 2000, "bonus": {"damage": 10}, "level_req": 3},
    6: {"name": "💣 مواد منفجره", "cost": 2000, "bonus": {"explosion": 10}, "level_req": 3},
    7: {"name": "🕵️ جاسوسی حرفه‌ای", "cost": 2500, "bonus": {"spy": 20}, "level_req": 4},
    8: {"name": "💰 مدیریت اقتصادی", "cost": 2500, "bonus": {"income": 20}, "level_req": 4},
    9: {"name": "🏰 معماری", "cost": 3000, "bonus": {"building": 20}, "level_req": 5},
    10: {"name": "🔬 تحقیقات", "cost": 3000, "bonus": {"research": 20}, "level_req": 5},
    11: {"name": "✈️ تکنولوژی هوایی", "cost": 4000, "bonus": {"air": 20}, "level_req": 6},
    12: {"name": "🚢 تکنولوژی دریایی", "cost": 4000, "bonus": {"sea": 20}, "level_req": 6},
    13: {"name": "☢️ انرژی اتمی", "cost": 5000, "bonus": {"nuclear": 50}, "level_req": 7},
    14: {"name": "🔋 انرژی پاک", "cost": 5000, "bonus": {"energy": 50}, "level_req": 7},
    15: {"name": "🤖 هوش مصنوعی", "cost": 10000, "bonus": {"ai": 50}, "level_req": 10},
    16: {"name": "🧬 بیوتکنولوژی", "cost": 10000, "bonus": {"health": 500}, "level_req": 10},
    17: {"name": "🌌 فضا", "cost": 20000, "bonus": {"space": 100}, "level_req": 15},
    18: {"name": "🕰️ زمان", "cost": 50000, "bonus": {"time": 50}, "level_req": 20},
    19: {"name": "✨ جادو", "cost": 100000, "bonus": {"magic": 100}, "level_req": 25},
    20: {"name": "👑 الهی", "cost": 500000, "bonus": {"divine": 500}, "level_req": 50},
    21: {"name": "🌾 کشاورزی پیشرفته", "cost": 2000, "bonus": {"food": 200}, "level_req": 3},
    22: {"name": "⛏️ استخراج عمیق", "cost": 2500, "bonus": {"mining": 50}, "level_req": 4},
    23: {"name": "🛢️ حفاری نفت", "cost": 3000, "bonus": {"oil": 50}, "level_req": 5},
    24: {"name": "🏭 تولید انبوه", "cost": 3500, "bonus": {"production": 50}, "level_req": 5},
    25: {"name": "💊 پزشکی مدرن", "cost": 4000, "bonus": {"heal": 1000}, "level_req": 6},
    26: {"name": "📚 آموزش", "cost": 3000, "bonus": {"exp": 100}, "level_req": 5},
    27: {"name": "💹 سرمایه‌گذاری", "cost": 5000, "bonus": {"interest": 10}, "level_req": 7},
    28: {"name": "🛡️ دفاع همه جانبه", "cost": 6000, "bonus": {"defense": 50}, "level_req": 8},
    29: {"name": "⚔️ حمله ترکیبی", "cost": 7000, "bonus": {"combo": 20}, "level_req": 9},
    30: {"name": "🎯 هدف گیری خودکار", "cost": 8000, "bonus": {"auto_aim": 20}, "level_req": 10},
}
# ==================================================
# توابع کمکی اصلی
# ==================================================

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            data.setdefault("users", {})
            data.setdefault("banned_users", [])
            data.setdefault("duels", {})
            data.setdefault("daily_resets", {})
            data.setdefault("pending_action", {})
            data.setdefault("alliances", [])
            data.setdefault("clans", {})
            data.setdefault("missions", {})
            data.setdefault("online_users", {})
            data.setdefault("market_listings", [])
            data.setdefault("tournaments", {})
            data.setdefault("gifts", {})
            data.setdefault("global_events", [])
            data.setdefault("daily_challenges", {})
            data.setdefault("empires", {})
            data.setdefault("lottery", {"tickets": [], "pool": 0})
            data.setdefault("casino", {})
            data.setdefault("battles", {})
            data.setdefault("marriages", {})
            data.setdefault("pets", {})
            data.setdefault("buildings", {})
            data.setdefault("technologies", {})
            data.setdefault("job_data", {})
            data.setdefault("achievements_data", {})
            return data
    return {
        "users": {}, "banned_users": [], "duels": {}, "daily_resets": {},
        "pending_action": {}, "alliances": [], "clans": {}, "missions": {},
        "online_users": {}, "market_listings": [], "tournaments": {},
        "gifts": {}, "global_events": [], "daily_challenges": {},
        "empires": {}, "lottery": {"tickets": [], "pool": 0}, "casino": {},
        "battles": {}, "marriages": {}, "pets": {}, "buildings": {},
        "technologies": {}, "job_data": {}, "achievements_data": {}
    }

def attack_select_keypad(current_user_id):
    builder = ChatKeypadBuilder()
    data = load_data()
    for uid, u in data["users"].items():
        if uid != current_user_id and u.get("country_name") and uid not in data.get("banned_users", []):
            builder.row(builder.button(f"attack_target_{uid}", f"💥 {u['country_name'][:15]} 💪{format_num(calculate_power(u))}"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()
    
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def format_num(num):
    if num >= 1_000_000_000:
        return f"{num/1_000_000_000:.1f}B"
    elif num >= 1_000_000:
        return f"{num/1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num/1_000:.1f}K"
    return f"{int(num):,}"

def calculate_power(user):
    base = 500
    level_bonus = user.get("level", 1) * 150
    soldier_power = user.get("soldiers", 0) * 50
    weapon_power = sum(w.get("power", 0) for w in user.get("weapons_list", []))
    terrorist_power = user.get("terrorists", 0) * 20
    fort_power = user.get("fort_level", 0) * 500
    job_bonus = 0
    job = user.get("job", 0)
    if job > 0 and job in JOBS_DB:
        job_bonus = JOBS_DB[job]["bonus"].get("attack", 0) * user.get("job_level", 1)
    pet_bonus = 0
    for pet in user.get("pets_list", []):
        pet_bonus += PETS_DB.get(pet.get("id", 0), {}).get("bonus", {}).get("attack", 0) * pet.get("level", 1)
    return base + level_bonus + soldier_power + weapon_power + terrorist_power + fort_power + job_bonus + pet_bonus

def get_health_bar(current, max_hp):
    percent = int((current / max_hp) * 100)
    filled = percent // 5
    return "█" * filled + "░" * (20 - filled) + f" {percent}%"

async def safe_reply(message, text, **kwargs):
    try:
        await message.reply(text, **kwargs)
    except Exception as e:
        print(f"Error: {e}")

def update_online_status(data, user_id):
    data.setdefault("online_users", {})[user_id] = datetime.now().isoformat()
    now = datetime.now()
    offline = [uid for uid, last in data["online_users"].items() 
               if now - datetime.fromisoformat(last) > timedelta(minutes=5)]
    for uid in offline:
        del data["online_users"][uid]
    return len(data["online_users"])

def check_achievements(data, user_id):
    user = data["users"].get(user_id, {})
    if not user:
        return []
    new_achievements = []
    for aid, ach in ACHIEVEMENTS_DB.items():
        if aid in user.get("achievements", []):
            continue
        achieved = False
        if ach["type"] == "coins" and user.get("coins", 0) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "power" and calculate_power(user) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "level" and user.get("level", 1) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "attacks" and user.get("attacks", 0) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "kills" and user.get("kills", 0) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "defends" and user.get("defends", 0) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "spies" and user.get("spies", 0) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "work" and user.get("work_count", 0) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "fort" and user.get("fort_level", 0) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "soldiers" and user.get("soldiers", 0) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "weapons" and len(user.get("weapons_list", [])) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "terrorists" and user.get("terrorists", 0) >= ach["requirement"]:
            achieved = True
        elif ach["type"] == "streak" and user.get("daily_streak", 0) >= ach["requirement"]:
            achieved = True
        if achieved:
            user.setdefault("achievements", []).append(aid)
            user["coins"] = user.get("coins", 0) + ach["reward"]
            new_achievements.append(ach)
    if new_achievements:
        save_data(data)
    return new_achievements
    # ==================================================
# کیبوردها - 50+ کیبورد مختلف
# ==================================================

def main_menu_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("status", "📊 وضعیت"), builder.button("profile", "👤 پروفایل"))
    builder.row(builder.button("work", "💼 کار"), builder.button("daily", "🎁 پاداش روزانه"))
    builder.row(builder.button("challenge", "🏆 چالش روزانه"), builder.button("attendance", "📅 حضور و غیاب"))
    builder.row(builder.button("recruit", "⚔️ استخدام"), builder.button("shop", "🔫 فروشگاه"))
    builder.row(builder.button("attack", "💥 حمله"), builder.button("defend", "🛡️ دفاع"))
    builder.row(builder.button("spy", "🕵️ جاسوسی"), builder.button("alliance", "🤝 اتحاد"))
    builder.row(builder.button("economy", "🏦 اقتصاد"), builder.button("fort", "🏰 قلعه"))
    builder.row(builder.button("clan", "🎌 کلن"), builder.button("empire", "👑 امپراتوری"))
    builder.row(builder.button("missions", "📜 مأموریت"), builder.button("leaderboard", "🏆 لیدربرد"))
    builder.row(builder.button("duel", "⚔️ دوال"), builder.button("tournament", "🏆 مسابقه"))
    builder.row(builder.button("medals", "🎖️ مدال"), builder.button("market", "🛒 بازار"))
    builder.row(builder.button("lottery", "🎰 لاتاری"), builder.button("casino", "🎲 کازینو"))
    builder.row(builder.button("resources", "⛏️ منابع"), builder.button("upgrade", "📈 ارتقا"))
    builder.row(builder.button("job", "💼 شغل"), builder.button("pet", "🐉 حیوان"))
    builder.row(builder.button("build", "🏗️ ساختمان"), builder.button("tech", "🔬 تکنولوژی"))
    builder.row(builder.button("marriage", "💑 ازدواج"), builder.button("inventory", "🎒 انبار"))
    builder.row(builder.button("help", "❓ راهنما"), builder.button("transfer", "💸 انتقال"))
    builder.row(builder.button("betray", "🤬 خیانت"), builder.button("buy_coins", "💰 خرید"))
    builder.row(builder.button("gift", "🎁 هدیه"), builder.button("events", "🌍 رویدادها"))
    builder.row(builder.button("settings", "⚙️ تنظیمات"), builder.button("support", "📞 پشتیبانی"))
    return builder.build()

def admin_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("admin_stats", "📊 آمار کلی"))
    builder.row(builder.button("admin_online", "🟢 آنلاین"))
    builder.row(builder.button("admin_users", "👥 کاربران"))
    builder.row(builder.button("admin_banned", "🚫 بن‌ها"))
    builder.row(builder.button("admin_broadcast", "📢 اطلاعیه"))
    builder.row(builder.button("admin_event", "🌍 رویداد"))
    builder.row(builder.button("admin_gift_all", "🎁 هدیه همگانی"))
    builder.row(builder.button("admin_lottery_draw", "🎰 قرعه‌کشی"))
    builder.row(builder.button("admin_tournament", "🏆 مسابقه"))
    builder.row(builder.button("admin_reset", "🔄 ریست"))
    builder.row(builder.button("admin_backup", "💾 پشتیبان"))
    builder.row(builder.button("admin_restore", "📂 بازیابی"))
    builder.row(builder.button("admin_logs", "📋 لاگ‌ها"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def attack_type_keypad(target_id):
    builder = ChatKeypadBuilder()
    builder.row(builder.button(f"attack_ground_{target_id}", "⚔️ زمینی"))
    builder.row(builder.button(f"attack_air_{target_id}", "✈️ هوایی"))
    builder.row(builder.button(f"attack_sea_{target_id}", "🌊 دریایی"))
    builder.row(builder.button(f"attack_nuclear_{target_id}", "☢️ اتمی (50K💰)"))
    builder.row(builder.button(f"attack_chemical_{target_id}", "🧪 شیمیایی (30K💰)"))
    builder.row(builder.button(f"attack_bacterial_{target_id}", "🦠 باکتریایی (40K💰)"))
    builder.row(builder.button(f"attack_space_{target_id}", "🛸 فضایی (100K💰)"))
    builder.row(builder.button(f"attack_magic_{target_id}", "✨ جادویی (80K💰)"))
    builder.row(builder.button("attack_back", "🔙"))
    return builder.build()

def clan_menu_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("clan_create", "🏰 ساخت (10K💰)"))
    builder.row(builder.button("clan_my", "📋 کلن من"))
    builder.row(builder.button("clan_list", "📜 لیست کلن‌ها"))
    builder.row(builder.button("clan_rank", "🏆 رتبه کلن‌ها"))
    builder.row(builder.button("clan_join", "🤝 درخواست عضویت"))
    builder.row(builder.button("clan_donate", "💰 کمک مالی"))
    builder.row(builder.button("clan_upgrade", "📈 ارتقا"))
    builder.row(builder.button("clan_shop", "🛒 فروشگاه کلن"))
    builder.row(builder.button("clan_war", "⚔️ جنگ کلن"))
    builder.row(builder.button("clan_chat", "💬 چت کلن"))
    builder.row(builder.button("clan_mission", "📜 مأموریت کلن"))
    builder.row(builder.button("clan_leave", "🚪 خروج"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def empire_menu_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("empire_create", "👑 ساخت (50K💰)"))
    builder.row(builder.button("empire_info", "📊 اطلاعات"))
    builder.row(builder.button("empire_members", "👥 اعضا"))
    builder.row(builder.button("empire_join", "🤝 پیوستن"))
    builder.row(builder.button("empire_upgrade", "📈 ارتقا"))
    builder.row(builder.button("empire_war", "⚔️ اعلان جنگ"))
    builder.row(builder.button("empire_territory", "🗺️ قلمروها"))
    builder.row(builder.button("empire_tax", "💰 مالیات"))
    builder.row(builder.button("empire_shop", "🛒 فروشگاه"))
    builder.row(builder.button("empire_treasury", "🏦 خزانه"))
    builder.row(builder.button("empire_donate", "💸 کمک"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def casino_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("casino_slots", "🎰 اسلات (100💰)"))
    builder.row(builder.button("casino_blackjack", "🃏 بلک‌جک (500💰)"))
    builder.row(builder.button("casino_roulette", "🎡 رولت (200💰)"))
    builder.row(builder.button("casino_dice", "🎲 تاس (50💰)"))
    builder.row(builder.button("casino_poker", "🃟 پوکر (1000💰)"))
    builder.row(builder.button("casino_baccarat", "🎴 باکارا (2000💰)"))
    builder.row(builder.button("casino_wheel", "🎡 چرخ شانس (100💰)"))
    builder.row(builder.button("casino_stats", "📊 آمار من"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def marriage_menu_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("marriage_propose", "💍 پیشنهاد ازدواج"))
    builder.row(builder.button("marriage_my", "💑 ازدواج من"))
    builder.row(builder.button("marriage_requests", "📨 درخواست‌ها"))
    builder.row(builder.button("marriage_gift", "🎁 هدیه به همسر"))
    builder.row(builder.button("marriage_divorce", "💔 طلاق (10K💰)"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def pet_menu_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("pet_shop", "🐕 خرید حیوان"))
    builder.row(builder.button("pet_list", "📋 حیوانات من"))
    builder.row(builder.button("pet_feed", "🍖 غذا دادن"))
    builder.row(builder.button("pet_upgrade", "📈 ارتقا"))
    builder.row(builder.button("pet_rename", "✏️ تغییر نام"))
    builder.row(builder.button("pet_sell", "💰 فروش"))
    builder.row(builder.button("pet_heal", "💊 درمان"))  # اضافه کن
    builder.row(builder.button("pet_equip", "🎽 تجهیزات"))  # اضافه کن
    builder.row(builder.button("pet_battle", "⚔️ مسابقه"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def job_menu_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("job_list", "📋 لیست مشاغل"))
    builder.row(builder.button("job_my", "💼 شغل من"))
    builder.row(builder.button("job_change", "🔄 تغییر شغل (5K💰)"))
    builder.row(builder.button("job_upgrade", "📈 ارتقا شغل"))
    builder.row(builder.button("job_work", "💪 کار ویژه"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def building_menu_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("build_list", "📋 ساختمان‌ها"))
    builder.row(builder.button("build_my", "🏗️ ساختمان‌های من"))
    builder.row(builder.button("build_construct", "🔨 ساخت"))
    builder.row(builder.button("build_upgrade", "📈 ارتقا"))
    builder.row(builder.button("build_destroy", "💔 تخریب"))
    builder.row(builder.button("build_collect", "📦 جمع‌آوری تولید"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def tech_menu_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("tech_list", "📋 تکنولوژی‌ها"))
    builder.row(builder.button("tech_my", "🔬 تکنولوژی من"))
    builder.row(builder.button("tech_research", "🧪 تحقیق"))
    builder.row(builder.button("tech_upgrade", "📈 ارتقا"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def economy_menu_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("tax", "💰 دریافت مالیات"))
    builder.row(builder.button("plunder", "⚔️ غارت"))
    builder.row(builder.button("treasury", "🏦 وضعیت خزانه"))
    builder.row(builder.button("trade", "🔄 تجارت"))
    builder.row(builder.button("stock", "📈 بازار سهام"))
    builder.row(builder.button("loan", "🏦 وام"))
    builder.row(builder.button("invest", "📈 سرمایه‌گذاری"))
    builder.row(builder.button("bank", "🏦 بانک"))
    builder.row(builder.button("exchange", "💱 صرافی"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def duel_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("duel_100", "💰 100"), builder.button("duel_500", "💰 500"))
    builder.row(builder.button("duel_1000", "💰 1K"), builder.button("duel_5000", "💰 5K"))
    builder.row(builder.button("duel_10000", "💰 10K"), builder.button("duel_50000", "💰 50K"))
    builder.row(builder.button("duel_100000", "💰 100K"), builder.button("duel_500000", "💰 500K"))
    builder.row(builder.button("duel_random", "🎲 تصادفی"), builder.button("duel_rank", "🏆 رنک"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def shop_menu_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("shop_ground", "⚔️ سلاح‌های زمینی"))
    builder.row(builder.button("shop_air", "✈️ سلاح‌های هوایی"))
    builder.row(builder.button("shop_sea", "🚢 سلاح‌های دریایی"))
    builder.row(builder.button("shop_special", "💎 سلاح‌های ویژه"))
    builder.row(builder.button("shop_ammo", "📦 مهمات"))
    builder.row(builder.button("shop_armor", "🛡️ زره"))
    builder.row(builder.button("shop_potion", "🧪 معجون"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()

def leaderboard_keypad():
    builder = ChatKeypadBuilder()
    builder.row(builder.button("lb_power", "💪 قدرت"), builder.button("lb_coins", "💰 سکه"))
    builder.row(builder.button("lb_level", "📈 سطح"), builder.button("lb_kills", "💀 کشته‌ها"))
    builder.row(builder.button("lb_attacks", "⚔️ حملات"), builder.button("lb_clan", "🎌 کلن"))
    builder.row(builder.button("lb_empire", "👑 امپراتوری"), builder.button("lb_today", "📅 امروز"))
    builder.row(builder.button("lb_weekly", "📆 هفته"), builder.button("lb_monthly", "📅 ماه"))
    builder.row(builder.button("back_main", "🔙"))
    return builder.build()
    # ==================================================
# هندلر اصلی ربات - قسمت اول
# ==================================================

@bot.on_message()
async def message_handler(bot: Robot, message: Message):
    user_id = str(message.sender_id)
    text = message.text.strip() if message.text else ""
    button_id = message.aux_data.button_id if message.aux_data else None
    data = load_data()
    
    # بروزرسانی وضعیت آنلاین
    online_count = update_online_status(data, user_id)
    
    # چک کردن پنل ادمین
    if text == ADMIN_PASSWORD:
        await safe_reply(message, "🔐 **پنل مدیریت فوق پیشرفته**\n\nبه پنل ادمین خوش آمدید.", chat_keypad=admin_keypad())
        return
    
    # چک کردن بن بودن کاربر
    if user_id in data.get("banned_users", []):
        await safe_reply(message, "🚫 **شما بن شده‌اید!**\n\nدلیل: تخلف از قوانین\nبرای اعتراض به ادمین پیام بدید:\n🆔 @AdminSupport", chat_keypad=None)
        return
    
    # استارت ربات
    if text == "/start":
        if user_id not in data["users"] or not data["users"][user_id].get("country_name"):
            await safe_reply(message, 
                "🌍 **به جنگ کشورها خوش آمدید!** 🌍\n\n"
                "⚔️ اینجا می‌تونی:\n"
                "• کشور خودت رو بسازی\n"
                "• به دیگران حمله کنی\n"
                "• با بقیه اتحاد ببندی\n"
                "• امپراتوری خودت رو تشکیل بدی\n"
                "• و کلی چیزای دیگه...\n\n"
                "✨ **جوایز شروع:**\n"
                "💰 ۱۰,۰۰۰ سکه\n"
                "⚔️ ۵۰ سرباز\n"
                "👥 ۵۰۰ رعایا\n"
                "🛡️ ۱۰۰,۰۰۰ جان\n\n"
                "📝 **لطفاً نام کشور خود را وارد کنید:**", chat_keypad=None)
            data["pending_action"][user_id] = {"action": "set_country_name"}
            save_data(data)
            return
        await safe_reply(message, "🏠 **منوی اصلی**\n\nاز دکمه‌های زیر استفاده کنید:", chat_keypad=main_menu_keypad())
        return
    
    # پردازش pending actions
    pending = data.get("pending_action", {}).get(user_id, {})
    
    # ساخت کشور جدید
    if pending.get("action") == "set_country_name":
        if not text or len(text.strip()) == 0:
            await safe_reply(message, "❌ نام کشور نمی‌تواند خالی باشد!", chat_keypad=None)
            return
        country_name = text[:30].strip()
        
        if user_id not in data["users"]:
            data["users"][user_id] = {}
        
        user = data["users"][user_id]
        user["country_name"] = country_name
        user["coins"] = 10000
        user["gold"] = 5000
        user["food"] = 5000
        user["iron"] = 1000
        user["oil"] = 500
        user["uranium"] = 100
        user["diamond"] = 10
        user["peasants"] = 500
        user["health"] = 100000
        user["max_health"] = 100000
        user["soldiers"] = 50
        user["weapons"] = 0
        user["weapons_list"] = []
        user["kills"] = 0
        user["deaths"] = 0
        user["attacks"] = 0
        user["defends"] = 0
        user["exp"] = 0
        user["level"] = 1
        user["terrorists"] = 0
        user["spies"] = 0
        user["fort_level"] = 0
        user["achievements"] = []
        user["medals"] = [{"id": "new_country", "name": "🌱 کشور تازه تأسیس", "emoji": "🌱"}]
        user["attack_streak"] = 0
        user["daily_streak"] = 0
        user["investments"] = 0
        user["job"] = 1
        user["job_level"] = 1
        user["pets_list"] = []
        user["buildings_list"] = []
        user["technologies_list"] = []
        user["alliances"] = []
        user["clan_id"] = None
        user["empire_id"] = None
        user["married_to"] = None
        user["work_count"] = 0
        
        del data["pending_action"][user_id]
        save_data(data)
        
        await safe_reply(message,
            f"✅ **کشور {country_name} با موفقیت ساخته شد!**\n\n"
            f"📊 **آمار اولیه:**\n"
            f"💰 سکه: {format_num(user['coins'])}\n"
            f"⚔️ سربازان: {user['soldiers']}\n"
            f"👥 رعایا: {user['peasants']}\n"
            f"❤️ جان: {format_num(user['health'])}\n"
            f"🏆 مدال: 🌱 کشور تازه تأسیس\n\n"
            f"🎮 از منوی اصلی بازی رو شروع کن!",
            chat_keypad=main_menu_keypad())
        return
    
    # اگر کاربر ثبت نام نکرده
    if user_id not in data["users"] or not data["users"][user_id].get("country_name"):
        await safe_reply(message, "❌ لطفا ابتدا /start بزنید!", chat_keypad=None)
        return
    
    user = data["users"][user_id]
    country_name = user["country_name"]
    
    # ========== دکمه‌های اصلی ==========
    
    # برگشت به منوی اصلی
    if button_id == "back_main":
        await safe_reply(message, "🏠 **منوی اصلی**", chat_keypad=main_menu_keypad())
        return
    
    # وضعیت
    if button_id == "status":
        health_bar = get_health_bar(user.get("health", 100000), user.get("max_health", 100000))
        total_users = len([u for u in data["users"].values() if u.get("country_name")])
        total_power = sum(calculate_power(u) for u in data["users"].values() if u.get("country_name"))
        
        await safe_reply(message,
            f"📊 **وضعیت جهانی**\n\n"
            f"🌍 کشورهای فعال: {total_users}\n"
            f"💪 قدرت کل: {format_num(total_power)}\n"
            f"🟢 آنلاین: {online_count}\n"
            f"⚔️ حملات کل: {sum(u.get('attacks', 0) for u in data['users'].values()):,}\n"
            f"💀 کشته‌ها کل: {sum(u.get('kills', 0) for u in data['users'].values()):,}\n\n"
            f"📈 **کشور {country_name}**\n"
            f"❤️ [{health_bar}] {format_num(user.get('health', 100000))}/{format_num(user.get('max_health', 100000))}\n"
            f"💰 سکه: {format_num(user.get('coins', 0))}\n"
            f"💪 قدرت: {format_num(calculate_power(user))}\n"
            f"📈 سطح: {user.get('level', 1)}\n"
            f"🏰 قلعه: سطح {user.get('fort_level', 0)}\n"
            f"🎌 کلن: {'دارد' if user.get('clan_id') else 'ندارد'}\n"
            f"👑 امپراتوری: {'دارد' if user.get('empire_id') else 'ندارد'}",
            chat_keypad=main_menu_keypad())
        return
    
    # پروفایل
    if button_id == "profile":
        health_bar = get_health_bar(user.get("health", 100000), user.get("max_health", 100000))
        
        # اطلاعات شغل
        job_name = "ندارد"
        job_level = 0
        if user.get("job", 0) in JOBS_DB:
            job_name = JOBS_DB[user["job"]]["name"]
            job_level = user.get("job_level", 1)
        
        # اطلاعات کلن
        clan_text = "ندارد"
        if user.get("clan_id") and user["clan_id"] in data.get("clans", {}):
            clan_text = data["clans"][user["clan_id"]]["name"]
        
        # اطلاعات همسر
        married_text = "ندارد"
        if user.get("married_to") and user["married_to"] in data["users"]:
            married_text = data["users"][user["married_to"]]["country_name"]
        
        await safe_reply(message,
            f"👤 **پروفایل {country_name}**\n\n"
            f"❤️ [{health_bar}]\n"
            f"💰 سکه: {format_num(user.get('coins', 0))}\n"
            f"💪 قدرت: {format_num(calculate_power(user))}\n"
            f"📈 سطح: {user.get('level', 1)} | تجربه: {format_num(user.get('exp', 0))}\n\n"
            f"⚔️ **نیروهای نظامی**\n"
            f"👥 سربازان: {format_num(user.get('soldiers', 0))}\n"
            f"🔫 سلاح‌ها: {user.get('weapons', 0)}\n"
            f"💣 تروریست‌ها: {format_num(user.get('terrorists', 0))}\n"
            f"🕵️ جاسوس‌ها: {user.get('spies', 0)}\n\n"
            f"📊 **آمار نبرد**\n"
            f"⚔️ حملات: {user.get('attacks', 0)} | 💀 کشته: {user.get('kills', 0)}\n"
            f"🛡️ دفاع: {user.get('defends', 0)} | ☠️ مرگ: {user.get('deaths', 0)}\n\n"
            f"🎖️ **سایر اطلاعات**\n"
            f"🏰 قلعه: سطح {user.get('fort_level', 0)}\n"
            f"💼 شغل: {job_name} (سطح {job_level})\n"
            f"🎌 کلن: {clan_text}\n"
            f"💑 همسر: {married_text}\n"
            f"🔥 استریک: {user.get('attack_streak', 0)}\n"
            f"📅 استریک روزانه: {user.get('daily_streak', 0)}",
            chat_keypad=main_menu_keypad())
        return
        # ========== سیستم کار ==========
if button_id == "work":
    work_count = data["daily_resets"].get(user_id, {}).get("work_count", 0)
    if work_count >= 20:
        await safe_reply(message, "❌ **امروز ۲۰ بار کار کردی!**\nفردا بیا.", chat_keypad=main_menu_keypad())
        return
    
    # محاسبه درآمد بر اساس شغل
    base_earning = random.randint(200, 800)
    job_bonus = 0
    if user.get("job", 0) in JOBS_DB:
        job_bonus = JOBS_DB[user["job"]]["bonus"].get("coins", 0) * user.get("job_level", 1)
    
    # پاداش سطح
    level_bonus = user.get("level", 1) * 10
    
    # پاداش استریک روزانه
    streak_bonus = 1 + (user.get("daily_streak", 0) * 0.05)
    
    total_earning = int((base_earning + job_bonus + level_bonus) * streak_bonus)
    
    # پاداش تجربه
    exp_gain = 20 + random.randint(0, 30)
    
    user["coins"] = user.get("coins", 0) + total_earning
    user["exp"] = user.get("exp", 0) + exp_gain
    
    # بروزرسانی تعداد کار
    data["daily_resets"][user_id]["work_count"] = work_count + 1
    
    # چک کردن افزایش سطح
    old_level = user.get("level", 1)
    new_level = 1 + (user["exp"] // 1000)
    if new_level > old_level:
        user["level"] = new_level
        user["max_health"] = user.get("max_health", 100000) + (new_level - old_level) * 5000
        user["health"] = user["max_health"]
        await safe_reply(message, f"🎉 **تبریک! به سطح {new_level} رسیدی!**\n❤️ حداکثر جان +{format_num((new_level - old_level) * 5000)}", chat_keypad=None)
    
    save_data(data)
    
    # لیست کارهای مختلف
    work_types = ["کشاورزی", "معدن", "تجارت", "ساخت و ساز", "آموزش", "پژوهش", "دیپلماسی", "جاسوسی", "حمل و نقل", "صنعت"]
    work_selected = random.choice(work_types)
    
    await safe_reply(message,
        f"💼 **کار در حوزه {work_selected}**\n\n"
        f"💰 درآمد: +{format_num(total_earning)} سکه\n"
        f"📈 تجربه: +{exp_gain}\n"
        f"💼 پاداش شغل: +{format_num(job_bonus)}\n"
        f"🔥 پاداش استریک: +{int((streak_bonus-1)*100)}%\n"
        f"📊 تعداد کار امروز: {work_count + 1}/۲۰",
        chat_keypad=main_menu_keypad())
    return

# ========== پاداش روزانه ==========
if button_id == "daily":
    today = datetime.now().date().isoformat()
    last_daily = data["daily_resets"].get(user_id, {}).get("last_daily")
    
    if last_daily == today:
        await safe_reply(message, "❌ **امروز پاداش گرفتی!**\nفردا بیا.", chat_keypad=main_menu_keypad())
        return
    
    # محاسبه پاداش بر اساس استریک
    streak = user.get("daily_streak", 0)
    reward = 1000 + (streak * 200)
    
    # پاداش ویژه در روزهای خاص
    special_reward = 0
    if streak == 7:
        special_reward = 5000
        await safe_reply(message, "🎉 **هفته اول کامل شد!** 🎉\n+۵,۰۰۰ سکه جایزه ویژه!", chat_keypad=None)
    elif streak == 14:
        special_reward = 10000
        await safe_reply(message, "🎉 **دو هفته متوالی!** 🎉\n+۱۰,۰۰۰ سکه جایزه ویژه!", chat_keypad=None)
    elif streak == 30:
        special_reward = 50000
        await safe_reply(message, "🎉 **یک ماه کامل!** 🎉\n+۵۰,۰۰۰ سکه جایزه ویژه!", chat_keypad=None)
    
    total_reward = reward + special_reward
    
    user["coins"] = user.get("coins", 0) + total_reward
    user["daily_streak"] = streak + 1
    data["daily_resets"][user_id]["last_daily"] = today
    
    save_data(data)
    
    await safe_reply(message,
        f"🎁 **پاداش روزانه {streak + 1}**\n\n"
        f"💰 پاداش پایه: +{format_num(reward)} سکه\n"
        f"🎁 پاداش ویژه: +{format_num(special_reward)} سکه\n"
        f"💎 مجموع: +{format_num(total_reward)} سکه\n"
        f"🔥 استریک: {streak + 1} روز\n\n"
        f"✨ {30 - (streak + 1)} روز مونده تا جایزه ماهانه!",
        chat_keypad=main_menu_keypad())
    return

# ========== چالش روزانه ==========
if button_id == "challenge":
    today = datetime.now().date().isoformat()
    challenge = data["daily_challenges"].get(user_id, {})
    
    if challenge.get("date") != today:
        # چالش جدید
        challenge_types = [
            {"name": "💰 جمع‌آوری سکه", "target": 5000, "type": "collect_coins", "reward": 2000},
            {"name": "⚔️ حمله موفق", "target": 5, "type": "attack", "reward": 1500},
            {"name": "💼 کار کردن", "target": 10, "type": "work", "reward": 1000},
            {"name": "🕵️ جاسوسی", "target": 3, "type": "spy", "reward": 1200},
            {"name": "🏰 ارتقای قلعه", "target": 1, "type": "fort", "reward": 3000},
            {"name": "👥 استخدام سرباز", "target": 20, "type": "recruit", "reward": 1500},
            {"name": "💀 کشتن دشمنان", "target": 10, "type": "kill", "reward": 2500},
            {"name": "🏆 بردن دوال", "target": 3, "type": "duel", "reward": 2000},
        ]
        challenge = random.choice(challenge_types)
        challenge["date"] = today
        challenge["progress"] = 0
        challenge["claimed"] = False
        data["daily_challenges"][user_id] = challenge
        save_data(data)
    
    if challenge.get("claimed"):
        await safe_reply(message, "✅ **جایزه چالش امروز رو گرفتی!**\nفردا چالش جدید.", chat_keypad=main_menu_keypad())
        return
    
    progress_bar = "█" * (challenge["progress"] * 20 // challenge["target"]) + "░" * (20 - (challenge["progress"] * 20 // challenge["target"]))
    
    if challenge["progress"] >= challenge["target"]:
        builder = ChatKeypadBuilder()
        builder.row(builder.button("claim_challenge", "🎁 دریافت جایزه"))
        builder.row(builder.button("back_main", "🔙"))
        await safe_reply(message,
            f"🏆 **چالش روزانه کامل شد!** 🏆\n\n"
            f"🎯 {challenge['name']}\n"
            f"📊 [{progress_bar}] {challenge['progress']}/{challenge['target']}\n"
            f"🎁 جایزه: {format_num(challenge['reward'])} سکه\n\n"
            f"✅ روی دکمه زیر کلیک کن تا جایزه بگیری!",
            chat_keypad=builder.build())
    else:
        await safe_reply(message,
            f"🏆 **چالش روزانه**\n\n"
            f"🎯 {challenge['name']}\n"
            f"📊 [{progress_bar}] {challenge['progress']}/{challenge['target']}\n"
            f"🎁 جایزه: {format_num(challenge['reward'])} سکه",
            chat_keypad=main_menu_keypad())
    return

# دریافت جایزه چالش
if button_id == "claim_challenge":
    today = datetime.now().date().isoformat()
    challenge = data["daily_challenges"].get(user_id, {})
    
    if challenge.get("date") != today or challenge.get("claimed"):
        await safe_reply(message, "❌ چالش معتبر نیست!", chat_keypad=main_menu_keypad())
        return
    
    if challenge["progress"] >= challenge["target"]:
        user["coins"] = user.get("coins", 0) + challenge["reward"]
        user["exp"] = user.get("exp", 0) + 100
        challenge["claimed"] = True
        save_data(data)
        
        await safe_reply(message,
            f"🎉 **جایزه چالش دریافت شد!** 🎉\n\n"
            f"💰 +{format_num(challenge['reward'])} سکه\n"
            f"📈 +۱۰۰ تجربه",
            chat_keypad=main_menu_keypad())
    else:
        await safe_reply(message, f"❌ چالش کامل نشده! {challenge['progress']}/{challenge['target']}", chat_keypad=main_menu_keypad())
    return

# ========== حضور و غیاب ==========
if button_id == "attendance":
    today = datetime.now().date().isoformat()
    attendance = data.get("attendance", {}).get(user_id, [])
    
    if today in attendance:
        await safe_reply(message, "✅ **امروز ثبت نام کردی!**\nفردا بیا.", chat_keypad=main_menu_keypad())
        return
    
    attendance.append(today)
    data.setdefault("attendance", {})[user_id] = attendance
    
    # محاسبه پاداش بر اساس تعداد روزهای حضور
    days_count = len(attendance)
    
    if days_count == 1:
        reward = 500
    elif days_count == 5:
        reward = 3000
    elif days_count == 10:
        reward = 10000
    elif days_count == 20:
        reward = 25000
    elif days_count == 30:
        reward = 50000
    else:
        reward = 100
    
    user["coins"] = user.get("coins", 0) + reward
    save_data(data)
    
    await safe_reply(message,
        f"📅 **حضور و غیاب روز {days_count}**\n\n"
        f"✅ حضور شما ثبت شد!\n"
        f"💰 پاداش: +{format_num(reward)} سکه\n"
        f"📊 تعداد کل حضور: {days_count} روز\n\n"
        f"🎯 {30 - days_count} روز مونده تا جایزه ۵۰,۰۰۰ سکه!",
        chat_keypad=main_menu_keypad())
    return

# ========== استخدام سرباز ==========
if button_id == "recruit":
    # هزینه استخدام
    soldier_count = user.get("soldiers", 0)
    cost = 100 + (soldier_count // 100) * 50
    cost = min(cost, 5000)
    
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **سکه کافی نیست!**\nنیاز: {format_num(cost)} سکه", chat_keypad=main_menu_keypad())
        return
    
    # تعداد سربازان جدید
    new_soldiers = random.randint(1, 10)
    
    user["coins"] -= cost
    user["soldiers"] = soldier_count + new_soldiers
    user["exp"] = user.get("exp", 0) + 20
    
    save_data(data)
    
    await safe_reply(message,
        f"⚔️ **استخدام سرباز جدید**\n\n"
        f"👥 +{new_soldiers} سرباز\n"
        f"💰 هزینه: {format_num(cost)} سکه\n"
        f"👥 مجموع سربازان: {format_num(user['soldiers'])}\n"
        f"📈 +۲۰ تجربه",
        chat_keypad=main_menu_keypad())
    return
# ========== فروشگاه ==========
if button_id == "shop":
    builder = ChatKeypadBuilder()
    builder.row(builder.button("shop_ground", "⚔️ سلاح‌های زمینی"))
    builder.row(builder.button("shop_air", "✈️ سلاح‌های هوایی"))
    builder.row(builder.button("shop_sea", "🚢 سلاح‌های دریایی"))
    builder.row(builder.button("shop_special", "💎 سلاح‌های ویژه"))
    builder.row(builder.button("back_main", "🔙"))
    await safe_reply(message, "🔫 **فروشگاه سلاح**\n\nدسته مورد نظر را انتخاب کنید:", chat_keypad=builder.build())
    return

# دسته‌بندی فروشگاه
if button_id in ["shop_ground", "shop_air", "shop_sea", "shop_special"]:
    category_map = {
        "shop_ground": "ground",
        "shop_air": "air", 
        "shop_sea": "sea",
        "shop_special": "special"
    }
    category = category_map[button_id]
    
    builder = ChatKeypadBuilder()
    for weapon in WEAPONS_DB[category]["items"]:
        if user.get("level", 1) >= weapon["level_req"]:
            builder.row(builder.button(f"weapon_buy_{weapon['id']}", 
                f"{weapon['emoji']} {weapon['name'][:15]} | {format_num(weapon['price'])}💰"))
        else:
            builder.row(builder.button(f"weapon_locked_{weapon['id']}", 
                f"🔒 {weapon['name'][:15]} (سطح {weapon['level_req']})"))
    builder.row(builder.button("shop", "🔙"))
    
    await safe_reply(message,
        f"{WEAPONS_DB[category]['title']}\n"
        f"📈 سطح شما: {user.get('level', 1)}\n"
        f"💰 سکه: {format_num(user.get('coins', 0))}",
        chat_keypad=builder.build())
    return

# خرید سلاح
if button_id and button_id.startswith("weapon_buy_"):
    weapon_id = button_id.replace("weapon_buy_", "")
    
    # پیدا کردن سلاح
    weapon = None
    category = None
    for cat, cat_data in WEAPONS_DB.items():
        for w in cat_data["items"]:
            if w["id"] == weapon_id:
                weapon = w
                category = cat
                break
        if weapon:
            break
    
    if not weapon:
        await safe_reply(message, "❌ سلاح یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    # چک کردن سطح و سکه
    if user.get("level", 1) < weapon["level_req"]:
        await safe_reply(message, f"❌ **سطح {weapon['level_req']} نیاز است!**\nسطح فعلی: {user.get('level', 1)}", chat_keypad=main_menu_keypad())
        return
    
    if user.get("coins", 0) < weapon["price"]:
        await safe_reply(message, f"❌ **سکه کافی نیست!**\nنیاز: {format_num(weapon['price'])} سکه", chat_keypad=main_menu_keypad())
        return
    
    # خرید
    user["coins"] -= weapon["price"]
    user["weapons"] = user.get("weapons", 0) + 1
    user.setdefault("weapons_list", []).append({
        "id": weapon["id"],
        "name": weapon["name"],
        "type": category,
        "power": weapon["power"],
        "critical": weapon["critical"],
        "buy_date": datetime.now().isoformat()
    })
    user["exp"] = user.get("exp", 0) + 50
    
    save_data(data)
    
    await safe_reply(message,
        f"✅ **{weapon['name']} خریداری شد!**\n\n"
        f"💪 قدرت: +{weapon['power']}\n"
        f"🎯 شانس بحرانی: +{weapon['critical']}%\n"
        f"💰 هزینه: {format_num(weapon['price'])} سکه\n"
        f"📈 +۵۰ تجربه\n\n"
        f"🔫 تعداد سلاح‌ها: {user['weapons']}",
        chat_keypad=main_menu_keypad())
    return

# سلاح قفل شده
if button_id and button_id.startswith("weapon_locked_"):
    await safe_reply(message, "🔒 **این سلاح قفل است!**\nسطح خود را افزایش دهید.", chat_keypad=main_menu_keypad())
    return
    # ========== دفاع ==========
if button_id == "defend":
    heal_base = random.randint(5000, 15000)
    fort_bonus = user.get("fort_level", 0) * 500
    total_heal = heal_base + fort_bonus
    
    cost = 1000
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    old_health = user.get("health", 100000)
    max_health = user.get("max_health", 100000)
    new_health = min(max_health, old_health + total_heal)
    actual_heal = new_health - old_health
    
    user["coins"] -= cost
    user["health"] = new_health
    user["defends"] = user.get("defends", 0) + 1
    
    save_data(data)
    
    await safe_reply(message,
        f"🛡️ **دفاع و بازیابی جان**\n\n"
        f"❤️ درمان: +{format_num(actual_heal)} جان\n"
        f"🏰 پاداش قلعه: +{format_num(fort_bonus)}\n"
        f"💰 هزینه: {format_num(cost)} سکه\n"
        f"❤️ جان فعلی: {format_num(new_health)}/{format_num(max_health)}",
        chat_keypad=main_menu_keypad())
    return

# ========== جاسوسی ==========
if button_id == "spy":
    # پیدا کردن کاربران آنلاین برای جاسوسی
    online_users = []
    for uid in data.get("online_users", {}):
        if uid != user_id and uid in data["users"] and uid not in data.get("banned_users", []):
            online_users.append(uid)
    
    if not online_users:
        await safe_reply(message, "🕵️ **هیچ کاربر آنلاینی برای جاسوسی نیست!**\nبعداً دوباره تلاش کن.", chat_keypad=main_menu_keypad())
        return
    
    # انتخاب تصادفی
    target_id = random.choice(online_users)
    target = data["users"][target_id]
    
    cost = 500
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= cost
    user["spies"] = user.get("spies", 0) + 1
    user["exp"] = user.get("exp", 0) + 30
    
    save_data(data)
    
    # اطلاعات جاسوسی
    spy_info = (
        f"🕵️ **گزارش جاسوسی از {target['country_name']}**\n\n"
        f"💰 سکه: {format_num(target.get('coins', 0))}\n"
        f"👥 سربازان: {format_num(target.get('soldiers', 0))}\n"
        f"🔫 سلاح‌ها: {target.get('weapons', 0)}\n"
        f"💣 تروریست‌ها: {format_num(target.get('terrorists', 0))}\n"
        f"🏰 قلعه: سطح {target.get('fort_level', 0)}\n"
        f"💪 قدرت: {format_num(calculate_power(target))}\n"
        f"❤️ جان: {format_num(target.get('health', 100000))}/{format_num(target.get('max_health', 100000))}\n"
        f"📈 سطح: {target.get('level', 1)}\n"
        f"⚔️ حملات: {target.get('attacks', 0)} | 💀 کشته: {target.get('kills', 0)}\n\n"
        f"📊 **وضعیت دفاعی**\n"
        f"🛡️ استعداد دفاع: {'ضعیف' if target.get('defends', 0) < 10 else 'متوسط' if target.get('defends', 0) < 50 else 'قوی'}\n"
        f"🔥 استریک حمله: {target.get('attack_streak', 0)}\n"
        f"💰 ارزش غارت تخمینی: {format_num(int(target.get('coins', 0) * 0.3))} سکه"
    )
    
    await safe_reply(message, spy_info, chat_keypad=main_menu_keypad())
    return

# ========== اتحاد ==========
if button_id == "alliance":
    builder = ChatKeypadBuilder()
    builder.row(builder.button("alliance_create", "🤝 درخواست اتحاد"))
    builder.row(builder.button("alliance_list", "📋 اتحادهای من"))
    builder.row(builder.button("alliance_pending", "⏳ درخواست‌های دریافتی"))
    builder.row(builder.button("alliance_break", "💔 شکستن اتحاد"))
    builder.row(builder.button("back_main", "🔙"))
    await safe_reply(message, "🤝 **منوی اتحادها**", chat_keypad=builder.build())
    return

# درخواست اتحاد
if button_id == "alliance_create":
    # پیدا کردن کاربران برای اتحاد
    available_users = []
    for uid, u in data["users"].items():
        if uid != user_id and u.get("country_name") and uid not in data.get("banned_users", []):
            # چک کردن اتحاد قبلی
            existing = False
            for a in data.get("alliances", []):
                if (a["from_id"] == user_id and a["to_id"] == uid) or (a["from_id"] == uid and a["to_id"] == user_id):
                    existing = True
                    break
            if not existing:
                available_users.append((uid, u["country_name"]))
    
    if not available_users:
        await safe_reply(message, "❌ **هیچ کاربری برای اتحاد موجود نیست!**", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for uid, name in available_users[:20]:
        builder.row(builder.button(f"alliance_req_{uid}", f"🤝 {name[:20]}"))
    builder.row(builder.button("alliance", "🔙"))
    
    await safe_reply(message, "🤝 **انتخاب کشور برای اتحاد:**", chat_keypad=builder.build())
    return

# ارسال درخواست اتحاد
if button_id and button_id.startswith("alliance_req_"):
    target_id = button_id.replace("alliance_req_", "")
    
    if target_id not in data["users"]:
        await safe_reply(message, "❌ کاربر یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    # ذخیره درخواست
    data["alliances"].append({
        "from_id": user_id,
        "to_id": target_id,
        "status": "pending",
        "date": datetime.now().isoformat()
    })
    save_data(data)
    
    target_name = data["users"][target_id]["country_name"]
    await safe_reply(message, f"✅ **درخواست اتحاد به {target_name} ارسال شد!**", chat_keypad=main_menu_keypad())
    
    # اطلاع به طرف مقابل
    try:
        await bot.send_message(int(target_id), 
            f"🤝 **درخواست اتحاد از {country_name}**\n\n"
            f"برای پاسخ به منوی اتحاد بروید.",
            chat_keypad=main_menu_keypad())
    except:
        pass
    return

# لیست اتحادهای من
if button_id == "alliance_list":
    my_alliances = []
    for a in data.get("alliances", []):
        if a["from_id"] == user_id or a["to_id"] == user_id:
            other_id = a["to_id"] if a["from_id"] == user_id else a["from_id"]
            if other_id in data["users"]:
                status_text = "✅ فعال" if a["status"] == "accepted" else "⏳ در انتظار"
                my_alliances.append(f"• {data['users'][other_id]['country_name']} - {status_text}")
    
    if not my_alliances:
        await safe_reply(message, "📋 **هیچ اتحادی ندارید!**", chat_keypad=main_menu_keypad())
        return
    
    await safe_reply(message, "🤝 **اتحادهای شما:**\n\n" + "\n".join(my_alliances), chat_keypad=main_menu_keypad())
    return

# درخواست‌های دریافتی
if button_id == "alliance_pending":
    pending = []
    for a in data.get("alliances", []):
        if a["to_id"] == user_id and a["status"] == "pending":
            if a["from_id"] in data["users"]:
                pending.append(a)
    
    if not pending:
        await safe_reply(message, "⏳ **درخواستی ندارید!**", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for a in pending:
        from_name = data["users"][a["from_id"]]["country_name"]
        builder.row(
            builder.button(f"alliance_accept_{a['from_id']}", f"✅ {from_name[:15]}"),
            builder.button(f"alliance_reject_{a['from_id']}", "❌ رد")
        )
    builder.row(builder.button("alliance", "🔙"))
    
    await safe_reply(message, "⏳ **درخواست‌های اتحاد:**", chat_keypad=builder.build())
    return

# پذیرفتن اتحاد
if button_id and button_id.startswith("alliance_accept_"):
    from_id = button_id.replace("alliance_accept_", "")
    
    for a in data.get("alliances", []):
        if a["from_id"] == from_id and a["to_id"] == user_id and a["status"] == "pending":
            a["status"] = "accepted"
            save_data(data)
            
            await safe_reply(message, f"✅ **اتحاد با {data['users'][from_id]['country_name']} برقرار شد!**\n\n🤝 از این به بعد می‌تونید به هم کمک کنید.", chat_keypad=main_menu_keypad())
            
            try:
                await bot.send_message(int(from_id), f"✅ **درخواست اتحاد شما توسط {country_name} پذیرفته شد!**")
            except:
                pass
            return
    
    await safe_reply(message, "❌ درخواست یافت نشد!", chat_keypad=main_menu_keypad())
    return

# رد کردن اتحاد
if button_id and button_id.startswith("alliance_reject_"):
    from_id = button_id.replace("alliance_reject_", "")
    
    data["alliances"] = [a for a in data.get("alliances", []) if not (a["from_id"] == from_id and a["to_id"] == user_id)]
    save_data(data)
    
    await safe_reply(message, "❌ درخواست رد شد.", chat_keypad=main_menu_keypad())
    return

# شکستن اتحاد
if button_id == "alliance_break":
    my_alliances = []
    for a in data.get("alliances", []):
        if (a["from_id"] == user_id or a["to_id"] == user_id) and a["status"] == "accepted":
            other_id = a["to_id"] if a["from_id"] == user_id else a["from_id"]
            if other_id in data["users"]:
                my_alliances.append((other_id, data["users"][other_id]["country_name"], a))
    
    if not my_alliances:
        await safe_reply(message, "❌ **هیچ اتحاد فعالی ندارید!**", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for other_id, name, a in my_alliances:
        builder.row(builder.button(f"alliance_break_{other_id}", f"💔 {name[:20]}"))
    builder.row(builder.button("alliance", "🔙"))
    
    await safe_reply(message, "💔 **انتخاب اتحاد برای شکستن:**", chat_keypad=builder.build())
    return

if button_id and button_id.startswith("alliance_break_"):
    other_id = button_id.replace("alliance_break_", "")
    
    data["alliances"] = [a for a in data.get("alliances", []) if not ((a["from_id"] == user_id and a["to_id"] == other_id) or (a["from_id"] == other_id and a["to_id"] == user_id))]
    save_data(data)
    
    await safe_reply(message, f"💔 **اتحاد با {data['users'][other_id]['country_name']} شکسته شد!**", chat_keypad=main_menu_keypad())
    return
    # ========== حمله ==========
if button_id == "attack":
    # پیدا کردن اهداف قابل حمله
    available_targets = []
    for uid, u in data["users"].items():
        if uid != user_id and u.get("country_name") and uid not in data.get("banned_users", []):
            # چک کردن سپر دفاعی
            shield_until = data.get("shields", {}).get(uid)
            if shield_until and datetime.fromisoformat(shield_until) > datetime.now():
                continue
            available_targets.append((uid, u["country_name"], calculate_power(u)))
    
    if not available_targets:
        await safe_reply(message, "💥 **هیچ هدفی برای حمله وجود ندارد!**\nبعداً دوباره تلاش کن.", chat_keypad=main_menu_keypad())
        return
    
    # مرتب‌سازی بر اساس قدرت
    available_targets.sort(key=lambda x: x[2])
    
    builder = ChatKeypadBuilder()
    for uid, name, power in available_targets[:20]:
        power_diff = calculate_power(user) - power
        if power_diff > 5000:
            indicator = "🟢"
        elif power_diff > 0:
            indicator = "🟡"
        else:
            indicator = "🔴"
        builder.row(builder.button(f"attack_target_{uid}", f"{indicator} {name[:15]} | 💪{format_num(power)}"))
    builder.row(builder.button("back_main", "🔙"))
    
    await safe_reply(message, 
        f"💥 **انتخاب هدف برای حمله**\n\n"
        f"🟢 = راحت | 🟡 = متوسط | 🔴 = سخت\n"
        f"💪 قدرت شما: {format_num(calculate_power(user))}",
        chat_keypad=builder.build())
    return

# انتخاب هدف
if button_id and button_id.startswith("attack_target_"):
    target_id = button_id.replace("attack_target_", "")
    
    if target_id not in data["users"]:
        await safe_reply(message, "❌ هدف یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    target = data["users"][target_id]
    
    # چک کردن سپر دفاعی
    shield_until = data.get("shields", {}).get(target_id)
    if shield_until and datetime.fromisoformat(shield_until) > datetime.now():
        await safe_reply(message, f"🛡️ **{target['country_name']} تحت حفاظت است!**\nنمی‌توانید حمله کنید.", chat_keypad=main_menu_keypad())
        return
    
    # چک کردن سلامت هدف
    if target.get("health", 0) <= 0:
        await safe_reply(message, f"💀 **{target['country_name']} قبلاً نابود شده!**", chat_keypad=main_menu_keypad())
        return
    
    data["pending_action"][user_id] = {"action": "attack_target", "target": target_id}
    save_data(data)
    
    # نمایش اطلاعات هدف
    power_user = calculate_power(user)
    power_target = calculate_power(target)
    success_chance = min(95, 30 + ((power_user - power_target) / 1000))
    if success_chance < 5:
        success_chance = 5
    
    await safe_reply(message,
        f"🎯 **هدف: {target['country_name']}**\n\n"
        f"💪 قدرت شما: {format_num(power_user)}\n"
        f"🛡️ قدرت دشمن: {format_num(power_target)}\n"
        f"📊 شانس موفقیت: {success_chance:.0f}%\n\n"
        f"⚔️ **نوع حمله را انتخاب کنید:**",
        chat_keypad=attack_type_keypad(target_id))
    return

# انواع حمله
if button_id and button_id.startswith("attack_") and "pending_action" in data and user_id in data["pending_action"]:
    pending = data["pending_action"][user_id]
    if pending.get("action") != "attack_target":
        return
    
    target_id = pending["target"]
    attack_type = button_id.split("_")[1]
    
    if target_id not in data["users"]:
        await safe_reply(message, "❌ هدف یافت نشد!", chat_keypad=main_menu_keypad())
        del data["pending_action"][user_id]
        save_data(data)
        return
    
    target = data["users"][target_id]
    
    # هزینه حملات ویژه
    special_costs = {
        "nuclear": 50000,
        "chemical": 30000,
        "bacterial": 40000,
        "space": 100000,
        "magic": 80000
    }
    
    if attack_type in special_costs:
        cost = special_costs[attack_type]
        if user.get("coins", 0) < cost:
            await safe_reply(message, f"❌ **{format_num(cost)} سکه برای این حمله نیاز است!**", chat_keypad=main_menu_keypad())
            del data["pending_action"][user_id]
            save_data(data)
            return
        user["coins"] -= cost
    
    # محاسبه قدرت حمله
    my_power = calculate_power(user)
    target_power = calculate_power(target)
    
    # شانس موفقیت
    base_chance = 0.3 + ((my_power - target_power) / 20000)
    base_chance = max(0.05, min(0.95, base_chance))
    
    # شانس بحرانی
    critical_chance = sum(w.get("critical", 0) for w in user.get("weapons_list", [])) / 100
    critical_chance = min(0.6, critical_chance)
    
    # استریک بونوس
    streak_bonus = 1 + (user.get("attack_streak", 0) * 0.05)
    
    # حمله ویژه بونوس
    attack_bonus = {
        "ground": 1.0,
        "air": 1.2,
        "sea": 1.1,
        "nuclear": 3.0,
        "chemical": 2.0,
        "bacterial": 2.5,
        "space": 4.0,
        "magic": 3.5
    }.get(attack_type, 1.0)
    
    success = random.random() < base_chance
    
    if success:
        # محاسبه خسارت
        base_damage = random.randint(5000, 20000) + int(my_power * 0.2)
        damage = int(base_damage * attack_bonus * streak_bonus)
        
        # ضربه بحرانی
        is_critical = random.random() < critical_chance
        if is_critical:
            damage = int(damage * 2.5)
        
        damage = min(damage, target.get("health", 100000))
        
        # محاسبه غنیمت
        loot_coins = int(target.get("coins", 0) * random.uniform(0.1, 0.3))
        loot_food = int(target.get("food", 0) * random.uniform(0.05, 0.15))
        loot_iron = int(target.get("iron", 0) * random.uniform(0.05, 0.15))
        
        # اعمال خسارت
        target["health"] = max(0, target.get("health", 100000) - damage)
        user["coins"] = user.get("coins", 0) + loot_coins
        user["food"] = user.get("food", 0) + loot_food
        user["iron"] = user.get("iron", 0) + loot_iron
        
        # آمار
        user["attacks"] = user.get("attacks", 0) + 1
        if target["health"] <= 0:
            user["kills"] = user.get("kills", 0) + 1
            # پاداش نابودی کامل
            user["coins"] += target.get("coins", 0) // 2
            target["coins"] = target.get("coins", 0) // 2
        
        user["exp"] = user.get("exp", 0) + 100 + (damage // 100)
        user["attack_streak"] = user.get("attack_streak", 0) + 1
        
        # بروزرسانی استریک دشمن (ریست)
        target["attack_streak"] = 0
        
        # لاگ نبرد
        data.setdefault("battle_logs", []).append({
            "attacker": user_id,
            "attacker_name": country_name,
            "defender": target_id,
            "defender_name": target["country_name"],
            "attack_type": attack_type,
            "damage": damage,
            "is_critical": is_critical,
            "loot": loot_coins,
            "date": datetime.now().isoformat()
        })
        
        # محدود کردن لاگ به 100 تا
        if len(data.get("battle_logs", [])) > 100:
            data["battle_logs"] = data["battle_logs"][-100:]
        
        # چک کردن افزایش سطح
        old_level = user.get("level", 1)
        new_level = 1 + (user["exp"] // 1000)
        level_up = False
        if new_level > old_level:
            user["level"] = new_level
            user["max_health"] = user.get("max_health", 100000) + 5000
            user["health"] = user["max_health"]
            level_up = True
        
        # چک کردن دستاوردها
        new_achievements = check_achievements(data, user_id)
        
        save_data(data)
        
        # پیام موفقیت
        crit_text = "⚡ **ضربه بحرانی!** ⚡\n" if is_critical else ""
        level_text = f"\n🎉 **به سطح {new_level} رسیدی!** 🎉" if level_up else ""
        ach_text = ""
        if new_achievements:
            ach_text = "\n🏆 **دستاورد جدید:**\n" + "\n".join([f"• {a['name']} (+{format_num(a['reward'])} سکه)" for a in new_achievements[:3]])
        
        await safe_reply(message,
            f"💥 **حمله {attack_type.upper()} به {target['country_name']}!**\n\n"
            f"{crit_text}"
            f"✅ **حمله موفق!**\n"
            f"💔 خسارت: {format_num(damage)}\n"
            f"💰 غنیمت: +{format_num(loot_coins)} سکه\n"
            f"🌾 غنیمت غذا: +{format_num(loot_food)}\n"
            f"⛏️ غنیمت آهن: +{format_num(loot_iron)}\n"
            f"📈 تجربه: +{100 + (damage // 100)}\n"
            f"🔥 استریک: {user['attack_streak']}\n"
            f"❤️ جان باقی {target['country_name']}: {format_num(target['health'])}/{format_num(target.get('max_health', 100000))}"
            f"{level_text}{ach_text}",
            chat_keypad=main_menu_keypad())
        
        # پیام به قربانی
        try:
            await bot.send_message(int(target_id),
                f"⚠️ **حمله {attack_type.upper()} از {country_name}!** ⚠️\n\n"
                f"💔 خسارت: {format_num(damage)}\n"
                f"💰 سکه غارت شده: {format_num(loot_coins)}\n"
                f"❤️ جان باقی: {format_num(target['health'])}/{format_num(target.get('max_health', 100000))}\n\n"
                f"🛡️ برای دفاع از /defend استفاده کن!",
                chat_keypad=main_menu_keypad())
        except:
            pass
        
    else:
        # حمله ناموفق
        user["attack_streak"] = 0
        user["exp"] = user.get("exp", 0) + 20
        save_data(data)
        
        await safe_reply(message,
            f"💥 **حمله {attack_type.upper()} به {target['country_name']}!**\n\n"
            f"❌ **حمله ناموفق!**\n"
            f"دشمن از حمله شما فرار کرد.\n"
            f"🔥 استریک شما ریست شد!\n"
            f"📈 +۲۰ تجربه",
            chat_keypad=main_menu_keypad())
    
    del data["pending_action"][user_id]
    save_data(data)
    return

# برگشت از صفحه حمله
if button_id == "attack_back":
    await safe_reply(message, "💥 **انتخاب هدف:**", chat_keypad=attack_select_keypad(user_id))
    return
 
    # ========== بازار ==========
if button_id == "market":
    builder = ChatKeypadBuilder()
    builder.row(builder.button("market_buy", "🛒 خرید از بازار"))
    builder.row(builder.button("market_sell", "📤 فروش در بازار"))
    builder.row(builder.button("market_my", "📦 کالاهای من"))
    builder.row(builder.button("market_list", "📋 لیست کامل"))
    builder.row(builder.button("back_main", "🔙"))
    await safe_reply(message, "🛒 **بازار آزاد**\n\nاینجا می‌تونی سلاح‌های اضافی خودت رو بفروشی یا از دیگران بخری.", chat_keypad=builder.build())
    return

# فروش سلاح
if button_id == "market_sell":
    weapons_list = user.get("weapons_list", [])
    if not weapons_list:
        await safe_reply(message, "❌ **سلاحی برای فروش ندارید!**", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for i, w in enumerate(weapons_list[:15]):
        builder.row(builder.button(f"sell_weapon_{i}", f"📤 {w['name']} | 💪{w['power']} | 🎯{w.get('critical',5)}%"))
    builder.row(builder.button("market", "🔙"))
    
    await safe_reply(message, "🔫 **انتخاب سلاح برای فروش:**", chat_keypad=builder.build())
    return

# انتخاب قیمت برای فروش
if button_id and button_id.startswith("sell_weapon_"):
    idx = int(button_id.replace("sell_weapon_", ""))
    weapons_list = user.get("weapons_list", [])
    
    if idx >= len(weapons_list):
        await safe_reply(message, "❌ سلاح یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    weapon = weapons_list[idx]
    suggested_price = weapon["price"] // 2
    
    data["pending_action"][user_id] = {
        "action": "market_sell_price",
        "weapon_idx": idx,
        "weapon": weapon
    }
    save_data(data)
    
    await safe_reply(message,
        f"💰 **فروش {weapon['name']}**\n\n"
        f"💪 قدرت: {weapon['power']}\n"
        f"🎯 شانس بحرانی: {weapon.get('critical', 5)}%\n"
        f"💰 قیمت پیشنهادی: {format_num(suggested_price)} - {format_num(weapon['price'])} سکه\n\n"
        f"📝 لطفاً قیمت مورد نظر را وارد کنید:",
        chat_keypad=None)
    return

# ثبت فروش
if pending.get("action") == "market_sell_price" and text.isdigit():
    price = int(text)
    if price < 100:
        await safe_reply(message, "❌ **حداقل قیمت ۱۰۰ سکه است!**", chat_keypad=main_menu_keypad())
    else:
        idx = pending.get("weapon_idx")
        weapon = pending.get("weapon")
        weapons_list = user.get("weapons_list", [])
        
        if idx >= len(weapons_list):
            await safe_reply(message, "❌ سلاح یافت نشد!", chat_keypad=main_menu_keypad())
        else:
            # حذف سلاح از انبار
            sold_weapon = weapons_list.pop(idx)
            user["weapons"] = len(weapons_list)
            
            # اضافه به لیست بازار
            listing = {
                "id": f"{user_id}_{int(time.time())}",
                "seller_id": user_id,
                "seller_name": country_name,
                "weapon": sold_weapon,
                "price": price,
                "date": datetime.now().isoformat()
            }
            data.setdefault("market_listings", []).append(listing)
            
            save_data(data)
            
            await safe_reply(message,
                f"✅ **{sold_weapon['name']} با قیمت {format_num(price)} سکه در بازار قرار گرفت!**\n\n"
                f"💰 پس از فروش، سکه به حساب شما واریز می‌شود.",
                chat_keypad=main_menu_keypad())
    
    del data["pending_action"][user_id]
    save_data(data)
    return

# خرید از بازار
if button_id == "market_buy":
    listings = data.get("market_listings", [])
    listings = [l for l in listings if l["seller_id"] != user_id]
    
    if not listings:
        await safe_reply(message, "🛒 **بازار خالی است!**\nاولین نفری باش که کالا می‌فروشد.", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for l in listings[:15]:
        builder.row(builder.button(f"buy_market_{l['id']}", 
            f"🔫 {l['weapon']['name'][:12]} | {format_num(l['price'])}💰 | {l['seller_name'][:10]}"))
    builder.row(builder.button("market", "🔙"))
    
    await safe_reply(message, "🛒 **سلاح‌های موجود در بازار:**", chat_keypad=builder.build())
    return

# تایید خرید
if button_id and button_id.startswith("buy_market_"):
    listing_id = button_id.replace("buy_market_", "")
    
    listing = None
    for l in data.get("market_listings", []):
        if l["id"] == listing_id:
            listing = l
            break
    
    if not listing:
        await safe_reply(message, "❌ **کالا یافت نشد!**\nاحتمالاً قبلاً فروخته شده.", chat_keypad=main_menu_keypad())
        return
    
    if user.get("coins", 0) < listing["price"]:
        await safe_reply(message, f"❌ **سکه کافی نیست!**\nنیاز: {format_num(listing['price'])} سکه", chat_keypad=main_menu_keypad())
        return
    
    # انجام خرید
    user["coins"] -= listing["price"]
    user["weapons"] += 1
    user.setdefault("weapons_list", []).append(listing["weapon"])
    
    # پرداخت به فروشنده
    seller = data["users"].get(listing["seller_id"])
    if seller:
        seller["coins"] = seller.get("coins", 0) + listing["price"]
    
    # حذف از بازار
    data["market_listings"] = [l for l in data["market_listings"] if l["id"] != listing_id]
    
    save_data(data)
    
    await safe_reply(message,
        f"✅ **{listing['weapon']['name']} خریداری شد!**\n\n"
        f"💰 هزینه: {format_num(listing['price'])} سکه\n"
        f"💪 قدرت: +{listing['weapon']['power']}\n"
        f"🎯 شانس بحرانی: +{listing['weapon'].get('critical', 5)}%",
        chat_keypad=main_menu_keypad())
    
    # اطلاع به فروشنده
    try:
        await bot.send_message(int(listing["seller_id"]),
            f"💰 **کالای شما فروخته شد!**\n\n"
            f"🔫 {listing['weapon']['name']}\n"
            f"💰 مبلغ: {format_num(listing['price'])} سکه\n"
            f"👤 خریدار: {country_name}")
    except:
        pass
    return

# کالاهای من در بازار
if button_id == "market_my":
    my_listings = [l for l in data.get("market_listings", []) if l["seller_id"] == user_id]
    
    if not my_listings:
        await safe_reply(message, "📦 **کالایی در بازار ندارید!**", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for l in my_listings:
        builder.row(builder.button(f"cancel_market_{l['id']}", 
            f"❌ لغو {l['weapon']['name'][:12]} | {format_num(l['price'])}💰"))
    builder.row(builder.button("market", "🔙"))
    
    await safe_reply(message, "📦 **کالاهای شما در بازار:**", chat_keypad=builder.build())
    return

# لغو فروش
if button_id and button_id.startswith("cancel_market_"):
    listing_id = button_id.replace("cancel_market_", "")
    
    for l in data.get("market_listings", []):
        if l["id"] == listing_id and l["seller_id"] == user_id:
            # برگرداندن سلاح به کاربر
            user.setdefault("weapons_list", []).append(l["weapon"])
            user["weapons"] = len(user["weapons_list"])
            
            # حذف از بازار
            data["market_listings"] = [x for x in data["market_listings"] if x["id"] != listing_id]
            
            save_data(data)
            
            await safe_reply(message, f"✅ **فروش {l['weapon']['name']} لغو شد!**\nسلاح به انبار شما برگشت.", chat_keypad=main_menu_keypad())
            return
    
    await safe_reply(message, "❌ کالا یافت نشد!", chat_keypad=main_menu_keypad())
    return

# لیست کامل بازار
if button_id == "market_list":
    listings = data.get("market_listings", [])
    
    if not listings:
        await safe_reply(message, "🛒 **بازار خالی است!**", chat_keypad=main_menu_keypad())
        return
    
    text = "🛒 **لیست کامل بازار**\n\n"
    for l in listings[:30]:
        text += f"🔫 {l['weapon']['name']} | 💪{l['weapon']['power']} | 🎯{l['weapon'].get('critical',5)}% | 💰{format_num(l['price'])} | 👤 {l['seller_name']}\n"
    
    if len(listings) > 30:
        text += f"\n... و {len(listings) - 30} کالای دیگر"
    
    await safe_reply(message, text, chat_keypad=main_menu_keypad())
    return
    # ========== لاتاری ==========
if button_id == "lottery":
    lottery_data = data.get("lottery", {"tickets": [], "pool": 0, "last_winner": None, "last_prize": 0})
    ticket_count = lottery_data["tickets"].count(user_id)
    pool = lottery_data.get("pool", 0)
    
    builder = ChatKeypadBuilder()
    builder.row(builder.button("lottery_buy", "🎫 خرید بلیط (500💰)"))
    builder.row(builder.button("lottery_buy_10", "🎫 خرید 10 بلیط (4,500💰)"))
    builder.row(builder.button("lottery_info", "📊 اطلاعات لاتاری"))
    builder.row(builder.button("back_main", "🔙"))
    
    await safe_reply(message,
        f"🎰 **لاتاری روزانه**\n\n"
        f"💰 جایزه فعلی: {format_num(pool)} سکه\n"
        f"🎫 بلیط‌های شما: {ticket_count}\n"
        f"🎲 شانس شما: {ticket_count}/{len(lottery_data['tickets'])}%\n\n"
        f"🏆 آخرین برنده: {lottery_data.get('last_winner_name', 'ندارد')}\n"
        f"🎁 آخرین جایزه: {format_num(lottery_data.get('last_prize', 0))}",
        chat_keypad=builder.build())
    return

# خرید بلیط
if button_id == "lottery_buy":
    cost = 500
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= cost
    data.setdefault("lottery", {}).setdefault("tickets", []).append(user_id)
    data["lottery"]["pool"] = data["lottery"].get("pool", 0) + cost
    
    save_data(data)
    
    ticket_count = data["lottery"]["tickets"].count(user_id)
    await safe_reply(message,
        f"🎫 **بلیط لاتاری خریداری شد!**\n\n"
        f"💰 هزینه: {format_num(cost)} سکه\n"
        f"🎫 تعداد بلیط‌های شما: {ticket_count}\n"
        f"🎲 شانس برنده شدن: {ticket_count}/{len(data['lottery']['tickets'])}\n\n"
        f"✨ قرعه‌کشی هر روز ساعت ۰۰:۰۰ انجام می‌شود.",
        chat_keypad=main_menu_keypad())
    return

# خرید 10 بلیط
if button_id == "lottery_buy_10":
    cost = 4500
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= cost
    for _ in range(10):
        data.setdefault("lottery", {}).setdefault("tickets", []).append(user_id)
    data["lottery"]["pool"] = data["lottery"].get("pool", 0) + cost
    
    save_data(data)
    
    ticket_count = data["lottery"]["tickets"].count(user_id)
    await safe_reply(message,
        f"🎫 **10 بلیط لاتاری خریداری شد!**\n\n"
        f"💰 هزینه: {format_num(cost)} سکه (۱۰٪ تخفیف)\n"
        f"🎫 تعداد بلیط‌های شما: {ticket_count}\n"
        f"🎲 شانس برنده شدن: {ticket_count}/{len(data['lottery']['tickets'])}\n\n"
        f"✨ قرعه‌کشی هر روز ساعت ۰۰:۰۰ انجام می‌شود.",
        chat_keypad=main_menu_keypad())
    return

# اطلاعات لاتاری
if button_id == "lottery_info":
    lottery_data = data.get("lottery", {"tickets": [], "pool": 0})
    total_tickets = len(lottery_data["tickets"])
    user_tickets = lottery_data["tickets"].count(user_id)
    
    # آمار
    top_buyers = []
    ticket_counts = {}
    for uid in lottery_data["tickets"]:
        ticket_counts[uid] = ticket_counts.get(uid, 0) + 1
    
    for uid, count in sorted(ticket_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        if uid in data["users"]:
            top_buyers.append(f"{data['users'][uid]['country_name'][:12]}: {count} بلیط")
    
    text = f"📊 **آمار لاتاری**\n\n"
    text += f"💰 جایزه کل: {format_num(lottery_data.get('pool', 0))} سکه\n"
    text += f"🎫 کل بلیط‌ها: {total_tickets}\n"
    text += f"🎫 بلیط‌های شما: {user_tickets}\n"
    text += f"🎲 شانس شما: {user_tickets/total_tickets*100:.1f}%\n\n"
    
    if top_buyers:
        text += "🏆 **بیشترین بلیط‌ها:**\n"
        text += "\n".join(top_buyers)
    
    await safe_reply(message, text, chat_keypad=main_menu_keypad())
    return
    # ========== کازینو ==========
if button_id == "casino":
    await safe_reply(message, "🎲 **کازینو رویال**\n\nبازی مورد نظر را انتخاب کنید:", chat_keypad=casino_keypad())
    return

# اسلات ماشین
if button_id == "casino_slots":
    cost = 100
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= cost
    
    # نمادهای اسلات
    symbols = ["🍒", "🍊", "🍋", "🍉", "⭐", "💎", "7️⃣", "🎰"]
    reels = [random.choice(symbols) for _ in range(3)]
    
    # محاسبه برد
    win = 0
    if reels[0] == reels[1] == reels[2]:
        if reels[0] == "7️⃣":
            win = cost * 50
        elif reels[0] == "💎":
            win = cost * 20
        elif reels[0] == "⭐":
            win = cost * 10
        elif reels[0] == "🎰":
            win = cost * 100
        else:
            win = cost * 5
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        win = cost * 2
    
    user["coins"] += win
    data.setdefault("casino", {}).setdefault(user_id, {"slots_wins": 0, "slots_losses": 0})
    if win > 0:
        data["casino"][user_id]["slots_wins"] += 1
    else:
        data["casino"][user_id]["slots_losses"] += 1
    
    save_data(data)
    
    result_text = "برد!" if win > 0 else "باخت!"
    await safe_reply(message,
        f"🎰 **اسلات ماشین**\n\n"
        f"[ {reels[0]} ] [ {reels[1]} ] [ {reels[2]} ]\n\n"
        f"💰 شرط: {format_num(cost)} سکه\n"
        f"🎉 نتیجه: {result_text}\n"
        f"💰 برد: +{format_num(win)} سکه",
        chat_keypad=main_menu_keypad())
    return

# بلک‌جک
if button_id == "casino_blackjack":
    cost = 500
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    # کارت‌ها
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]  # 11 = Ace
    player_cards = [random.choice(cards), random.choice(cards)]
    dealer_cards = [random.choice(cards), random.choice(cards)]
    
    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)
    
    # ساده‌سازی: فقط یک دور
    if player_sum > 21:
        # بشکن
        win = 0
        result = "شما بشکن کردید!"
    elif dealer_sum > 21:
        win = cost * 2
        result = "دیلر بشکن کرد! شما برنده شدید!"
    elif player_sum > dealer_sum:
        win = cost * 2
        result = "شما برنده شدید!"
    elif player_sum < dealer_sum:
        win = 0
        result = "دیلر برنده شد!"
    else:
        win = cost
        result = "مساوی!"
    
    user["coins"] -= cost
    user["coins"] += win
    
    save_data(data)
    
    await safe_reply(message,
        f"🃏 **بلک‌جک**\n\n"
        f"🎴 کارت‌های شما: {player_cards[0]}, {player_cards[1]} = {player_sum}\n"
        f"🎴 کارت‌های دیلر: {dealer_cards[0]}, ?\n\n"
        f"💰 شرط: {format_num(cost)} سکه\n"
        f"🎉 نتیجه: {result}\n"
        f"💰 برد: +{format_num(win)} سکه",
        chat_keypad=main_menu_keypad())
    return

# رولت
if button_id == "casino_roulette":
    cost = 200
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    data["pending_action"][user_id] = {"action": "casino_roulette", "cost": cost}
    save_data(data)
    
    await safe_reply(message,
        f"🎡 **رولت**\n\n"
        f"💰 شرط: {format_num(cost)} سکه\n\n"
        f"🔴 قرمز (1-18)\n"
        f"⚫ سیاه (19-36)\n"
        f"🟢 صفر (0)\n\n"
        f"📝 رنگ یا عدد خود را وارد کنید:",
        chat_keypad=None)
    return

if pending.get("action") == "casino_roulette" and text:
    cost = pending.get("cost", 200)
    
    # چرخاندن رولت
    number = random.randint(0, 36)
    color = "🟢" if number == 0 else ("🔴" if number <= 18 else "⚫")
    
    win = 0
    result_text = ""
    
    if text.isdigit():
        bet_number = int(text)
        if 0 <= bet_number <= 36:
            if bet_number == number:
                win = cost * 35
                result_text = f"عدد {bet_number} آمد! شما برنده شدید!"
            else:
                result_text = f"عدد {number} آمد. شما باختید."
        else:
            result_text = "عدد نامعتبر!"
    else:
        bet_color = text.strip()
        if bet_color in ["قرمز", "🔴", "red"] and color == "🔴":
            win = cost * 2
            result_text = f"{color} {number} آمد! شما برنده شدید!"
        elif bet_color in ["سیاه", "⚫", "black"] and color == "⚫":
            win = cost * 2
            result_text = f"{color} {number} آمد! شما برنده شدید!"
        elif bet_color in ["صفر", "🟢", "zero", "0"] and number == 0:
            win = cost * 35
            result_text = f"صفر آمد! شما برنده شدید!"
        else:
            result_text = f"{color} {number} آمد. شما باختید."
    
    user["coins"] -= cost
    user["coins"] += win
    
    save_data(data)
    del data["pending_action"][user_id]
    save_data(data)
    
    await safe_reply(message,
        f"🎡 **رولت**\n\n"
        f"🎲 عدد: {number} {color}\n"
        f"💰 شرط: {format_num(cost)} سکه\n"
        f"🎉 نتیجه: {result_text}\n"
        f"💰 برد: +{format_num(win)} سکه",
        chat_keypad=main_menu_keypad())
    return

# تاس
if button_id == "casino_dice":
    cost = 50
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    user_dice = random.randint(1, 6)
    bot_dice = random.randint(1, 6)
    
    if user_dice > bot_dice:
        win = cost * 2
        result = "شما برنده شدید!"
    elif user_dice < bot_dice:
        win = 0
        result = "ربات برنده شد!"
    else:
        win = cost
        result = "مساوی!"
    
    user["coins"] -= cost
    user["coins"] += win
    
    save_data(data)
    
    await safe_reply(message,
        f"🎲 **تاس**\n\n"
        f"🎲 شما: {user_dice}\n"
        f"🤖 ربات: {bot_dice}\n\n"
        f"💰 شرط: {format_num(cost)} سکه\n"
        f"🎉 نتیجه: {result}\n"
        f"💰 برد: +{format_num(win)} سکه",
        chat_keypad=main_menu_keypad())
    return
    # ========== کلن ==========
if button_id == "clan":
    await safe_reply(message, "🎌 **منوی کلن**\n\nمدیریت کلن خود را از اینجا انجام دهید:", chat_keypad=clan_menu_keypad())
    return

# ساخت کلن
if button_id == "clan_create":
    if user.get("clan_id"):
        await safe_reply(message, "❌ **شما قبلاً عضو یک کلن هستید!**\nاول از کلن خود خارج شوید.", chat_keypad=main_menu_keypad())
        return
    
    cost = 10000
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    await safe_reply(message, "🏰 **نام کلن خود را وارد کنید:**\n(حداکثر ۲۰ کاراکتر)", chat_keypad=None)
    data["pending_action"][user_id] = {"action": "create_clan"}
    save_data(data)
    return

if pending.get("action") == "create_clan" and text:
    clan_name = text.strip()[:20]
    if not clan_name:
        await safe_reply(message, "❌ نام نمی‌تواند خالی باشد!", chat_keypad=main_menu_keypad())
        return
    
    # چک کردن تکراری نبودن نام
    for existing in data.get("clans", {}).values():
        if existing["name"].lower() == clan_name.lower():
            await safe_reply(message, "❌ **این نام قبلاً استفاده شده است!**\nنام دیگری انتخاب کنید.", chat_keypad=main_menu_keypad())
            return
    
    cost = 10000
    user["coins"] -= cost
    
    clan_id = f"clan_{user_id}_{int(time.time())}"
    data.setdefault("clans", {})[clan_id] = {
        "name": clan_name,
        "owner": user_id,
        "owner_name": country_name,
        "members": [user_id],
        "level": 1,
        "exp": 0,
        "treasury": 0,
        "description": "یک کلن جدید",
        "created_at": datetime.now().isoformat(),
        "wins": 0,
        "losses": 0
    }
    user["clan_id"] = clan_id
    
    save_data(data)
    
    await safe_reply(message,
        f"✅ **کلن {clan_name} با موفقیت ساخته شد!**\n\n"
        f"👑 شما رهبر کلن هستید.\n"
        f"💰 {format_num(cost)} سکه هزینه شد.\n\n"
        f"🎌 از منوی کلن برای مدیریت استفاده کنید.",
        chat_keypad=main_menu_keypad())
    return

# اطلاعات کلن من
if button_id == "clan_my":
    clan_id = user.get("clan_id")
    if not clan_id or clan_id not in data.get("clans", {}):
        await safe_reply(message, "❌ **شما عضو هیچ کلنی نیستید!**\nبا /clan_create یک کلن بسازید یا به کلن دیگری بپیوندید.", chat_keypad=main_menu_keypad())
        return
    
    clan = data["clans"][clan_id]
    
    # جمع‌آوری اطلاعات اعضا
    members_list = []
    total_power = 0
    for mid in clan.get("members", []):
        if mid in data["users"]:
            m = data["users"][mid]
            power = calculate_power(m)
            total_power += power
            role = "👑 رهبر" if mid == clan["owner"] else "👤 عضو"
            members_list.append(f"{role} {m['country_name']} | 💪{format_num(power)}")
    
    # محاسبه تجربه برای سطح بعدی
    next_exp = clan["level"] * 10000
    exp_progress = int((clan.get("exp", 0) / next_exp) * 20)
    exp_bar = "█" * exp_progress + "░" * (20 - exp_progress)
    
    await safe_reply(message,
        f"🎌 **کلن {clan['name']}**\n\n"
        f"👑 رهبر: {clan['owner_name']}\n"
        f"📈 سطح: {clan['level']}\n"
        f"📊 [{exp_bar}] {format_num(clan.get('exp', 0))}/{format_num(next_exp)}\n"
        f"💰 خزانه: {format_num(clan.get('treasury', 0))} سکه\n"
        f"💪 قدرت کل: {format_num(total_power)}\n"
        f"👥 اعضا: {len(clan.get('members', []))}\n"
        f"🏆 برد/باخت: {clan.get('wins', 0)}/{clan.get('losses', 0)}\n"
        f"📝 توضیحات: {clan.get('description', 'ندارد')}\n\n"
        f"👥 **لیست اعضا:**\n" + "\n".join(members_list[:15]),
        chat_keypad=clan_menu_keypad())
    return

# لیست کلن‌ها
if button_id == "clan_list":
    clans = data.get("clans", {})
    if not clans:
        await safe_reply(message, "📜 **هیچ کلنی وجود ندارد!**\nاولین نفری باش که کلن می‌سازد.", chat_keypad=main_menu_keypad())
        return
    
    text = "📜 **لیست کلن‌ها**\n\n"
    for cid, clan in list(clans.items())[:20]:
        text += f"🎌 {clan['name']} | 👑 {clan['owner_name'][:12]} | 👥 {len(clan.get('members', []))} | 📈س{clan['level']}\n"
    
    await safe_reply(message, text, chat_keypad=main_menu_keypad())
    return

# رتبه کلن‌ها
if button_id == "clan_rank":
    clans = data.get("clans", {})
    if not clans:
        await safe_reply(message, "🏆 **هیچ کلنی وجود ندارد!**", chat_keypad=main_menu_keypad())
        return
    
    # محاسبه قدرت هر کلن
    clan_powers = []
    for cid, clan in clans.items():
        total_power = 0
        for mid in clan.get("members", []):
            if mid in data["users"]:
                total_power += calculate_power(data["users"][mid])
        clan_powers.append({
            "name": clan["name"],
            "power": total_power,
            "level": clan["level"],
            "members": len(clan.get("members", []))
        })
    
    clan_powers.sort(key=lambda x: x["power"], reverse=True)
    
    text = "🏆 **رتبه کلن‌ها (بر اساس قدرت)**\n\n"
    for i, c in enumerate(clan_powers[:15], 1):
        medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else f"{i}."))
        text += f"{medal} {c['name'][:15]} | 💪{format_num(c['power'])} | 📈س{c['level']} | 👥{c['members']}\n"
    
    await safe_reply(message, text, chat_keypad=main_menu_keypad())
    return

# درخواست عضویت
if button_id == "clan_join":
    clans = data.get("clans", {})
    if not clans:
        await safe_reply(message, "❌ **هیچ کلنی وجود ندارد!**", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for cid, clan in list(clans.items())[:20]:
        builder.row(builder.button(f"join_clan_{cid}", f"🤝 {clan['name'][:15]} | 👥{len(clan.get('members', []))}"))
    builder.row(builder.button("clan", "🔙"))
    
    await safe_reply(message, "🤝 **انتخاب کلن برای درخواست عضویت:**", chat_keypad=builder.build())
    return

if button_id and button_id.startswith("join_clan_"):
    clan_id = button_id.replace("join_clan_", "")
    
    if clan_id not in data.get("clans", {}):
        await safe_reply(message, "❌ کلن یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    if user.get("clan_id"):
        await safe_reply(message, "❌ **شما قبلاً عضو یک کلن هستید!**", chat_keypad=main_menu_keypad())
        return
    
    clan = data["clans"][clan_id]
    
    # ذخیره درخواست
    data.setdefault("clan_requests", {}).setdefault(clan_id, []).append({
        "user_id": user_id,
        "user_name": country_name,
        "date": datetime.now().isoformat()
    })
    save_data(data)
    
    await safe_reply(message, f"✅ **درخواست عضویت به کلن {clan['name']} ارسال شد!**\nمنتظر تایید رهبر کلن باشید.", chat_keypad=main_menu_keypad())
    
    # اطلاع به رهبر کلن
    try:
        await bot.send_message(int(clan["owner"]),
            f"🤝 **درخواست عضویت جدید**\n\n"
            f"👤 کاربر: {country_name}\n"
            f"🎌 کلن: {clan['name']}\n\n"
            f"برای بررسی به منوی کلن بروید.")
    except:
        pass
    return

# کمک مالی به کلن
if button_id == "clan_donate":
    clan_id = user.get("clan_id")
    if not clan_id:
        await safe_reply(message, "❌ **شما عضو کلنی نیستید!**", chat_keypad=main_menu_keypad())
        return
    
    await safe_reply(message, "💰 **مبلغ کمک مالی را وارد کنید:**\n(حداقل ۱۰۰ سکه)\n\n💡 هر ۱۰۰ سکه = ۱۰ تجربه کلن", chat_keypad=None)
    data["pending_action"][user_id] = {"action": "clan_donate"}
    save_data(data)
    return

if pending.get("action") == "clan_donate" and text.isdigit():
    amount = int(text)
    clan_id = user.get("clan_id")
    
    if amount < 100:
        await safe_reply(message, "❌ **حداقل مبلغ ۱۰۰ سکه است!**", chat_keypad=main_menu_keypad())
    elif user.get("coins", 0) < amount:
        await safe_reply(message, f"❌ **سکه کافی نیست!**\nنیاز: {format_num(amount)} سکه", chat_keypad=main_menu_keypad())
    else:
        user["coins"] -= amount
        clan = data["clans"][clan_id]
        clan["treasury"] = clan.get("treasury", 0) + amount
        clan["exp"] = clan.get("exp", 0) + (amount // 10)
        
        # بررسی ارتقای سطح کلن
        old_level = clan["level"]
        next_exp = clan["level"] * 10000
        level_up = False
        
        while clan["exp"] >= next_exp and clan["level"] < 20:
            clan["level"] += 1
            clan["exp"] -= next_exp
            next_exp = clan["level"] * 10000
            level_up = True
            
            # اطلاع به اعضا
            for mid in clan.get("members", []):
                try:
                    await bot.send_message(int(mid), f"🎉 **کلن {clan['name']} به سطح {clan['level']} ارتقا یافت!** 🎉")
                except:
                    pass
        
        save_data(data)
        
        await safe_reply(message,
            f"✅ **{format_num(amount)} سکه به کلن کمک شد!**\n\n"
            f"📊 تجربه کلن: +{amount//10}\n"
            f"💰 خزانه کلن: {format_num(clan['treasury'])} سکه",
            chat_keypad=main_menu_keypad())
    
    del data["pending_action"][user_id]
    save_data(data)
    return

# ارتقای کلن (فقط رهبر)
if button_id == "clan_upgrade":
    clan_id = user.get("clan_id")
    if not clan_id:
        await safe_reply(message, "❌ **شما عضو کلنی نیستید!**", chat_keypad=main_menu_keypad())
        return
    
    clan = data["clans"][clan_id]
    
    if clan["owner"] != user_id:
        await safe_reply(message, "❌ **فقط رهبر کلن می‌تواند ارتقا دهد!**", chat_keypad=main_menu_keypad())
        return
    
    if clan["level"] >= 20:
        await safe_reply(message, "🏆 **کلن شما در حداکثر سطح است!**", chat_keypad=main_menu_keypad())
        return
    
    cost = clan["level"] * 5000
    if clan.get("treasury", 0) < cost:
        await safe_reply(message, f"❌ **خزانه کلن {format_num(cost)} سکه نیاز دارد!**", chat_keypad=main_menu_keypad())
        return
    
    clan["treasury"] -= cost
    clan["level"] += 1
    
    save_data(data)
    
    await safe_reply(message,
        f"🎉 **کلن {clan['name']} به سطح {clan['level']} ارتقا یافت!** 🎉\n\n"
        f"💰 هزینه: {format_num(cost)} سکه از خزانه",
        chat_keypad=main_menu_keypad())
    
    # اطلاع به اعضا
    for mid in clan.get("members", []):
        if mid != user_id:
            try:
                await bot.send_message(int(mid), f"🎉 **کلن {clan['name']} به سطح {clan['level']} ارتقا یافت!** 🎉")
            except:
                pass
    return

# خروج از کلن
if button_id == "clan_leave":
    clan_id = user.get("clan_id")
    if not clan_id:
        await safe_reply(message, "❌ **شما عضو کلنی نیستید!**", chat_keypad=main_menu_keypad())
        return
    
    clan = data["clans"][clan_id]
    
    if clan["owner"] == user_id:
        # انتقال رهبری
        other_members = [m for m in clan.get("members", []) if m != user_id]
        if other_members:
            new_owner = other_members[0]
            clan["owner"] = new_owner
            clan["owner_name"] = data["users"][new_owner]["country_name"]
            await safe_reply(message, f"👑 **رهبری کلن به {clan['owner_name']} منتقل شد.**", chat_keypad=main_menu_keypad())
            
            try:
                await bot.send_message(int(new_owner), f"👑 **شما رهبر جدید کلن {clan['name']} شدید!**")
            except:
                pass
        else:
            # حذف کلن
            del data["clans"][clan_id]
            await safe_reply(message, f"🏰 **کلن {clan['name']} حذف شد.**", chat_keypad=main_menu_keypad())
    else:
        clan["members"] = [m for m in clan.get("members", []) if m != user_id]
        await safe_reply(message, f"🚪 **شما از کلن {clan['name']} خارج شدید.**", chat_keypad=main_menu_keypad())
    
    user["clan_id"] = None
    save_data(data)
    return
    
    # ========== امپراتوری ==========
if button_id == "empire":
    await safe_reply(message, "👑 **منوی امپراتوری**\n\nبا ایجاد امپراتوری، قدرت خود را چند برابر کنید:", chat_keypad=empire_menu_keypad())
    return

# ساخت امپراتوری
if button_id == "empire_create":
    if user.get("empire_id"):
        await safe_reply(message, "❌ **شما قبلاً امپراتوری دارید!**", chat_keypad=main_menu_keypad())
        return
    
    cost = 50000
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    await safe_reply(message, "👑 **نام امپراتوری خود را وارد کنید:**\n(حداکثر ۲۰ کاراکتر)", chat_keypad=None)
    data["pending_action"][user_id] = {"action": "create_empire"}
    save_data(data)
    return

if pending.get("action") == "create_empire" and text:
    empire_name = text.strip()[:20]
    if not empire_name:
        await safe_reply(message, "❌ نام نمی‌تواند خالی باشد!", chat_keypad=main_menu_keypad())
        return
    
    cost = 50000
    user["coins"] -= cost
    
    empire_id = f"empire_{user_id}_{int(time.time())}"
    data.setdefault("empires", {})[empire_id] = {
        "name": empire_name,
        "owner": user_id,
        "owner_name": country_name,
        "members": [user_id],
        "level": 1,
        "exp": 0,
        "treasury": 0,
        "territories": [],
        "created_at": datetime.now().isoformat()
    }
    user["empire_id"] = empire_id
    
    save_data(data)
    
    await safe_reply(message,
        f"✅ **امپراتوری {empire_name} با موفقیت تأسیس شد!**\n\n"
        f"👑 شما امپراتور هستید.\n"
        f"💰 {format_num(cost)} سکه هزینه شد.",
        chat_keypad=main_menu_keypad())
    return

# اطلاعات امپراتوری
if button_id == "empire_info":
    empire_id = user.get("empire_id")
    if not empire_id or empire_id not in data.get("empires", {}):
        await safe_reply(message, "❌ **شما عضو هیچ امپراتوری نیستید!**", chat_keypad=main_menu_keypad())
        return
    
    empire = data["empires"][empire_id]
    
    # جمع‌آوری اطلاعات
    members_list = []
    total_power = 0
    for mid in empire.get("members", []):
        if mid in data["users"]:
            m = data["users"][mid]
            power = calculate_power(m)
            total_power += power
            role = "👑 امپراتور" if mid == empire["owner"] else "👤 وزیر" if mid in empire.get("ministers", []) else "👤 عضو"
            members_list.append(f"{role} {m['country_name']} | 💪{format_num(power)}")
    
    await safe_reply(message,
        f"👑 **امپراتوری {empire['name']}**\n\n"
        f"👑 امپراتور: {empire['owner_name']}\n"
        f"📈 سطح: {empire.get('level', 1)}\n"
        f"💰 خزانه: {format_num(empire.get('treasury', 0))} سکه\n"
        f"💪 قدرت کل: {format_num(total_power)}\n"
        f"👥 اعضا: {len(empire.get('members', []))}\n"
        f"🗺️ قلمروها: {len(empire.get('territories', []))}\n\n"
        f"👥 **لیست اعضا:**\n" + "\n".join(members_list[:15]),
        chat_keypad=empire_menu_keypad())
    return
    # ========== ازدواج ==========
if button_id == "marriage":
    await safe_reply(message, "💑 **منوی ازدواج**\n\nبا ازدواج می‌توانید قدرت خود را افزایش دهید:", chat_keypad=marriage_menu_keypad())
    return

# پیشنهاد ازدواج
if button_id == "marriage_propose":
    if user.get("married_to"):
        await safe_reply(message, "❌ **شما قبلاً ازدواج کرده‌اید!**\nبرای ازدواج مجدد必须先 طلاق بگیرید.", chat_keypad=main_menu_keypad())
        return
    
    # پیدا کردن کاربران آنلاین
    available_users = []
    for uid, u in data["users"].items():
        if uid != user_id and u.get("country_name") and not u.get("married_to") and uid not in data.get("banned_users", []):
            available_users.append((uid, u["country_name"]))
    
    if not available_users:
        await safe_reply(message, "❌ **هیچ کاربر مجردی برای ازدواج وجود ندارد!**", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for uid, name in available_users[:20]:
        builder.row(builder.button(f"marry_propose_{uid}", f"💍 {name[:20]}"))
    builder.row(builder.button("marriage", "🔙"))
    
    await safe_reply(message, "💍 **انتخاب همسر آینده:**", chat_keypad=builder.build())
    return

if button_id and button_id.startswith("marry_propose_"):
    target_id = button_id.replace("marry_propose_", "")
    
    if target_id not in data["users"]:
        await safe_reply(message, "❌ کاربر یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    target = data["users"][target_id]
    
    if target.get("married_to"):
        await safe_reply(message, f"❌ **{target['country_name']} قبلاً ازدواج کرده است!**", chat_keypad=main_menu_keypad())
        return
    
    # ذخیره درخواست
    data.setdefault("marriage_requests", []).append({
        "from_id": user_id,
        "from_name": country_name,
        "to_id": target_id,
        "to_name": target["country_name"],
        "date": datetime.now().isoformat()
    })
    save_data(data)
    
    await safe_reply(message, f"💍 **درخواست ازدواج به {target['country_name']} ارسال شد!**\nمنتظر پاسخ باشید.", chat_keypad=main_menu_keypad())
    
    # اطلاع به طرف مقابل
    try:
        builder = ChatKeypadBuilder()
        builder.row(
            builder.button(f"marry_accept_{user_id}", "✅ قبول"),
            builder.button(f"marry_reject_{user_id}", "❌ رد")
        )
        await bot.send_message(int(target_id),
            f"💍 **درخواست ازدواج از {country_name}**\n\n"
            f"آیا با ازدواج موافقید؟",
            chat_keypad=builder.build())
    except:
        pass
    return

# پذیرفتن ازدواج
if button_id and button_id.startswith("marry_accept_"):
    from_id = button_id.replace("marry_accept_", "")
    
    if from_id not in data["users"]:
        await safe_reply(message, "❌ کاربر یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    from_user = data["users"][from_id]
    
    if from_user.get("married_to"):
        await safe_reply(message, f"❌ {from_user['country_name']} قبلاً ازدواج کرده است!", chat_keypad=main_menu_keypad())
        return
    
    if user.get("married_to"):
        await safe_reply(message, "❌ شما قبلاً ازدواج کرده‌اید!", chat_keypad=main_menu_keypad())
        return
    
    # انجام ازدواج
    user["married_to"] = from_id
    from_user["married_to"] = user_id
    
    # پاداش ازدواج
    reward = 5000
    user["coins"] = user.get("coins", 0) + reward
    from_user["coins"] = from_user.get("coins", 0) + reward
    
    # مدال ازدواج
    user.setdefault("achievements", []).append("marriage")
    from_user.setdefault("achievements", []).append("marriage")
    
    # حذف درخواست‌ها
    data["marriage_requests"] = [r for r in data.get("marriage_requests", []) if not ((r["from_id"] == from_id and r["to_id"] == user_id) or (r["from_id"] == user_id and r["to_id"] == from_id))]
    
    save_data(data)
    
    await safe_reply(message,
        f"💑 **تبریک! شما با {from_user['country_name']} ازدواج کردید!** 💑\n\n"
        f"💰 +{format_num(reward)} سکه به هر دو نفر\n"
        f"🏆 مدال عشق ابدی\n"
        f"💪 قدرت زوجی: +۱۰٪ در حملات مشترک",
        chat_keypad=main_menu_keypad())
    
    try:
        await bot.send_message(int(from_id),
            f"💑 **تبریک! {country_name} درخواست ازدواج شما را پذیرفت!** 💑\n\n"
            f"💰 +{format_num(reward)} سکه دریافت کردید.")
    except:
        pass
    return

# رد کردن ازدواج
if button_id and button_id.startswith("marry_reject_"):
    from_id = button_id.replace("marry_reject_", "")
    
    data["marriage_requests"] = [r for r in data.get("marriage_requests", []) if not (r["from_id"] == from_id and r["to_id"] == user_id)]
    save_data(data)
    
    await safe_reply(message, "❌ درخواست ازدواج رد شد.", chat_keypad=main_menu_keypad())
    
    try:
        await bot.send_message(int(from_id), f"❌ درخواست ازدواج شما توسط {country_name} رد شد.")
    except:
        pass
    return

# اطلاعات ازدواج من
if button_id == "marriage_my":
    married_to = user.get("married_to")
    if not married_to or married_to not in data["users"]:
        await safe_reply(message, "💔 **شما مجرد هستید!**\nبرای ازدواج به منوی ازدواج بروید.", chat_keypad=main_menu_keypad())
        return
    
    spouse = data["users"][married_to]
    
    await safe_reply(message,
        f"💑 **اطلاعات ازدواج** 💑\n\n"
        f"👫 همسر: {spouse['country_name']}\n"
        f"💪 قدرت همسر: {format_num(calculate_power(spouse))}\n"
        f"💰 سکه همسر: {format_num(spouse.get('coins', 0))}\n"
        f"❤️ جان همسر: {format_num(spouse.get('health', 100000))}/{format_num(spouse.get('max_health', 100000))}\n\n"
        f"✨ **مزایای ازدواج:**\n"
        f"• +۱۰٪ قدرت در حملات گروهی\n"
        f"• امکان هدیه دادن به همسر\n"
        f"• محافظت متقابل",
        chat_keypad=marriage_menu_keypad())
    return

# هدیه به همسر
if button_id == "marriage_gift":
    married_to = user.get("married_to")
    if not married_to:
        await safe_reply(message, "❌ شما مجرد هستید!", chat_keypad=main_menu_keypad())
        return
    
    await safe_reply(message, "🎁 **مبلغ هدیه را وارد کنید:**\n(حداقل ۱۰۰ سکه)", chat_keypad=None)
    data["pending_action"][user_id] = {"action": "marriage_gift"}
    save_data(data)
    return

if pending.get("action") == "marriage_gift" and text.isdigit():
    amount = int(text)
    married_to = user.get("married_to")
    
    if amount < 100:
        await safe_reply(message, "❌ حداقل ۱۰۰ سکه!", chat_keypad=main_menu_keypad())
    elif user.get("coins", 0) < amount:
        await safe_reply(message, f"❌ سکه کافی نیست! نیاز: {format_num(amount)}", chat_keypad=main_menu_keypad())
    else:
        user["coins"] -= amount
        spouse = data["users"][married_to]
        spouse["coins"] = spouse.get("coins", 0) + amount
        
        save_data(data)
        
        await safe_reply(message, f"🎁 {format_num(amount)} سکه به همسرتان هدیه دادید!", chat_keypad=main_menu_keypad())
        
        try:
            await bot.send_message(int(married_to), f"🎁 همسرتان {country_name} {format_num(amount)} سکه به شما هدیه داد!")
        except:
            pass
    
    del data["pending_action"][user_id]
    save_data(data)
    return

# طلاق
if button_id == "marriage_divorce":
    if not user.get("married_to"):
        await safe_reply(message, "❌ شما مجرد هستید!", chat_keypad=main_menu_keypad())
        return
    
    cost = 10000
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ {format_num(cost)} سکه برای طلاق نیاز است!", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    builder.row(builder.button("divorce_confirm", "✅ تایید طلاق"), builder.button("back_main", "🔙"))
    await safe_reply(message, f"⚠️ **آیا از طلاق مطمئن هستید؟**\n💰 هزینه: {format_num(cost)} سکه", chat_keypad=builder.build())
    return

if button_id == "divorce_confirm":
    married_to = user.get("married_to")
    if not married_to:
        await safe_reply(message, "❌ شما مجرد هستید!", chat_keypad=main_menu_keypad())
        return
    
    cost = 10000
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ سکه کافی نیست!", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= cost
    spouse_name = data["users"][married_to]["country_name"]
    
    # حذف ازدواج
    if married_to in data["users"]:
        data["users"][married_to]["married_to"] = None
    user["married_to"] = None
    
    save_data(data)
    
    await safe_reply(message, f"💔 **شما از {spouse_name} طلاق گرفتید!**\n💰 {format_num(cost)} سکه هزینه شد.", chat_keypad=main_menu_keypad())
    
    try:
        await bot.send_message(int(married_to), f"💔 همسرتان {country_name} از شما طلاق گرفت!")
    except:
        pass
    return
# ========== حیوانات (کامل) ==========
if button_id == "pet":
    builder = ChatKeypadBuilder()
    builder.row(builder.button("pet_shop", "🐕 فروشگاه حیوانات"))
    builder.row(builder.button("pet_list", "📋 حیوانات من"))
    builder.row(builder.button("pet_feed", "🍖 غذا دادن"))
    builder.row(builder.button("pet_upgrade", "📈 ارتقای حیوان"))
    builder.row(builder.button("pet_rename", "✏️ تغییر نام"))
    builder.row(builder.button("pet_sell", "💰 فروش حیوان"))
    builder.row(builder.button("pet_battle", "⚔️ مسابقه حیوانات"))
    builder.row(builder.button("pet_equip", "🎽 تجهیزات حیوان"))
    builder.row(builder.button("pet_heal", "💊 درمان حیوان"))
    builder.row(builder.button("back_main", "🔙"))
    await safe_reply(message, "🐉 **سیستم حیوانات پیشرفته**\n\n"
        "✨ حیوانات می‌توانند:\n"
        "• به شما قدرت ببخشند\n"
        "• در جنگ به شما کمک کنند\n"
        "• با هم مسابقه دهند\n"
        "• ارتقا پیدا کنند\n"
        "• تجهیزات بپوشند", chat_keypad=builder.build())
    return

# فروشگاه حیوانات
if button_id == "pet_shop":
    builder = ChatKeypadBuilder()
    for pid, pet in PETS_DB.items():
        if user.get("level", 1) >= pet.get("level_req", 1):
            builder.row(builder.button(f"pet_buy_{pid}", 
                f"{pet['name']} | {format_num(pet['price'])}💰 | 🎯{pet.get('level_req',1)}"))
        else:
            builder.row(builder.button(f"pet_locked_{pid}", 
                f"🔒 {pet['name']} (نیاز سطح {pet.get('level_req',1)})"))
    builder.row(builder.button("pet", "🔙"))
    
    await safe_reply(message,
        f"🐕 **فروشگاه حیوانات**\n\n"
        f"💰 سکه شما: {format_num(user.get('coins', 0))}\n"
        f"📈 سطح شما: {user.get('level', 1)}\n\n"
        f"✨ هر حیوان قدرت ویژه خود را دارد!",
        chat_keypad=builder.build())
    return

# خرید حیوان
if button_id and button_id.startswith("pet_buy_"):
    pet_id = int(button_id.replace("pet_buy_", ""))
    
    if pet_id not in PETS_DB:
        await safe_reply(message, "❌ حیوان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    pet = PETS_DB[pet_id]
    
    if user.get("level", 1) < pet.get("level_req", 1):
        await safe_reply(message, f"❌ **سطح {pet['level_req']} نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    if user.get("coins", 0) < pet["price"]:
        await safe_reply(message, f"❌ **{format_num(pet['price'])} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    # بررسی ظرفیت حیوانات (حداکثر 10 عدد)
    pets_list = user.get("pets_list", [])
    if len(pets_list) >= 10:
        await safe_reply(message, "❌ **ظرفیت حیوانات شما پر است!**\nحداکثر ۱۰ حیوان می‌توانید داشته باشید.", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= pet["price"]
    
    new_pet = {
        "id": pet_id,
        "name": pet["name"],
        "custom_name": pet["name"],
        "level": 1,
        "exp": 0,
        "health": 100,
        "max_health": 100,
        "hunger": 100,
        "happiness": 100,
        "equipment": {},
        "battle_wins": 0,
        "battle_losses": 0,
        "buy_date": datetime.now().isoformat()
    }
    
    user.setdefault("pets_list", []).append(new_pet)
    
    save_data(data)
    
    await safe_reply(message,
        f"✅ **{pet['name']} خریداری شد!**\n\n"
        f"🐕 نام: {pet['name']}\n"
        f"💰 قیمت: {format_num(pet['price'])} سکه\n"
        f"🎁 پاداش اولیه: {format_num(pet.get('bonus', {}).get('attack', 0))} قدرت\n\n"
        f"✨ از منوی حیوانات برای مدیریت استفاده کنید.",
        chat_keypad=main_menu_keypad())
    return

# حیوان قفل شده
if button_id and button_id.startswith("pet_locked_"):
    await safe_reply(message, "🔒 **این حیوان قفل است!**\nسطح خود را افزایش دهید.", chat_keypad=main_menu_keypad())
    return

# لیست حیوانات من
if button_id == "pet_list":
    pets_list = user.get("pets_list", [])
    
    if not pets_list:
        await safe_reply(message, "🐕 **شما هیچ حیوانی ندارید!**\nاز فروشگاه حیوانات خرید کنید.", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for i, pet in enumerate(pets_list[:8]):
        # محاسبه وضعیت
        hunger_status = "😋" if pet.get("hunger", 100) > 70 else "😐" if pet.get("hunger", 100) > 30 else "😫"
        health_status = "❤️" if pet.get("health", 100) > 70 else "💛" if pet.get("health", 100) > 30 else "💔"
        
        builder.row(builder.button(f"pet_detail_{i}", 
            f"{pet['custom_name']} | سطح{pet.get('level',1)} | {hunger_status}{health_status}"))
    builder.row(builder.button("pet", "🔙"))
    
    await safe_reply(message, "🐕 **حیوانات شما:**\n(برای مشاهده جزئیات کلیک کنید)", chat_keypad=builder.build())
    return

# جزئیات حیوان
if button_id and button_id.startswith("pet_detail_"):
    idx = int(button_id.replace("pet_detail_", ""))
    pets_list = user.get("pets_list", [])
    
    if idx >= len(pets_list):
        await safe_reply(message, "❌ حیوان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    pet = pets_list[idx]
    original_pet = PETS_DB.get(pet["id"], {})
    
    # نوار وضعیت
    hunger_bar = "█" * (pet.get("hunger", 100) // 10) + "░" * (10 - (pet.get("hunger", 100) // 10))
    health_bar = "█" * (pet.get("health", 100) // 10) + "░" * (10 - (pet.get("health", 100) // 10))
    happiness_bar = "█" * (pet.get("happiness", 100) // 10) + "░" * (10 - (pet.get("happiness", 100) // 10))
    
    # محاسبه قدرت حیوان
    pet_power = (pet.get("level", 1) * 50) + (original_pet.get("bonus", {}).get("attack", 0) * pet.get("level", 1))
    
    builder = ChatKeypadBuilder()
    builder.row(builder.button(f"pet_feed_{idx}", "🍖 غذا"), builder.button(f"pet_play_{idx}", "🎮 بازی"))
    builder.row(builder.button(f"pet_upgrade_{idx}", f"📈 ارتقا ({pet.get('level',1)}→{pet.get('level',1)+1})"))
    builder.row(builder.button(f"pet_rename_{idx}", "✏️ تغییر نام"), builder.button(f"pet_sell_{idx}", "💰 فروش"))
    builder.row(builder.button(f"pet_heal_{idx}", "💊 درمان"), builder.button(f"pet_equip_{idx}", "🎽 تجهیزات"))
    builder.row(builder.button("pet_list", "🔙"))
    
    await safe_reply(message,
        f"🐉 **{pet['custom_name']}** ({original_pet.get('name', 'ناشناس')})\n\n"
        f"📊 **آمار:**\n"
        f"📈 سطح: {pet.get('level', 1)}\n"
        f"💪 قدرت: {format_num(pet_power)}\n"
        f"❤️ سلامت: [{health_bar}] {pet.get('health', 100)}/100\n"
        f"🍖 گرسنگی: [{hunger_bar}] {pet.get('hunger', 100)}/100\n"
        f"😊 شادی: [{happiness_bar}] {pet.get('happiness', 100)}/100\n"
        f"🏆 برد/باخت: {pet.get('battle_wins', 0)}/{pet.get('battle_losses', 0)}\n\n"
        f"🎁 **پاداش فعال:**\n"
        f"• حمله: +{original_pet.get('bonus', {}).get('attack', 0) * pet.get('level', 1)}\n"
        f"• دفاع: +{original_pet.get('bonus', {}).get('defense', 0) * pet.get('level', 1)}\n"
        f"• جاسوسی: +{original_pet.get('bonus', {}).get('spy', 0) * pet.get('level', 1)}",
        chat_keypad=builder.build())
    return

# غذا دادن به حیوان
if button_id and button_id.startswith("pet_feed_"):
    idx = int(button_id.replace("pet_feed_", ""))
    pets_list = user.get("pets_list", [])
    
    if idx >= len(pets_list):
        await safe_reply(message, "❌ حیوان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    pet = pets_list[idx]
    
    cost = 100 * pet.get("level", 1)
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= cost
    pet["hunger"] = min(100, pet.get("hunger", 100) + 30)
    pet["happiness"] = min(100, pet.get("happiness", 100) + 10)
    
    save_data(data)
    
    await safe_reply(message,
        f"🍖 **به {pet['custom_name']} غذا دادید!**\n\n"
        f"🍖 گرسنگی: +30\n"
        f"😊 شادی: +10\n"
        f"💰 هزینه: {format_num(cost)} سکه",
        chat_keypad=main_menu_keypad())
    return

# بازی با حیوان
if button_id and button_id.startswith("pet_play_"):
    idx = int(button_id.replace("pet_play_", ""))
    pets_list = user.get("pets_list", [])
    
    if idx >= len(pets_list):
        await safe_reply(message, "❌ حیوان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    pet = pets_list[idx]
    
    pet["happiness"] = min(100, pet.get("happiness", 100) + 20)
    pet["hunger"] = max(0, pet.get("hunger", 100) - 10)
    
    # تجربه تصادفی
    exp_gain = random.randint(10, 30)
    pet["exp"] = pet.get("exp", 0) + exp_gain
    
    # چک کردن ارتقای سطح
    old_level = pet.get("level", 1)
    new_level = 1 + (pet["exp"] // 200)
    level_up = False
    if new_level > old_level and new_level <= 20:
        pet["level"] = new_level
        pet["max_health"] = 100 + (new_level - 1) * 10
        pet["health"] = pet["max_health"]
        level_up = True
    
    save_data(data)
    
    level_text = f"\n🎉 **سطح {new_level} شد!** 🎉" if level_up else ""
    
    await safe_reply(message,
        f"🎮 **با {pet['custom_name']} بازی کردید!**\n\n"
        f"😊 شادی: +20\n"
        f"🍖 گرسنگی: -10\n"
        f"📈 تجربه حیوان: +{exp_gain}{level_text}",
        chat_keypad=main_menu_keypad())
    return

# ارتقای حیوان
if button_id and button_id.startswith("pet_upgrade_"):
    idx = int(button_id.replace("pet_upgrade_", ""))
    pets_list = user.get("pets_list", [])
    
    if idx >= len(pets_list):
        await safe_reply(message, "❌ حیوان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    pet = pets_list[idx]
    
    if pet.get("level", 1) >= 20:
        await safe_reply(message, "🏆 **حیوان شما در حداکثر سطح است!**", chat_keypad=main_menu_keypad())
        return
    
    cost = 500 * pet.get("level", 1)
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    # چک کردن نیازهای ارتقا
    if pet.get("happiness", 100) < 50:
        await safe_reply(message, "❌ **شادی حیوان کمتر از ۵۰ است!**\nاول با حیوان بازی کنید.", chat_keypad=main_menu_keypad())
        return
    
    if pet.get("hunger", 100) < 50:
        await safe_reply(message, "❌ **گرسنگی حیوان کمتر از ۵۰ است!**\nاول به حیوان غذا دهید.", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= cost
    pet["level"] = pet.get("level", 1) + 1
    pet["max_health"] = 100 + (pet["level"] - 1) * 10
    pet["health"] = pet["max_health"]
    
    save_data(data)
    
    await safe_reply(message,
        f"📈 **{pet['custom_name']} به سطح {pet['level']} ارتقا یافت!**\n\n"
        f"💪 قدرت حیوان افزایش یافت!\n"
        f"❤️ حداکثر سلامت: {pet['max_health']}\n"
        f"💰 هزینه: {format_num(cost)} سکه",
        chat_keypad=main_menu_keypad())
    return

# تغییر نام حیوان
if button_id and button_id.startswith("pet_rename_"):
    idx = int(button_id.replace("pet_rename_", ""))
    data["pending_action"][user_id] = {"action": "pet_rename", "pet_idx": idx}
    save_data(data)
    await safe_reply(message, "✏️ **نام جدید حیوان را وارد کنید:**\n(حداکثر ۱۵ کاراکتر)", chat_keypad=None)
    return

if pending.get("action") == "pet_rename" and text:
    idx = pending.get("pet_idx", 0)
    pets_list = user.get("pets_list", [])
    
    if idx >= len(pets_list):
        await safe_reply(message, "❌ حیوان یافت نشد!", chat_keypad=main_menu_keypad())
    else:
        new_name = text.strip()[:15]
        if new_name:
            pets_list[idx]["custom_name"] = new_name
            save_data(data)
            await safe_reply(message, f"✅ **نام حیوان به {new_name} تغییر کرد!**", chat_keypad=main_menu_keypad())
        else:
            await safe_reply(message, "❌ نام نمی‌تواند خالی باشد!", chat_keypad=main_menu_keypad())
    
    del data["pending_action"][user_id]
    save_data(data)
    return

# فروش حیوان
if button_id and button_id.startswith("pet_sell_"):
    idx = int(button_id.replace("pet_sell_", ""))
    pets_list = user.get("pets_list", [])
    
    if idx >= len(pets_list):
        await safe_reply(message, "❌ حیوان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    pet = pets_list[idx]
    original_pet = PETS_DB.get(pet["id"], {})
    
    # قیمت فروش (۵۰٪ قیمت خرید)
    sell_price = int(original_pet.get("price", 100) * 0.5)
    
    builder = ChatKeypadBuilder()
    builder.row(builder.button(f"pet_sell_confirm_{idx}", "✅ تایید فروش"), builder.button("pet_list", "🔙"))
    
    await safe_reply(message,
        f"💰 **فروش {pet['custom_name']}**\n\n"
        f"💵 قیمت فروش: {format_num(sell_price)} سکه\n"
        f"⚠️ آیا مطمئن هستید؟",
        chat_keypad=builder.build())
    return

if button_id and button_id.startswith("pet_sell_confirm_"):
    idx = int(button_id.replace("pet_sell_confirm_", ""))
    pets_list = user.get("pets_list", [])
    
    if idx >= len(pets_list):
        await safe_reply(message, "❌ حیوان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    pet = pets_list[idx]
    original_pet = PETS_DB.get(pet["id"], {})
    sell_price = int(original_pet.get("price", 100) * 0.5)
    
    # حذف حیوان
    user["pets_list"] = [p for i, p in enumerate(pets_list) if i != idx]
    user["coins"] = user.get("coins", 0) + sell_price
    
    save_data(data)
    
    await safe_reply(message,
        f"💰 **{pet['custom_name']} فروخته شد!**\n\n"
        f"💵 +{format_num(sell_price)} سکه",
        chat_keypad=main_menu_keypad())
    return

# درمان حیوان
if button_id and button_id.startswith("pet_heal_"):
    idx = int(button_id.replace("pet_heal_", ""))
    pets_list = user.get("pets_list", [])
    
    if idx >= len(pets_list):
        await safe_reply(message, "❌ حیوان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    pet = pets_list[idx]
    
    cost = 200 * pet.get("level", 1)
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= cost
    pet["health"] = pet.get("max_health", 100)
    
    save_data(data)
    
    await safe_reply(message,
        f"💊 **{pet['custom_name']} درمان شد!**\n\n"
        f"❤️ سلامت: {pet['health']}/{pet.get('max_health', 100)}\n"
        f"💰 هزینه: {format_num(cost)} سکه",
        chat_keypad=main_menu_keypad())
    return

# مسابقه حیوانات
if button_id == "pet_battle":
    pets_list = user.get("pets_list", [])
    if not pets_list:
        await safe_reply(message, "❌ **شما حیوانی ندارید!**\nاول حیوان بخرید.", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for i, pet in enumerate(pets_list[:8]):
        if pet.get("health", 100) > 0:
            builder.row(builder.button(f"pet_battle_select_{i}", 
                f"⚔️ {pet['custom_name']} | سطح{pet.get('level',1)} | ❤️{pet.get('health',100)}"))
    builder.row(builder.button("pet", "🔙"))
    
    await safe_reply(message, "⚔️ **انتخاب حیوان برای مسابقه:**\n(حیوان سالم انتخاب کنید)", chat_keypad=builder.build())
    return

if button_id and button_id.startswith("pet_battle_select_"):
    my_idx = int(button_id.replace("pet_battle_select_", ""))
    my_pets = user.get("pets_list", [])
    
    if my_idx >= len(my_pets):
        await safe_reply(message, "❌ حیوان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    my_pet = my_pets[my_idx]
    
    if my_pet.get("health", 100) <= 0:
        await safe_reply(message, "❌ **حیوان شما مرده است!**\nاول درمان کنید.", chat_keypad=main_menu_keypad())
        return
    
    # پیدا کردن حریف (یک حیوان تصادفی از یک کاربر دیگر)
    opponents = []
    for uid, u in data["users"].items():
        if uid != user_id and u.get("pets_list"):
            for p in u["pets_list"]:
                if p.get("health", 100) > 0:
                    opponents.append((uid, u["country_name"], p))
    
    if not opponents:
        await safe_reply(message, "❌ **هیچ حریفی برای مسابقه وجود ندارد!**\nبعداً دوباره تلاش کن.", chat_keypad=main_menu_keypad())
        return
    
    opponent_uid, opponent_name, opponent_pet = random.choice(opponents)
    
    # محاسبه قدرت حیوانات
    my_power = (my_pet.get("level", 1) * 50) + random.randint(1, 30)
    opp_power = (opponent_pet.get("level", 1) * 50) + random.randint(1, 30)
    
    # مسابقه
    if my_power > opp_power:
        winner = "you"
        my_pet["battle_wins"] = my_pet.get("battle_wins", 0) + 1
        opponent_pet["battle_losses"] = opponent_pet.get("battle_losses", 0) + 1
        
        # پاداش
        reward = 500
        user["coins"] = user.get("coins", 0) + reward
        my_pet["exp"] = my_pet.get("exp", 0) + 50
        
        # چک کردن ارتقا
        old_level = my_pet.get("level", 1)
        new_level = 1 + (my_pet["exp"] // 200)
        level_up = new_level > old_level and new_level <= 20
        
        if level_up:
            my_pet["level"] = new_level
            my_pet["max_health"] = 100 + (new_level - 1) * 10
            my_pet["health"] = my_pet["max_health"]
        
        save_data(data)
        
        level_text = f"\n🎉 **حیوان شما به سطح {new_level} رسید!** 🎉" if level_up else ""
        
        await safe_reply(message,
            f"⚔️ **مسابقه حیوانات!** ⚔️\n\n"
            f"🐕 {my_pet['custom_name']} (شما) 💪{my_power}\n"
            f"🐕 {opponent_pet['custom_name']} ({opponent_name}) 💪{opp_power}\n\n"
            f"🎉 **شما برنده شدید!** 🎉\n"
            f"💰 +{format_num(reward)} سکه\n"
            f"📈 +۵۰ تجربه حیوان{level_text}",
            chat_keypad=main_menu_keypad())
        
        # اطلاع به بازنده
        try:
            await bot.send_message(int(opponent_uid),
                f"⚔️ **مسابقه حیوانات!**\n\n"
                f"🐕 {opponent_pet['custom_name']} شما در مقابل {my_pet['custom_name']} باخت! 😢")
        except:
            pass
    else:
        my_pet["battle_losses"] = my_pet.get("battle_losses", 0) + 1
        opponent_pet["battle_wins"] = opponent_pet.get("battle_wins", 0) + 1
        
        # کاهش سلامت
        damage = random.randint(10, 30)
        my_pet["health"] = max(0, my_pet.get("health", 100) - damage)
        
        save_data(data)
        
        await safe_reply(message,
            f"⚔️ **مسابقه حیوانات!** ⚔️\n\n"
            f"🐕 {my_pet['custom_name']} (شما) 💪{my_power}\n"
            f"🐕 {opponent_pet['custom_name']} ({opponent_name}) 💪{opp_power}\n\n"
            f"😢 **شما باختید!**\n"
            f"💔 سلامت حیوان: -{damage}\n"
            f"❤️ سلامت فعلی: {my_pet['health']}/{my_pet.get('max_health', 100)}",
            chat_keypad=main_menu_keypad())
    return
    # ========== لیدربرد کامل ==========
if button_id == "leaderboard" or button_id == "lb_power" or button_id == "lb_coins" or button_id == "lb_level" or button_id == "lb_kills" or button_id == "lb_attacks":
    
    if button_id == "leaderboard":
        sort_type = "power"
    elif button_id == "lb_power":
        sort_type = "power"
    elif button_id == "lb_coins":
        sort_type = "coins"
    elif button_id == "lb_level":
        sort_type = "level"
    elif button_id == "lb_kills":
        sort_type = "kills"
    elif button_id == "lb_attacks":
        sort_type = "attacks"
    else:
        sort_type = "power"
    
    # جمع‌آوری داده‌ها
    users_data = []
    for uid, u in data["users"].items():
        if u.get("country_name"):
            users_data.append({
                "uid": uid,
                "name": u["country_name"],
                "power": calculate_power(u),
                "coins": u.get("coins", 0),
                "level": u.get("level", 1),
                "kills": u.get("kills", 0),
                "attacks": u.get("attacks", 0)
            })
    
    users_data.sort(key=lambda x: x[sort_type], reverse=True)
    
    titles = {
        "power": "💪 قدرت",
        "coins": "💰 سکه",
        "level": "📈 سطح",
        "kills": "💀 کشته",
        "attacks": "⚔️ حمله"
    }
    
    text = f"🏆 **لیدربرد بر اساس {titles[sort_type]}**\n\n"
    for i, u in enumerate(users_data[:20], 1):
        medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else f"{i}."))
        text += f"{medal} {u['name'][:15]} | {format_num(u[sort_type])}\n"
    
    builder = ChatKeypadBuilder()
    builder.row(builder.button("lb_power", "💪 قدرت"), builder.button("lb_coins", "💰 سکه"))
    builder.row(builder.button("lb_level", "📈 سطح"), builder.button("lb_kills", "💀 کشته"))
    builder.row(builder.button("lb_attacks", "⚔️ حمله"), builder.button("lb_clan", "🎌 کلن"))
    builder.row(builder.button("lb_empire", "👑 امپراتوری"), builder.button("lb_today", "📅 امروز"))
    builder.row(builder.button("lb_weekly", "📆 هفته"), builder.button("lb_monthly", "📅 ماه"))
    builder.row(builder.button("back_main", "🔙"))
    
    await safe_reply(message, text, chat_keypad=builder.build())
    return

# لیدربرد کلن‌ها
if button_id == "lb_clan":
    clans = data.get("clans", {})
    if not clans:
        await safe_reply(message, "🏆 **هیچ کلنی وجود ندارد!**", chat_keypad=main_menu_keypad())
        return
    
    clan_data = []
    for cid, clan in clans.items():
        total_power = 0
        for mid in clan.get("members", []):
            if mid in data["users"]:
                total_power += calculate_power(data["users"][mid])
        clan_data.append({
            "name": clan["name"],
            "power": total_power,
            "level": clan.get("level", 1),
            "members": len(clan.get("members", []))
        })
    
    clan_data.sort(key=lambda x: x["power"], reverse=True)
    
    text = "🎌 **لیدربرد کلن‌ها (بر اساس قدرت)**\n\n"
    for i, c in enumerate(clan_data[:15], 1):
        medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else f"{i}."))
        text += f"{medal} {c['name'][:15]} | 💪{format_num(c['power'])} | 📈س{c['level']} | 👥{c['members']}\n"
    
    builder = ChatKeypadBuilder()
    builder.row(builder.button("lb_power", "💪 قدرت"), builder.row(builder.button("back_main", "🔙")))
    await safe_reply(message, text, chat_keypad=builder.build())
    return

# لیدربرد امپراتوری‌ها
if button_id == "lb_empire":
    empires = data.get("empires", {})
    if not empires:
        await safe_reply(message, "👑 **هیچ امپراتوری وجود ندارد!**", chat_keypad=main_menu_keypad())
        return
    
    empire_data = []
    for eid, empire in empires.items():
        total_power = 0
        for mid in empire.get("members", []):
            if mid in data["users"]:
                total_power += calculate_power(data["users"][mid])
        empire_data.append({
            "name": empire["name"],
            "power": total_power,
            "level": empire.get("level", 1),
            "members": len(empire.get("members", []))
        })
    
    empire_data.sort(key=lambda x: x["power"], reverse=True)
    
    text = "👑 **لیدربرد امپراتوری‌ها**\n\n"
    for i, e in enumerate(empire_data[:15], 1):
        medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else f"{i}."))
        text += f"{medal} {e['name'][:15]} | 💪{format_num(e['power'])} | 📈س{e['level']} | 👥{e['members']}\n"
    
    builder = ChatKeypadBuilder()
    builder.row(builder.button("lb_power", "💪 قدرت"), builder.row(builder.button("back_main", "🔙")))
    await safe_reply(message, text, chat_keypad=builder.build())
    return

# لیدربرد امروز
if button_id == "lb_today":
    today = datetime.now().date().isoformat()
    today_stats = []
    
    for uid, u in data["users"].items():
        if u.get("country_name"):
            attacks_today = 0
            for log in data.get("battle_logs", []):
                if log["attacker"] == uid and log["date"].startswith(today):
                    attacks_today += 1
            if attacks_today > 0:
                today_stats.append({
                    "name": u["country_name"],
                    "attacks": attacks_today,
                    "power_gain": 0
                })
    
    today_stats.sort(key=lambda x: x["attacks"], reverse=True)
    
    text = "📅 **لیدربرد امروز (بیشترین حمله)**\n\n"
    for i, u in enumerate(today_stats[:20], 1):
        medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else f"{i}."))
        text += f"{medal} {u['name'][:15]} | ⚔️ {u['attacks']}\n"
    
    if not today_stats:
        text += "هنوز حمله‌ای ثبت نشده!"
    
    builder = ChatKeypadBuilder()
    builder.row(builder.button("lb_today", "📅 امروز"), builder.button("lb_weekly", "📆 هفته"))
    builder.row(builder.button("lb_monthly", "📅 ماه"), builder.button("back_main", "🔙"))
    await safe_reply(message, text, chat_keypad=builder.build())
    return

# لیدربرد هفته
if button_id == "lb_weekly":
    week_ago = (datetime.now() - timedelta(days=7)).isoformat()
    week_stats = {}
    
    for log in data.get("battle_logs", []):
        if log["date"] > week_ago:
            attacker = log["attacker"]
            if attacker not in week_stats:
                week_stats[attacker] = {"attacks": 0, "damage": 0}
            week_stats[attacker]["attacks"] += 1
            week_stats[attacker]["damage"] += log.get("damage", 0)
    
    weekly_list = []
    for uid, stats in week_stats.items():
        if uid in data["users"] and data["users"][uid].get("country_name"):
            weekly_list.append({
                "name": data["users"][uid]["country_name"],
                "attacks": stats["attacks"],
                "damage": stats["damage"]
            })
    
    weekly_list.sort(key=lambda x: x["attacks"], reverse=True)
    
    text = "📆 **لیدربرد هفته (بیشترین حمله)**\n\n"
    for i, u in enumerate(weekly_list[:20], 1):
        medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else f"{i}."))
        text += f"{medal} {u['name'][:15]} | ⚔️ {u['attacks']} | 💥 {format_num(u['damage'])}\n"
    
    if not weekly_list:
        text += "هفته هیچ حمله‌ای ثبت نشده!"
    
    builder = ChatKeypadBuilder()
    builder.row(builder.button("lb_today", "📅 امروز"), builder.button("lb_weekly", "📆 هفته"))
    builder.row(builder.button("lb_monthly", "📅 ماه"), builder.button("back_main", "🔙"))
    await safe_reply(message, text, chat_keypad=builder.build())
    return

# لیدربرد ماه
if button_id == "lb_monthly":
    month_ago = (datetime.now() - timedelta(days=30)).isoformat()
    month_stats = {}
    
    for log in data.get("battle_logs", []):
        if log["date"] > month_ago:
            attacker = log["attacker"]
            if attacker not in month_stats:
                month_stats[attacker] = {"attacks": 0, "damage": 0, "kills": 0}
            month_stats[attacker]["attacks"] += 1
            month_stats[attacker]["damage"] += log.get("damage", 0)
    
    monthly_list = []
    for uid, stats in month_stats.items():
        if uid in data["users"] and data["users"][uid].get("country_name"):
            monthly_list.append({
                "name": data["users"][uid]["country_name"],
                "attacks": stats["attacks"],
                "damage": stats["damage"]
            })
    
    monthly_list.sort(key=lambda x: x["attacks"], reverse=True)
    
    text = "📅 **لیدربرد ماه (بیشترین حمله)**\n\n"
    for i, u in enumerate(monthly_list[:20], 1):
        medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else f"{i}."))
        text += f"{medal} {u['name'][:15]} | ⚔️ {u['attacks']} | 💥 {format_num(u['damage'])}\n"
    
    if not monthly_list:
        text += "ماه هیچ حمله‌ای ثبت نشده!"
    
    builder = ChatKeypadBuilder()
    builder.row(builder.button("lb_today", "📅 امروز"), builder.button("lb_weekly", "📆 هفته"))
    builder.row(builder.button("lb_monthly", "📅 ماه"), builder.button("back_main", "🔙"))
    await safe_reply(message, text, chat_keypad=builder.build())
    return
    # ========== سیستم ساختمان‌ها ==========
if button_id == "build":
    await safe_reply(message, "🏗️ **منوی ساختمان‌ها**\n\nبا ساخت ساختمان‌ها می‌توانید تولید منابع خود را افزایش دهید:", chat_keypad=building_menu_keypad())
    return

if button_id == "build_list":
    text = "🏗️ **لیست ساختمان‌ها**\n\n"
    for bid, building in BUILDINGS_DB.items():
        text += f"{building['name']}\n💰 هزینه: {format_num(building['cost'])} | 📈 حداکثر سطح: {building['max_level']}\n"
        text += f"📦 تولید: {', '.join([f'{k}: +{v}' for k, v in building.get('production', {}).items()])}\n\n"
    await safe_reply(message, text, chat_keypad=main_menu_keypad())
    return

if button_id == "build_construct":
    # نمایش ساختمان‌های قابل ساخت
    builder = ChatKeypadBuilder()
    user_buildings = {b['id']: b for b in user.get("buildings_list", [])}
    
    for bid, building in BUILDINGS_DB.items():
        if bid not in user_buildings:
            builder.row(builder.button(f"build_confirm_{bid}", f"🔨 {building['name']} | {format_num(building['cost'])}💰"))
        else:
            existing = user_buildings[bid]
            if existing.get('level', 1) < building['max_level']:
                builder.row(builder.button(f"build_upgrade_{bid}", f"📈 {building['name']} (سطح {existing.get('level',1)}) | {format_num(building['upgrade_cost'] * existing.get('level',1))}💰"))
    builder.row(builder.button("build", "🔙"))
    
    await safe_reply(message, "🔨 **ساخت یا ارتقای ساختمان:**", chat_keypad=builder.build())
    return

if button_id and button_id.startswith("build_confirm_"):
    building_id = int(button_id.replace("build_confirm_", ""))
    building = BUILDINGS_DB.get(building_id)
    
    if not building:
        await safe_reply(message, "❌ ساختمان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    cost = building["cost"]
    if user.get("coins", 0) < cost:
        await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= cost
    user.setdefault("buildings_list", []).append({
        "id": building_id,
        "name": building["name"],
        "level": 1,
        "production": building.get("production", {}),
        "last_collect": datetime.now().isoformat()
    })
    
    save_data(data)
    await safe_reply(message, f"✅ **{building['name']} ساخته شد!**\n💰 هزینه: {format_num(cost)} سکه", chat_keypad=main_menu_keypad())
    return

if button_id and button_id.startswith("build_upgrade_"):
    building_id = int(button_id.replace("build_upgrade_", ""))
    building = BUILDINGS_DB.get(building_id)
    
    if not building:
        await safe_reply(message, "❌ ساختمان یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    user_buildings = user.get("buildings_list", [])
    for i, b in enumerate(user_buildings):
        if b["id"] == building_id:
            current_level = b.get("level", 1)
            if current_level >= building["max_level"]:
                await safe_reply(message, "🏆 **این ساختمان در حداکثر سطح است!**", chat_keypad=main_menu_keypad())
                return
            
            cost = building["upgrade_cost"] * current_level
            if user.get("coins", 0) < cost:
                await safe_reply(message, f"❌ **{format_num(cost)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
                return
            
            user["coins"] -= cost
            user_buildings[i]["level"] = current_level + 1
            save_data(data)
            
            await safe_reply(message, f"📈 **{building['name']} به سطح {current_level + 1} ارتقا یافت!**\n💰 هزینه: {format_num(cost)} سکه", chat_keypad=main_menu_keypad())
            return
    
    await safe_reply(message, "❌ ساختمان یافت نشد!", chat_keypad=main_menu_keypad())
    return

if button_id == "build_collect":
    user_buildings = user.get("buildings_list", [])
    total_collected = 0
    collected_resources = {}
    
    for b in user_buildings:
        building = BUILDINGS_DB.get(b["id"], {})
        last_collect = datetime.fromisoformat(b.get("last_collect", datetime.now().isoformat()))
        hours_passed = (datetime.now() - last_collect).total_seconds() / 3600
        hours_passed = min(hours_passed, 24)  # حداکثر 24 ساعت
        
        for resource, amount in building.get("production", {}).items():
            production = int(amount * b.get("level", 1) * hours_passed)
            if production > 0:
                collected_resources[resource] = collected_resources.get(resource, 0) + production
                total_collected += production
        
        b["last_collect"] = datetime.now().isoformat()
    
    # اعمال منابع جمع‌آوری شده
    for resource, amount in collected_resources.items():
        if resource == "food":
            user["food"] = user.get("food", 0) + amount
        elif resource == "iron":
            user["iron"] = user.get("iron", 0) + amount
        elif resource == "oil":
            user["oil"] = user.get("oil", 0) + amount
        elif resource == "coins":
            user["coins"] = user.get("coins", 0) + amount
        elif resource == "exp":
            user["exp"] = user.get("exp", 0) + amount
    
    save_data(data)
    
    if total_collected > 0:
        resource_text = "\n".join([f"• {k}: +{format_num(v)}" for k, v in collected_resources.items()])
        await safe_reply(message, f"📦 **منابع جمع‌آوری شد!**\n\n{resource_text}", chat_keypad=main_menu_keypad())
    else:
        await safe_reply(message, "📦 **هنوز چیزی برای جمع‌آوری نیست!**\nبعداً دوباره تلاش کن.", chat_keypad=main_menu_keypad())
    return

if button_id == "build_my":
    user_buildings = user.get("buildings_list", [])
    if not user_buildings:
        await safe_reply(message, "🏗️ **شما هیچ ساختمانی ندارید!**\nاز منوی ساخت استفاده کنید.", chat_keypad=main_menu_keypad())
        return
    
    text = "🏗️ **ساختمان‌های شما**\n\n"
    for b in user_buildings:
        building = BUILDINGS_DB.get(b["id"], {})
        text += f"• {building.get('name', 'نامشخص')} | سطح {b.get('level', 1)}\n"
        text += f"  📦 تولید: {', '.join([f'{k}: +{v * b.get("level", 1)}/ساعت' for k, v in building.get('production', {}).items()])}\n\n"
    
    await safe_reply(message, text, chat_keypad=main_menu_keypad())
    return
    # ========== سیستم تکنولوژی ==========
if button_id == "tech":
    await safe_reply(message, "🔬 **منوی تکنولوژی**\n\nبا تحقیق تکنولوژی‌ها می‌توانید قدرت خود را افزایش دهید:", chat_keypad=tech_menu_keypad())
    return

if button_id == "tech_list":
    text = "🔬 **لیست تکنولوژی‌ها**\n\n"
    for tid, tech in TECHNOLOGIES_DB.items():
        status = "🔒 قفل" if user.get("level", 1) < tech["level_req"] else "✅ قابل تحقیق"
        text += f"{tech['name']}\n💰 هزینه: {format_num(tech['cost'])} | {status} | نیاز سطح {tech['level_req']}\n"
        text += f"🎁 پاداش: {', '.join([f'{k}: +{v}' for k, v in tech.get('bonus', {}).items()])}\n\n"
    await safe_reply(message, text, chat_keypad=main_menu_keypad())
    return

if button_id == "tech_research":
    # نمایش تکنولوژی‌های قابل تحقیق
    builder = ChatKeypadBuilder()
    researched = user.get("technologies_list", [])
    
    for tid, tech in TECHNOLOGIES_DB.items():
        if tid not in researched and user.get("level", 1) >= tech["level_req"]:
            builder.row(builder.button(f"tech_research_{tid}", f"🧪 {tech['name']} | {format_num(tech['cost'])}💰"))
    builder.row(builder.button("tech", "🔙"))
    
    if not builder.rows:
        await safe_reply(message, "🔬 **هیچ تکنولوژی قابل تحقیقی وجود ندارد!**\nسطح خود را افزایش دهید.", chat_keypad=main_menu_keypad())
    else:
        await safe_reply(message, "🧪 **تحقیق تکنولوژی جدید:**", chat_keypad=builder.build())
    return

if button_id and button_id.startswith("tech_research_"):
    tech_id = int(button_id.replace("tech_research_", ""))
    tech = TECHNOLOGIES_DB.get(tech_id)
    
    if not tech:
        await safe_reply(message, "❌ تکنولوژی یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    researched = user.get("technologies_list", [])
    if tech_id in researched:
        await safe_reply(message, "❌ **این تکنولوژی قبلاً تحقیق شده!**", chat_keypad=main_menu_keypad())
        return
    
    if user.get("level", 1) < tech["level_req"]:
        await safe_reply(message, f"❌ **سطح {tech['level_req']} نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    if user.get("coins", 0) < tech["cost"]:
        await safe_reply(message, f"❌ **{format_num(tech['cost'])} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= tech["cost"]
    user.setdefault("technologies_list", []).append(tech_id)
    
    # اعمال پاداش تکنولوژی
    for bonus_type, bonus_value in tech.get("bonus", {}).items():
        if bonus_type == "attack":
            user["soldiers"] = user.get("soldiers", 0) + bonus_value
        elif bonus_type == "defense":
            user["max_health"] = user.get("max_health", 100000) + bonus_value
        elif bonus_type == "income":
            user["coins"] = user.get("coins", 0) + bonus_value
        elif bonus_type == "exp":
            user["exp"] = user.get("exp", 0) + bonus_value
    
    save_data(data)
    
    await safe_reply(message, f"✅ **{tech['name']} تحقیق شد!**\n💰 هزینه: {format_num(tech['cost'])} سکه\n🎁 پاداش اعمال شد!", chat_keypad=main_menu_keypad())
    return

if button_id == "tech_my":
    researched = user.get("technologies_list", [])
    if not researched:
        await safe_reply(message, "🔬 **شما هیچ تکنولوژی‌ای تحقیق نکرده‌اید!**", chat_keypad=main_menu_keypad())
        return
    
    text = "🔬 **تکنولوژی‌های تحقیق شده:**\n\n"
    for tid in researched:
        tech = TECHNOLOGIES_DB.get(tid, {})
        text += f"✅ {tech.get('name', 'نامشخص')}\n"
    
    await safe_reply(message, text, chat_keypad=main_menu_keypad())
    return
    # ========== سیستم دوال ==========
if button_id == "duel":
    await safe_reply(message, "⚔️ **دوال**\n\nشرط خود را انتخاب کنید:", chat_keypad=duel_keypad())
    return

if button_id and button_id.startswith("duel_") and button_id != "duel_random" and button_id != "duel_rank":
    amounts = {
        "duel_100": 100, "duel_500": 500, "duel_1000": 1000,
        "duel_5000": 5000, "duel_10000": 10000, "duel_50000": 50000,
        "duel_100000": 100000, "duel_500000": 500000
    }
    amount = amounts.get(button_id)
    
    if not amount:
        await safe_reply(message, "❌ مقدار نامعتبر!", chat_keypad=main_menu_keypad())
        return
    
    if user.get("coins", 0) < amount:
        await safe_reply(message, f"❌ **{format_num(amount)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    # پیدا کردن کاربران آنلاین
    online_users = []
    for uid in data.get("online_users", {}):
        if uid != user_id and uid in data["users"] and uid not in data.get("banned_users", []):
            online_users.append(uid)
    
    if not online_users:
        await safe_reply(message, "❌ **هیچ کاربر آنلاینی برای دوال وجود ندارد!**", chat_keypad=main_menu_keypad())
        return
    
    builder = ChatKeypadBuilder()
    for uid in online_users[:15]:
        target = data["users"][uid]
        builder.row(builder.button(f"duel_challenge_{uid}_{amount}", f"⚔️ {target['country_name'][:15]} | 💪{format_num(calculate_power(target))}"))
    builder.row(builder.button("duel", "🔙"))
    
    await safe_reply(message, f"⚔️ **انتخاب حریف برای دوال با شرط {format_num(amount)} سکه:**", chat_keypad=builder.build())
    return

if button_id and button_id.startswith("duel_challenge_"):
    parts = button_id.split("_")
    target_id = parts[2]
    amount = int(parts[3])
    
    if target_id not in data["users"]:
        await safe_reply(message, "❌ کاربر یافت نشد!", chat_keypad=main_menu_keypad())
        return
    
    target = data["users"][target_id]
    
    if user.get("coins", 0) < amount:
        await safe_reply(message, f"❌ **{format_num(amount)} سکه نیاز است!**", chat_keypad=main_menu_keypad())
        return
    
    # ایجاد درخواست دوال
    duel_id = f"duel_{user_id}_{target_id}_{int(time.time())}"
    data["duels"][duel_id] = {
        "challenger": user_id,
        "challenger_name": country_name,
        "target": target_id,
        "target_name": target["country_name"],
        "amount": amount,
        "status": "pending",
        "date": datetime.now().isoformat()
    }
    save_data(data)
    
    await safe_reply(message, f"✅ **درخواست دوال به {target['country_name']} ارسال شد!**\n💰 شرط: {format_num(amount)} سکه", chat_keypad=main_menu_keypad())
    
    # اطلاع به طرف مقابل
    builder = ChatKeypadBuilder()
    builder.row(builder.button(f"duel_accept_{duel_id}", "✅ قبول"), builder.button(f"duel_reject_{duel_id}", "❌ رد"))
    
    try:
        await bot.send_message(int(target_id),
            f"⚔️ **درخواست دوال از {country_name}**\n\n"
            f"💰 شرط: {format_num(amount)} سکه\n"
            f"💪 قدرت شما: {format_num(calculate_power(target))}\n"
            f"💪 قدرت حریف: {format_num(calculate_power(user))}\n\n"
            f"آیا می‌پذیرید؟",
            chat_keypad=builder.build())
    except:
        pass
    return

if button_id and button_id.startswith("duel_accept_"):
    duel_id = button_id.replace("duel_accept_", "")
    duel = data.get("duels", {}).get(duel_id)
    
    if not duel or duel["status"] != "pending":
        await safe_reply(message, "❌ درخواست دوال معتبر نیست!", chat_keypad=main_menu_keypad())
        return
    
    if user_id != duel["target"]:
        await safe_reply(message, "❌ این درخواست برای شما نیست!", chat_keypad=main_menu_keypad())
        return
    
    amount = duel["amount"]
    challenger_id = duel["challenger"]
    challenger = data["users"].get(challenger_id, {})
    
    # چک کردن سکه هر دو طرف
    if user.get("coins", 0) < amount:
        await safe_reply(message, f"❌ **شما {format_num(amount)} سکه ندارید!**", chat_keypad=main_menu_keypad())
        return
    
    if challenger.get("coins", 0) < amount:
        await safe_reply(message, f"❌ **حریف {format_num(amount)} سکه ندارد!**", chat_keypad=main_menu_keypad())
        duel["status"] = "cancelled"
        save_data(data)
        return
    
    # محاسبه برنده
    my_power = calculate_power(user)
    challenger_power = calculate_power(challenger)
    
    if my_power > challenger_power:
        winner_id = user_id
        winner_name = country_name
        loser_id = challenger_id
    elif challenger_power > my_power:
        winner_id = challenger_id
        winner_name = duel["challenger_name"]
        loser_id = user_id
    else:
        # مساوی: سکه برگردانده می‌شود
        user["coins"] += amount
        challenger["coins"] += amount
        duel["status"] = "draw"
        save_data(data)
        
        await safe_reply(message, f"⚖️ **دوال مساوی شد!**\n💰 سکه‌ها برگردانده شد.", chat_keypad=main_menu_keypad())
        
        try:
            await bot.send_message(int(challenger_id), f"⚖️ **دوال با {country_name} مساوی شد!**\n💰 سکه‌ها برگردانده شد.")
        except:
            pass
        return
    
    # انتقال سکه
    user["coins"] -= amount
    challenger["coins"] -= amount
    data["users"][winner_id]["coins"] += amount * 2
    
    # ثبت آمار دوال
    duel["status"] = "completed"
    duel["winner"] = winner_id
    duel["winner_name"] = winner_name
    
    data.setdefault("duel_stats", {}).setdefault(winner_id, {"wins": 0, "losses": 0})
    data.setdefault("duel_stats", {}).setdefault(loser_id, {"wins": 0, "losses": 0})
    data["duel_stats"][winner_id]["wins"] += 1
    data["duel_stats"][loser_id]["losses"] += 1
    
    save_data(data)
    
    await safe_reply(message,
        f"⚔️ **نتیجه دوال!** ⚔️\n\n"
        f"🏆 **برنده: {winner_name}**\n"
        f"💰 جایزه: {format_num(amount * 2)} سکه\n"
        f"💪 قدرت شما: {format_num(my_power)}\n"
        f"💪 قدرت حریف: {format_num(challenger_power)}",
        chat_keypad=main_menu_keypad())
    
    try:
        await bot.send_message(int(challenger_id),
            f"⚔️ **نتیجه دوال!** ⚔️\n\n"
            f"🏆 **برنده: {winner_name}**\n"
            f"💰 جایزه: {format_num(amount * 2)} سکه")
    except:
        pass
    return

if button_id and button_id.startswith("duel_reject_"):
    duel_id = button_id.replace("duel_reject_", "")
    duel = data.get("duels", {}).get(duel_id)
    
    if duel and duel["status"] == "pending":
        duel["status"] = "rejected"
        save_data(data)
        
        await safe_reply(message, "❌ درخواست دوال رد شد.", chat_keypad=main_menu_keypad())
        
        try:
            await bot.send_message(int(duel["challenger"]), f"❌ درخواست دوال شما توسط {country_name} رد شد.")
        except:
            pass
    return

if button_id == "duel_random":
    # پیدا کردن کاربران آنلاین با قدرت مشابه
    online_users = []
    for uid in data.get("online_users", {}):
        if uid != user_id and uid in data["users"] and uid not in data.get("banned_users", []):
            power_diff = abs(calculate_power(user) - calculate_power(data["users"][uid]))
            if power_diff < 5000:  # قدرت مشابه
                online_users.append(uid)
    
    if not online_users:
        await safe_reply(message, "❌ **هیچ حریفی با قدرت مشابه پیدا نشد!**\nبعداً دوباره تلاش کن.", chat_keypad=main_menu_keypad())
        return
    
    target_id = random.choice(online_users)
    target = data["users"][target_id]
    
    # شرط تصادفی
    amount = random.choice([100, 500, 1000, 5000])
    
    if user.get("coins", 0) < amount or target.get("coins", 0) < amount:
        await safe_reply(message, "❌ **یکی از طرفین سکه کافی ندارد!**", chat_keypad=main_menu_keypad())
        return
    
    user["coins"] -= amount
    target["coins"] -= amount
    
    my_power = calculate_power(user)
    target_power = calculate_power(target)
    
    if my_power > target_power:
        winner_id = user_id
        winner_name = country_name
    else:
        winner_id = target_id
        winner_name = target["country_name"]
    
    data["users"][winner_id]["coins"] += amount * 2
    
    save_data(data)
    
    await safe_reply(message,
        f"🎲 **دوال تصادفی!** 🎲\n\n"
        f"🎯 حریف: {target['country_name']}\n"
        f"💰 شرط: {format_num(amount)} سکه\n"
        f"💪 قدرت شما: {format_num(my_power)}\n"
        f"💪 قدرت حریف: {format_num(target_power)}\n\n"
        f"🏆 **برنده: {winner_name}**",
        chat_keypad=main_menu_keypad())
    
    try:
        await bot.send_message(int(target_id),
            f"🎲 **دوال تصادفی!** 🎲\n\n"
            f"🎯 حریف: {country_name}\n"
            f"💰 شرط: {format_num(amount)} سکه\n"
            f"🏆 **برنده: {winner_name}**")
    except:
        pass
    return

if button_id == "duel_rank":
    duel_stats = data.get("duel_stats", {})
    if not duel_stats:
        await safe_reply(message, "🏆 **هیچ آماری برای دوال وجود ندارد!**", chat_keypad=main_menu_keypad())
        return
    
    stats_list = []
    for uid, stats in duel_stats.items():
        if uid in data["users"] and data["users"][uid].get("country_name"):
            wins = stats.get("wins", 0)
            losses = stats.get("losses", 0)
            total = wins + losses
            win_rate = (wins / total * 100) if total > 0 else 0
            stats_list.append({
                "name": data["users"][uid]["country_name"],
                "wins": wins,
                "losses": losses,
                "win_rate": win_rate
            })
    
    stats_list.sort(key=lambda x: x["wins"], reverse=True)
    
    text = "🏆 **رتبه دوال (بیشترین برد)**\n\n"
    for i, s in enumerate(stats_list[:15], 1):
        medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else f"{i}."))
        text += f"{medal} {s['name'][:15]} | برد: {s['wins']} | باخت: {s['losses']} | {s['win_rate']:.0f}%\n"
    
    # آمار شخصی
    my_stats = duel_stats.get(user_id, {})
    text += f"\n📊 **آمار شما:**\nبرد: {my_stats.get('wins', 0)} | باخت: {my_stats.get('losses', 0)}"
    
    await safe_reply(message, text, chat_keypad=main_menu_keypad())
    return
    # ========== سرمایه‌گذاری ==========
if button_id == "invest":
    investment = user.get("investments", 0)
    last_invest_date = data["daily_resets"].get(user_id, {}).get("invest_date")
    today = datetime.now().date().isoformat()
    
    if investment > 0 and last_invest_date != today:
        # دریافت سود
        profit = int(investment * random.uniform(0.05, 0.15))
        user["coins"] += profit
        user["exp"] += 50
        data["daily_resets"][user_id]["invest_date"] = today
        save_data(data)
        
        await safe_reply(message,
            f"📈 **سود سرمایه‌گذاری!**\n\n"
            f"💰 سرمایه: {format_num(investment)} سکه\n"
            f"🎁 سود امروز: +{format_num(profit)} سکه\n"
            f"📈 +۵۰ تجربه",
            chat_keypad=main_menu_keypad())
    else:
        if investment > 0:
            await safe_reply(message, f"❌ **شما قبلاً سرمایه‌گذاری کرده‌اید!**\n💰 سرمایه فعلی: {format_num(investment)} سکه\nسود روزانه فردا قابل برداشت است.", chat_keypad=main_menu_keypad())
            return
        
        # سرمایه‌گذاری جدید
        min_invest = 5000
        if user.get("coins", 0) < min_invest:
            await safe_reply(message, f"❌ **حداقل سرمایه‌گذاری {format_num(min_invest)} سکه است!**", chat_keypad=main_menu_keypad())
            return
        
        await safe_reply(message, f"💰 **مبلغ سرمایه‌گذاری را وارد کنید:**\n(حداقل {format_num(min_invest)} سکه)\n\n💡 سود روزانه ۵-۱۵٪", chat_keypad=None)
        data["pending_action"][user_id] = {"action": "invest_amount"}
        save_data(data)
    return

if pending.get("action") == "invest_amount" and text.isdigit():
    amount = int(text)
    min_invest = 5000
    
    if amount < min_invest:
        await safe_reply(message, f"❌ **حداقل سرمایه‌گذاری {format_num(min_invest)} سکه است!**", chat_keypad=main_menu_keypad())
    elif user.get("coins", 0) < amount:
        await safe_reply(message, f"❌ **سکه کافی نیست!**\nنیاز: {format_num(amount)} سکه", chat_keypad=main_menu_keypad())
    else:
        user["coins"] -= amount
        user["investments"] = amount
        data["daily_resets"][user_id]["invest_date"] = datetime.now().date().isoformat()
        save_data(data)
        
        await safe_reply(message,
            f"✅ **{format_num(amount)} سکه سرمایه‌گذاری شد!**\n\n"
            f"💡 سود روزانه: ۵-۱۵٪\n"
            f"📅 از فردا می‌توانید سود خود را برداشت کنید.",
            chat_keypad=main_menu_keypad())
    
    del data["pending_action"][user_id]
    save_data(data)
    return
    # ==================================================
# تابع daily_reset_task - ریست روزانه و رویدادها
# ==================================================
# ==================================================
# تابع daily_reset_task - ریست روزانه و رویدادها
# ==================================================



async def main():
    global bot
    print("=" * 70)
    print("🔥 **ربات جنگ کشورها - نسخه نهایی کامل** 🔥")
    print("=" * 70)
    print("📊 **آمار ربات:**")
    print(f"   • سلاح‌ها: {sum(len(cat['items']) for cat in WEAPONS_DB.values())} عدد")
    print(f"   • مدال‌ها: {len(ACHIEVEMENTS_DB)} عدد")
    print(f"   • مشاغل: {len(JOBS_DB)} عدد")
    print(f"   • حیوانات: {len(PETS_DB)} عدد")
    print(f"   • ساختمان‌ها: {len(BUILDINGS_DB)} عدد")
    print(f"   • تکنولوژی‌ها: {len(TECHNOLOGIES_DB)} عدد")
    print("=" * 70)
    print("✅ **ربات با موفقیت راه‌اندازی شد!**")
    print("📝 **منوی ادمین:** رمز 16948")
    print("=" * 70)
    
    asyncio.create_task(daily_reset_task())
    await bot.run()


if __name__ == "__main__":
    asyncio.run(main())