import requests
import time

TOKEN = "8522684488:AAGBLIhapSR42j6HAWAcNHl-ipqJN8eU828"
CHAT_ID = "7216850185"

API_URL = "https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=wg6hAv7crwZdlFQcmoYwKdYqnK0cXaXD"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

while True:
    send_message("📡 Scanning market...")

    try:
        data = requests.get(API_URL).json()

        if isinstance(data, list):
            for stock in data[:5]:
                if stock.get("price", 0) < 5:
                    send_message(
                        f"🚀 {stock['symbol']} | ${stock['price']} | {stock['changesPercentage']}"
                    )
        else:
            send_message("⚠️ API error")

    except Exception as e:
        send_message(f"Error: {e}")

    time.sleep(300)
