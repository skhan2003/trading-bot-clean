import requests

TOKEN = "YOUR_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

send("🚀 BOT IS LIVE")
