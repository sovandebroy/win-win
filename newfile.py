import os
import random
from datetime import datetime, timedelta
import pytz
import asyncio
import threading
from flask import Flask
from telegram.ext import ApplicationBuilder
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode

# ==========================================
# 🌐 Flask Web Server
# ==========================================
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "Bot status: ONLINE (Win Signal Master 24/7 Time & Perfect Period Sync Active)"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app_web.run(host='0.0.0.0', port=port)


# ==========================================
# 🤖 Telegram Bot Configurations
# ==========================================
# 🟢 আপনার বট টোকেন এবং আপডেট করা প্রাইভেট চ্যানেল আইডি (-100 সহ)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8896208550:AAEE5IJhBW5jgdTBMnyr59g2qhhq7PjgtDA")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "-1004477616247")  # 👈 এখানে আপনার প্রাইভেট চ্যানেল আইডি বসানো হয়েছে
BOT_USERNAME = "win_signal_master_bot"

TOKEN = BOT_TOKEN.strip()

current_pattern = []
pattern_index = 0


# ==========================================
# ⏰ Time & Live Game Period Synchronization Function
# ==========================================
def get_bd_time():
    try:
        bd_tz = pytz.timezone('Asia/Dhaka')
        return datetime.now(bd_tz)
    except Exception:
        return datetime.utcnow() + timedelta(hours=6)

def get_current_1min_period():
    now_utc = datetime.now(pytz.utc)
    date_str = now_utc.strftime("%Y%m%d")
    
    total_minutes_utc = (now_utc.hour * 60) + now_utc.minute
    period_count = 10000 + total_minutes_utc + 1
    
    return f"{date_str}1000{period_count}"


# ==========================================
# 📊 Advanced AI Trend Evaluator (10 Strategies)
# ==========================================
def high_tech_ai_trend_evaluator():
    strategies_weights = {
        "DRAGON_TREND": 15,       
        "THREE_BY_THREE": 12,     
        "CROSS_WAVE": 12,         
        "TWO_BY_TWO_ZONE": 10,    
        "STABLE_ZIGZAG": 10,      
        "SMART_MIXED": 10,
        "MIRROR_REFLECTION": 8,
        "FIBONACCI_STEP": 8,
        "MOMENTUM_WAVE": 8,
        "ALTERNATE_CLUSTER": 7
    }

    strategies = list(strategies_weights.keys())
    weights = list(strategies_weights.values())
    selected_strategy = random.choices(strategies, weights=weights, k=1)[0]

    start = random.choice(["BIG", "SMALL"])
    opposite = "SMALL" if start == "BIG" else "BIG"
    
    if selected_strategy == "DRAGON_TREND":
        dragon_len = random.randint(5, 7)
        pattern = [start] * dragon_len
    elif selected_strategy == "THREE_BY_THREE":
        pattern = [start, start, start, opposite, opposite, opposite]
    elif selected_strategy == "CROSS_WAVE":
        pattern = [start, start, opposite, opposite, opposite, start]
    elif selected_strategy == "TWO_BY_TWO_ZONE":
        pattern = [start, start, opposite, opposite, start, start, opposite, opposite]
    elif selected_strategy == "STABLE_ZIGZAG":
        pattern = [start, opposite, start, opposite, start, opposite, start]
    elif selected_strategy == "MIRROR_REFLECTION":
        pattern = [start, opposite, start, start, opposite, start]
    elif selected_strategy == "FIBONACCI_STEP":
        pattern = [start, start, opposite, start, opposite, opposite]
    elif selected_strategy == "MOMENTUM_WAVE":
        pattern = [start, opposite, opposite, start, start, opposite]
    elif selected_strategy == "ALTERNATE_CLUSTER":
        pattern = [start, start, opposite, opposite, start, opposite]
    else:
        pattern = [start, opposite, start, start, opposite, start]

    return pattern

