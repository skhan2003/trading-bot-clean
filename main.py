import requests
import time
import os
from flask import Flask
import threading

# 🔑 USE ENV VARIABLE (safer)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = "7216850185"

stocks = ["NIO", "SOFI", "LCID", "RIVN", "PLTR"]

last_prices = {}

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
        print("Sent:", msg)
    except Exception as e:
        print("Send error:", e)

def get_price(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        res = requests.get(url, timeout=10)
        data = res.json()
        return round(data["chart"]["result"][0]["meta"]["regularMarketPrice"], 2)
    except Exception as e:
        print(f"{symbol} error:", e)
        return None

def scanner():
    send("🚀 BOT STARTED (LIVE SCANNER)")
    
    while True:
        print("Scanning market...")

        for s in stocks:
            price = get_price(s)

            if price:
                if s not in last_prices:
                    last_prices[s] = price

                change = abs(price - last_prices[s])

                # 🔥 Slightly more sensitive (better alerts)
                if change > 0.15:
                    send(f"🚀 {s} moved: ${last_prices[s]} → ${price}")
                    last_prices[s] = price
            else:
                print(f"{s} skipped")

        time.sleep(60)

# 🌐 Flask server (REQUIRED for free Render)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 🚀 Run both
threading.Thread(target=scanner).start()
run()
