import requests
import time

TOKEN = "8522684488:AAGBLIhapSR42j6HAWAcNHl-ipqJN8eU828"
CHAT_ID = "7216850185"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

while True:
    send_message("📡 Scanning market...")

    try:
        # FREE WORKING API
        url = "https://query1.finance.yahoo.com/v7/finance/screener/predefined/saved?count=10&scrIds=day_gainers"
        data = requests.get(url).json()

        stocks = data["finance"]["result"][0]["quotes"]

        for stock in stocks:
            price = stock.get("regularMarketPrice", 0)

            if price and price < 5:
                send_message(
                    f"🚀 {stock['symbol']} | ${price}"
                )

    except Exception as e:
        send_message(f"Error: {e}")

    time.sleep(300)
