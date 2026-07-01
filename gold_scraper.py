import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

def send_telegram(message):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

def clean_price(text):
    # Extracts only the digits from a string like "₹ 14460"
    return int(''.join(filter(str.isdigit, text)))

def get_rates():
    try:
        url = "https://akgsma.com/"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Finding the rates based on the website structure
        rate_22k_text = soup.find(string=lambda x: x and "22K916" in x).split('-')[1].strip()
        
        # Clean and calculate
        price_22k_1g = clean_price(rate_22k_text)
        
        return {
            "22k_1g": price_22k_1g,
            "22k_8g": price_22k_1g * 8,
        }
    except Exception as e:
        print(f"Error: {e}")
        return None

data = get_rates()

if data:
    today_date = datetime.now().strftime("%d/%m/%Y")
    
    msg = (
        f"✨ *Kerala Gold Rate - {today_date}*\n\n"
        f"🟡 *22K Gold (916)*\n"
        f"• 1 gram: ₹{data['22k_1g']:,}\n"
        f"• 8 gram: ₹{data['22k_8g']:,}"
    )
    send_telegram(msg)
else:
    send_telegram("❌ Failed to fetch gold rates. Check the AKGSMA website.")
