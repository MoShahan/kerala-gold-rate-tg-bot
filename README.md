# 🪙 Kerala Daily Gold Rate Bot

An automated Python scraper that fetches daily gold rates (22K and 18K) from the **All Kerala Gold & Silver Merchants Association (AKGSMA)** and sends them directly to a Telegram chat.

## 🚀 Features
* **Live Scraping:** Fetches the latest rates directly from [AKGSMA](https://akgsma.com/).
* **Multiple Categories:** Tracks 1 gram and 8 gram (1 Pavan) prices for both **22K** and **18K** gold.
* **Fully Automated:** Runs every morning at 9:00 AM IST using GitHub Actions (Cloud-based).
* **Zero Cost:** Uses free-tier GitHub Actions and Telegram Bot API.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Libraries:** `BeautifulSoup4` (Scraping), `Requests` (API & Web)
* **Automation:** GitHub Actions (YAML)
* **Notifier:** Telegram Bot API

## 📋 Setup & Installation

### 1. Telegram Setup
1. Create a bot via [@BotFather](https://t.me/botfather) and save the **API Token**.
2. Get your Chat ID via [@userinfobot](https://t.me/userinfobot).

### 2. GitHub Secrets
To protect your tokens, add the following to **Settings > Secrets and variables > Actions**:
* `TELEGRAM_TOKEN`: Your bot's API token.
* `TELEGRAM_CHAT_ID`: Your personal Telegram ID.

### 3. File Structure
* `gold_scraper.py`: The Python logic for scraping and sending messages.
* `requirements.txt`: Lists the Python dependencies.
* `.github/workflows/daily_run.yml`: The automation schedule.

## 🤖 How It Works
The bot uses `BeautifulSoup` to parse the HTML table on the AKGSMA website. It specifically targets:
* **22K916 (1gm)** - Used for calculating the 1g and 8g standard rates.
* **18K750 (1gm)** - Used for calculating the 1g and 8g low-karat rates.

The script then formats the numbers with Indian currency separators and pushes a notification via the Telegram Bot API.

## 📈 Example Message
> ✨ **Kerala Gold Rate Today**
> 
> 🟡 **22K Gold (916)**
> • 1 gram: ₹14,460
> • 8 gram: ₹115,680
> 
> 🟠 **18K Gold (750)**
> • 1 gram: ₹11,950
> • 8 gram: ₹95,600
> 
> 📍 Source: AKGSMA

---
*Created with ❤️ for personal use in Kerala.*
