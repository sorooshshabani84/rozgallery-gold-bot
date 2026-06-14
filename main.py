import os
import time
import schedule
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@rozgallerydaily"

def send_message(text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        r = requests.post(
            url,
            json={
                "chat_id": CHANNEL,
                "text": text
            }
        )

        print("STATUS:", r.status_code)
        print("RESPONSE:", r.text)

    except Exception as e:
        print("ERROR:", e)

def job():
    print("JOB RUNNING...")

    send_message("""
📈 بازار طلا و ارز

🟡 طلای ۱۸ عیار: در حال دریافت...
💵 دلار: در حال دریافت...
🌍 اونس جهانی: در حال دریافت...

🪙 سکه امامی: در حال دریافت...
🪙 نیم سکه: در حال دریافت...
🪙 ربع سکه: در حال دریافت...

@rozgallerydaily
""")

job()

schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(30)
