import requests
from flask import Flask
import threading
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1487535942536396810/VQ-wp-Nr4kkUr8w6hShPBYAQp-3_2zrI6C6-yN6Oi-3DY3Vb6zcTRwxz_ooGdG64qmRc"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def send_test():
    while True:
        requests.post(WEBHOOK_URL, json={"content": "🚀 BOT IS WORKING"})
        time.sleep(30)

threading.Thread(target=send_test).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
