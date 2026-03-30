import requests
import time

TOKEN = "8522684488:AAGBLIhapSR42j6HAWAcNHl-ipqJN8eU828"
CHAT_ID = "7216850185"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def get_price(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        headers = {"User-Agent": "Mozilla/5.0"}

        res = requests.get(url, headers=headers, timeout=5)
        data = res.json()

        result = data["chart"]["result"][0]
        price = result["meta"]["regularMarketPrice"]

        return price

    except:
        return None

stocks = ["NIO", "SOFI", "LCID", "RIVN", "PLTR"]

send("📡 Scanner started")

while True:
    for s in stocks:
        price = get_price(s)

        if price:
            send(f"🚀 {s}: ${price}")
        else:
            send(f"⚠️ {s}: data error")

    time.sleep(300)
