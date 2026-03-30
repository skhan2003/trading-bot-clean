import requests

TOKEN = "8522684488:AAGBLIhapSR42j6HAWAcNHl-ipqJN8eU828"
CHAT_ID = "7216850185"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": "🚀 WORKING NOW"}
)
