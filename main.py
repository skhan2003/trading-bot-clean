import requests
from flask import Flask
import threading
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1487535942536396810/VQ-wp-Nr4kkUr8w6hShPBYAQp-3_2zrI6C6-yN6Oi-3DY3Vb6zcTRwxz_ooGdG64qmRc"
API_KEY = "wg6hAv7crwZdlFQcmoYwKdYqnK0cXaXD"

app = Flask(__name__)

@app.route("/")
def home():
    return "ADVANCED BOT RUNNING"

def get_stocks():
    url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={API_KEY}"
    data = requests.get(url).json()

    strong = []

    for stock in data:
        try:
            price = float(stock["price"])
            change = float(stock["changesPercentage"].replace('%',''))
            volume = int(stock["volume"])
            avg_volume = int(stock.get("avgVolume", volume))

            if avg_volume == 0:
                continue

            volume_ratio = volume / avg_volume

            if (
                1 <= price <= 50 and
                change >= 20 and
                volume >= 500000 and
                volume_ratio >= 2
            ):
                trade_type = "BREAKOUT 🚀" if change > 35 else "PULLBACK 🛡️"

                strong.append({
                    "symbol": stock["symbol"],
                    "price": price,
                    "change": change,
                    "volume": volume,
                    "ratio": round(volume_ratio, 2),
                    "type": trade_type
                })

        except:
            continue

    return strong[:5]

def send_alert(stock):
    entry = round(stock["price"] * 1.02, 2)
    stop = round(stock["price"] * 0.95, 2)
    target = round(stock["price"] * 1.18, 2)

    message = f"""
🚀 **ADVANCED SIGNAL**

Ticker: {stock['symbol']}
Type: {stock['type']}

Price: ${stock['price']}
Change: +{stock['change']}%
Volume: {stock['volume']} (x{stock['ratio']})

🎯 Entry: ${entry}
🛑 Stop: ${stop}
💰 Target: ${target}
"""

    requests.post(WEBHOOK_URL, json={"content": message})

def bot_loop():
    sent = set()

    while True:
        try:
            stocks = get_stocks()

            for stock in stocks:
                if stock["symbol"] not in sent:
                    send_alert(stock)
                    sent.add(stock["symbol"])

            time.sleep(120)  # every 2 minutes

        except Exception as e:
            print("Error:", e)
            time.sleep(60)

threading.Thread(target=bot_loop).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