def get_high_tech_ai_prediction():
    global current_pattern, pattern_index
    if not current_pattern or pattern_index >= len(current_pattern):
        current_pattern = high_tech_ai_trend_evaluator()
        pattern_index = 0
    
    raw_prediction = current_pattern[pattern_index]
    pattern_index += 1
    return raw_prediction


# ==========================================
# 🎨 Smart Color Evaluator Logic (Only Green & Red)
# ==========================================
def get_smart_trend_color(pred_text):
    if pred_text == "BIG":
        return random.choice(["GREEN 🟢", "GREEN 🟢", "RED 🔴"])
    else:
        return random.choice(["RED 🔴", "RED 🔴", "GREEN 🟢"])


# ==========================================
# 📢 Extra Supporting Message Functions
# ==========================================
async def send_level_chart_alert(app, markup):
    chart_msg = (
        f"💎 <b>WIN SIGNAL MASTER VIP 10-LEVEL MARTINGALE</b> 💎\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🛡️ <b>OFFICIAL MONEY MANAGEMENT CHART</b>\n\n"
        f"🎯 <i>Strictly follow this Martingale plan to protect your capital & maximize daily profits!</i>\n\n"
        f"📊 <b>LEVEL BREAKDOWN:</b>\n"
        f"▫️ <b>Level 1  ➜</b>  ₹1\n"
        f"▫️ <b>Level 2  ➜</b>  ₹3\n"
        f"▫️ <b>Level 3  ➜</b>  ₹7\n"
        f"▫️ <b>Level 4  ➜</b>  ₹16\n"
        f"▫️ <b>Level 5  ➜</b>  ₹40\n"
        f"▫️ <b>Level 6  ➜</b>  ₹85\n"
        f"▫️ <b>Level 7  ➜</b>  ₹200\n"
        f"▫️ <b>Level 8  ➜</b>  ₹420\n"
        f"▫️ <b>Level 9  ➜</b>  ₹900\n"
        f"▫️ <b>Level 10 ➜</b>  ₹2000\n"
        f"▫️ <b>Level 11 ➜</b>  ₹4500\n"
        f"▫️ <b>Level 12 ➜</b>  ₹10000\n\n"
        f"💰 <b>TOTAL REQUIRED BALANCE:</b>\n"
        f"📌 <b>Up to Level 10 Total: ₹3,672</b>\n"
        f"📌 <b>Up to Level 12 Total: ₹18,172</b>"
    )
    try:
        await app.bot.send_message(chat_id=CHANNEL_ID, text=chart_msg, parse_mode=ParseMode.HTML, reply_markup=markup)
    except Exception as e:
        print(f"Level Chart Error: {e}")

async def send_referral_promo(app, markup):
    promo_msg = (
        f"💎 ✨ <b>MAXIMIZE YOUR EARNINGS WITH WIN SIGNAL MASTER!</b> ✨ 💎\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🇬🇧 <b>ENGLISH:</b>\n"
        f"Build your powerful team and generate passive daily income! Earn lifetime commissions, daily salaries, and referral bonuses. Share your link now!\n\n"
        f"🇮🇳 <b>हिंदी (HINDI):</b>\n"
        f"अपनी खुद की मजबूत टीम बनाएं और रोजाना पैसिव इनकम कमाएं! लाइफटाइम कमीशन, डेली सैलरी और रेफरल बोनस पाएं। अभी अपना लिंक शेयर करें!\n\n"
        f"🇮🇳 <b>বাংলা (BANGLA):</b>\n"
        f"একটি শক্তিশালী টিম তৈরি করুন এবং প্রতিদিন প্যাসিভ ইনকাম করুন! লাইফটাইম কমিশন, ডেইলি স্যালারি এবং রেফারেল বোনাস উপভোগ করুন। এখনই শেয়ার করুন!\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━"
    )
    try:
        await app.bot.send_message(chat_id=CHANNEL_ID, text=promo_msg, parse_mode=ParseMode.HTML, reply_markup=markup)
    except Exception as e:
        print(f"Promo Error: {e}")


