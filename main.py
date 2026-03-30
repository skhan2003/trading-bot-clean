import requests
import time

TOKEN = "8522684488:AAGBLIhapSR42j6HAWAcNHl-ipqJN8eU828"
CHAT_ID = "7216850185"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

# STATIC WATCHLIST (reliable)
stocks = ["NIO", "SOFI", "LCID", "RIVN", "PLTR", "F"]

def get_price(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers).json()

        return res["quoteResponse"]["result"][0]["regularMarketPrice"]
    except:
        return None

while True:
    send_message("📡 Scanning market...")

    for stock in stocks:
        price = get_price(stock)

        if price and price < 5:
            send_message(f"🚀 {stock} | ${price}")

    time.sleep(300)
