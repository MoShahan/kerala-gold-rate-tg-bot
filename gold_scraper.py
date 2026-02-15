import requests
from bs4 import BeautifulSoup
import os

def send_telegram(message):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    r = requests.post(url, data=payload)
    print(f"Telegram Response: {r.text}") # This shows in GitHub logs

def get_kerala_rate():
    try:
        # Source 1: AKGSMA
        url = "https://akgsma.com/"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for any text that looks like a price near "22K"
        # We search for the text and then find the next element containing the ₹ symbol
        target = soup.find(string=lambda x: x and "22K" in x and "1gm" in x)
        if target:
            rate = target.find_next(string=lambda x: "₹" in x or (x and x.strip().isdigit()))
            return rate.strip()
        return None
    except Exception as e:
        print(f"Scraping error: {e}")
        return None

current_rate = get_kerala_rate()

if current_rate:
    # Calculation for 1 Pavan (8 grams)
    # Remove ₹ and commas to do math
    clean_rate = ''.join(filter(str.isdigit, current_rate))
    pavan_rate = int(clean_rate) * 8
    
    msg = (f"✨ *Kerala Gold Rate Today*\n\n"
           f"💰 *22K (1gm):* {current_rate}\n"
           f"🪙 *22K (8gm/Pavan):* ₹{pavan_rate:,}\n\n"
           f"📍 Source: AKGSMA")
    send_telegram(msg)
else:
    # If it fails, send an error to your Telegram so you know!
    send_telegram("❌ Gold scraper failed to find the price today. Please check the website layout.")
