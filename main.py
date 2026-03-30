import requests
import time

TOKEN = "YOUR_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def get_price(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
        res = requests.get(url)

        if res.status_code != 200:
            return None

        data = res.json()

        if "quoteResponse" not in data:
            return None

        result = data["quoteResponse"].get("result", [])

        if len(result) == 0:
            return None

        return result[0].get("regularMarketPrice")

    except Exception as e:
        return None

stocks = ["NIO", "SOFI", "LCID"]

while True:
    send("📡 Scanning market...")

    for s in stocks:
        price = get_price(s)

        if price:
            send(f"🚀 {s}: ${price}")
        else:
            send(f"⚠️ {s}: data error")

    time.sleep(120)
