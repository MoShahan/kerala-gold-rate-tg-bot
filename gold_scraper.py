import requests
from bs4 import BeautifulSoup
import os

def send_telegram(message):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

def get_kerala_rate():
    try:
        url = "https://akgsma.com/"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        # Scrapes the 1 gram price for 22K gold
        rate = soup.find(string="22K916 (1gm)").find_next(string=lambda x: "₹" in x)
        return rate.strip()
    except Exception as e:
        return None

current_rate = get_kerala_rate()
if current_rate:
    msg = f"✨ *Kerala Gold Rate Today*\n\n💰 22K (1gm): *{current_rate}*\n📍 Source: AKGSMA"
    send_telegram(msg)
