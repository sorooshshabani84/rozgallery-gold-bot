import os
import time
import schedule
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@rozgallerydaily"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHANNEL,
        "text": text
    })

def job():
    text = """📈 بازار طلا و ارز

🟡 طلای ۱۸ عیار: در حال دریافت...
💵 دلار: در حال دریافت...
🌍 اونس جهانی: در حال دریافت...

🪙 سکه امامی: در حال دریافت...
🪙 نیم سکه: در حال دریافت...
🪙 ربع سکه: در حال دریافت...

@rozgallerydaily
"""
    send_message(text)

# اجرای اولیه
job()

# هر 10 دقیقه
schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(30)
