import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@rozgallerydaily"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(
    url,
    json={
        "chat_id": CHANNEL,
        "text": "✅ تست ربات Railway"
    }
)

print(r.status_code)
print(r.text)
