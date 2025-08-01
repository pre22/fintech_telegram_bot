# Walletx


A simple simulated wallet management Telegram bot using `python-telegram-bot`, Docker, and Python 3.

## Features
- Check balance `/balance`
- Fund wallet `/fund <amount>`
- Withdraw funds `/withdraw <amount>`
- View last 5 transactions `/transactions`

## Getting Started

### Prerequisites
- Docker + Docker Compose installed
- Telegram Bot Token from @BotFather

### Setup

1. Clone this repo:
```bash
git clone https://github.com/pre22/fintech_telegram_bot.git
cd fintech_telegram_bot
```

2. Add your bot token in `bot/main.py` using this key in your .env file:
```python
BOT_TOKEN = "BOT_TOKEN"
```

3. Run the app using Docker Compose:

```bash
docker compose up --build
```

## Bot Commands

| Command        | Description |
|----------------|-------------|
| `/start`       | Welcome message |
| `/balance`     | Show current balance |
| `/fund 50`     | Fund your wallet with $50 |
| `/withdraw 20` | Withdraw $20 from wallet |
| `/transactions`| View last 5 transactions |

