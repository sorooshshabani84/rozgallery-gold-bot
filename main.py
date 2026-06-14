import os
import time
import requests
import schedule

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@rozgallerydaily"


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHANNEL,
        "text": text
    })


# 💵 دلار (API پایدار)
def get_dollar():
    try:
        r = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=IRR", timeout=10)
        data = r.json()
        return data["rates"]["IRR"]
    except:
        return "نامشخص"


# 🟡 طلا جهانی
def get_gold():
    try:
        r = requests.get("https://api.metals.live/v1/spot/gold", timeout=10)
        data = r.json()
        return data[0]["price"]
    except:
        return "نامشخص"


def job():
    dollar = get_dollar()
    gold = get_gold()

    text = f"""📈 بازار طلا و ارز

💵 دلار: {dollar} ریال
🟡 طلا جهانی: {gold} دلار

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
