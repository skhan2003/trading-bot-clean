import requests
import time

# 🔑 YOUR DETAILS (already filled from your bot)
TOKEN = "8522684488:AAGBLIhapSR42j6HAWAcNHI-i"
CHAT_ID = "7216850185"

# 📊 Stocks to track
stocks = ["NIO", "SOFI", "LCID", "RIVN", "PLTR"]

# 🧠 Store last prices
last_prices = {}

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass

def get_price(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        res = requests.get(url, timeout=10)
        data = res.json()

        return round(data["chart"]["result"][0]["meta"]["regularMarketPrice"], 2)

    except:
        return None


# 🚀 START MESSAGE
send("🚀 PRO SCANNER STARTED")

while True:
    print("Scanning market...")

    for s in stocks:
        price = get_price(s)

        if price:
            if s not in last_prices:
                last_prices[s] = price

            change = abs(price - last_prices[s])

            # 🔥 ONLY SEND ALERT IF MOVE > $0.2
            if change > 0.2:
                send(f"🚀 {s} moved: ${last_prices[s]} → ${price}")
                last_prices[s] = price

        else:
            print(f"{s} API issue (skipped)")

    time.sleep(60)
