import os
import time
import requests
import schedule
from bs4 import BeautifulSoup

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@rozgallerydaily"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHANNEL,
        "text": text
    })


def get_price(url):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "lxml")
        price = soup.select_one(".value")
        return price.text.strip() if price else "نامشخص"
    except:
        return "نامشخص"


def get_data():
    dollar = get_price("https://www.tgju.org/profile/price_dollar_rl")
    gold18 = get_price("https://www.tgju.org/profile/geram18")
    ounce = get_price("https://www.tgju.org/profile/ons")

    emami = get_price("https://www.tgju.org/profile/sekee")
    nim = get_price("https://www.tgju.org/profile/nim")
    rob = get_price("https://www.tgju.org/profile/rob")

    return dollar, gold18, ounce, emami, nim, rob


def job():
    dollar, gold18, ounce, emami, nim, rob = get_data()

    text = f"""📈 بازار طلا و ارز (زنده)

🟡 طلای ۱۸ عیار: {gold18}
💵 دلار: {dollar}
🌍 اونس جهانی: {ounce}

🪙 سکه امامی: {emami}
🪙 نیم سکه: {nim}
🪙 ربع سکه: {rob}

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
