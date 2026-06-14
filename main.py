import requests

TOKEN = "8682876117:AAHcJxShwgr0UufSW5QntUWaSWwea1PQGjY"
CHANNEL = "@rozgallerydaily"

text = "✅ ربات Rozgallery با موفقیت راه‌اندازی شد."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, json={
    "chat_id": CHANNEL,
    "text": text
})

print("Message sent")
