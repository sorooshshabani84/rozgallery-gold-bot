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
        soup = BeautifulSoup(r.text, "html.parser")

        # فقط همه عددهای داخل صفحه رو می‌گیریم
        text = soup.get_text()

        # پیدا کردن اولین عدد بزرگ (قیمت‌ها معمولاً این شکلی‌اند)
        import re
        numbers = re.findall(r'[\d,]{4,}', text)

        if numbers:
            return numbers[0]

        return "نامشخص"

    except Exception as e:
        print("ERROR:", e)
        return "نامشخص"

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
