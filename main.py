import requests
import time

TOKEN = "8522684488:AAGBLIhapSR42j6HAWAcNHl-ipqJN8eU828"
CHAT_ID = "7216850185"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def get_gainers():
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=AAPL,TSLA,AMD,NIO,PLTR,SOFI,F,LCID,RIVN"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []

    try:
        data = response.json()
        return data["quoteResponse"]["result"]
    except:
        return []

while True:
    send_message("📡 Scanning market...")

    stocks = get_gainers()

    if not stocks:
        send_message("⚠️ Data fetch failed, retrying...")
    else:
        for stock in stocks:
            price = stock.get("regularMarketPrice", 0)

            if price and price < 5:
                send_message(
                    f"🚀 {stock['symbol']} | ${price}"
                )

    time.sleep(300)
