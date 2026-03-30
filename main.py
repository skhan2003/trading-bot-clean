import requests
import time

TOKEN = "8522684488:AAGBLIhapSR42j6HAWAcNHl-ipqJN8eU828"
CHAT_ID = "7216850185"

# API (free market data)
API_URL = "https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=demo"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def scan_market():
    try:
        data = requests.get(API_URL).json()

        for stock in data[:10]:  # top 10 gainers
            price = stock.get("price", 0)
            change = stock.get("changesPercentage", "")

            # FILTERS (your strategy)
            if price < 5:
                message = f"""
🚀 PENNY STOCK ALERT

Ticker: {stock['symbol']}
Price: ${price}
Change: {change}
Volume: {stock.get('volume')}

🔥 Potential breakout!
"""
                send_message(message)

    except Exception as e:
        send_message(f"Error: {e}")

# RUN LOOP
while True:
    send_message("📡 Scanning market...")
    scan_market()
    time.sleep(300)  # every 5 minutes
