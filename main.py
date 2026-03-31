import requests
from flask import Flask
import threading
import time
from datetime import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1487535942536396810/VQ-wp-Nr4kkUr8w6hShPBYAQp-3_2zrI6C6-yN6Oi-3DY3Vb6zcTRwxz_ooGdG64qmRc"
API_KEY = "wg6hAv7crwZdlFQcmoYwKdYqnK0cXaXD"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def get_gappers():
    url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={API_KEY}"
    data = requests.get(url).json()

    results = []
    for stock in data:
        try:
            price = float(stock["price"])
            change = float(stock["changesPercentage"].replace('%',''))
            volume = int(stock["volume"])

            if 1 <= price <= 50 and change >= 20 and volume >= 500000:
                results.append(stock)
        except:
            continue

    return results[:3]

def send_alert(stock):
    message = f"""
🚀 GAPPER ALERT

Ticker: {stock['symbol']}
Price: ${stock['price']}
Change: {stock['changesPercentage']}
Volume: {stock['volume']}

🔥 Entry: Break resistance
🛑 Stop: -5%
🎯 Target: +10–20%
"""
    requests.post(WEBHOOK_URL, json={"content": message})

def bot_loop():
    while True:
        now = datetime.now()

        if now.hour == 14 and now.minute == 20:
            gappers = get_gappers()
            for stock in gappers:
                send_alert(stock)
            time.sleep(60)

        time.sleep(10)

threading.Thread(target=bot_loop).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
