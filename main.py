import requests
import time

TOKEN = "8522684488:AAGBLIhapSR42j6HAWAcNHl-ipqJN8eU828"
CHAT_ID = "7216850185"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def get_price(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=5)

        if res.status_code != 200:
            return None

        data = res.json()
        result = data.get("quoteResponse", {}).get("result", [])

        if not result:
            return None

        return result[0].get("regularMarketPrice")

    except:
        return None

# 🔥 your watchlist (we can expand later)
stocks = ["NIO", "SOFI", "LCID", "RIVN", "PLTR"]

send("📡 Scanner started")

while True:
    for stock in stocks:
        price = get_price(stock)

        if price:
            # simple alert logic
            if price < 5:
                send(f"🚀 ALERT: {stock} under $5 → ${price}")
        else:
            send(f"⚠️ {stock} data error")

    time.sleep(300)  # every 5 minutes