# ==========================================
# 🚀 Telegram Automation Main Loop (24/7 Active)
# ==========================================
async def send_auto_prediction(app):
    last_sent_period = ""
    last_chart_hour = ""
    last_promo_hour = ""

    keyboard = [
        [InlineKeyboardButton("🤖 Start Win Signal Bot 🏆", url=f"https://t.me/{BOT_USERNAME}")],
        [InlineKeyboardButton("📊 Join VIP Channel", url="https://t.me/WinSignalMaster")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    alert_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Open Bot & Play", url=f"https://t.me/{BOT_USERNAME}")],
        [InlineKeyboardButton("📢 Channel Link", url="https://t.me/WinSignalMaster")]
    ])

    promo_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Start Bot Now", url=f"https://t.me/{BOT_USERNAME}")],
        [InlineKeyboardButton("💎 Contact For Support", url="https://t.me/WinSignalMaster")]
    ])

    print("Win Signal Master 24/7 Non-Stop Automation Loop started successfully...")

    while True:
        try:
            now = get_bd_time()
            current_hour = now.hour
            current_minute = now.minute
            current_date_str = now.strftime('%Y-%m-%d')

            # ১. প্রতি ১ মিনিটে অটোমেটিক সিগন্যাল পাঠানো
            period_num = get_current_1min_period()
            if period_num != last_sent_period:
                pred = get_high_tech_ai_prediction()
                pred_text = "SMALL" if pred == "SMALL" else "BIG"
                color_text = get_smart_trend_color(pred_text)
                
                msg = (
                    f"💎 <b>WIN SIGNAL MASTER ULTRA AI</b> 💎\n"
                    f"💎 <b>VIP 24/7 PREDICTION 1 Min</b> 💎\n\n"
                    f"🔹 <b>PERIOD:</b> {period_num}\n"
                    f"🎯 <b>PREDICTION:</b> {pred_text}\n"
                    f"🎨 <b>COLOR:</b> {color_text}\n"
                    f"───────────────────\n"
                    f"💡 <i>Recommended: Safe 1-10 Level Martingale</i>"
                )
                
                await app.bot.send_message(
                    chat_id=CHANNEL_ID,
                    text=msg,
                    parse_mode=ParseMode.HTML,
                    reply_markup=reply_markup
                )
                
                print(f"24/7 Signal sent successfully for period: {period_num}")
                last_sent_period = period_num

            # ২. মার্টিনগেল লেভেল চার্ট (প্রতি ৬ ঘণ্টায়: 0, 6, 12, 18 টা বাজে)
            if current_hour in [0, 6, 12, 18] and current_minute == 0:
                chart_key = f"{current_date_str}_{current_hour}"
                if last_chart_hour != chart_key:
                    await send_level_chart_alert(app, alert_markup)
                    last_chart_hour = chart_key

            # ৩. রেফারেল প্রমোশন বার্তা (প্রতি ৬ ঘণ্টায়: 3, 9, 15, 21 টা বাজে)
            if current_hour in [3, 9, 15, 21] and current_minute == 0:
                promo_key = f"{current_date_str}_{current_hour}"
                if last_promo_hour != promo_key:
                    await send_referral_promo(app, promo_markup)
                    last_promo_hour = promo_key

        except Exception as e:
            print(f"Loop Error: {e}")

        await asyncio.sleep(2)


# ==========================================
# ⚙️ Main Application Launcher
# ==========================================
async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    await app.initialize()
    await app.start()
    
    # ব্যাকগ্রাউন্ডে Flask ওয়েব সার্ভার চালু করা
    threading.Thread(target=run_web, daemon=True).start()
    
    print("Win Signal Master AI Bot (24/7 Mode) is fully running and active...")
    
    await send_auto_prediction(app)

if __name__ == "__main__":
    asyncio.run(main())
