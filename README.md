# tg_alert_system
tg_alert_system is a lightweight Telegram bot for real-time logging and alerting. It allows you to send error logs or important notifications from your projects directly to Telegram users.

# Features

Users can subscribe to receive alerts by sending /start to the bot.

Send error logs or notifications in real-time using a simple alert(project, error_log) function.

Supports multiple users simultaneously.

Easy setup with environment variables.

# Installation

Clone the repository:

git clone <repo_url>
cd tg_alert_system


Install dependencies:

pip install -r requirements.txt


# Create a token.env file in the project root:

BOT_TOKEN=your_telegram_bot_token

Usage

Run the bot:

<code>python main.py</code>


Users send /start to the bot to subscribe for alerts.

From your project, call:

from tg_alert_system import alert

await alert("MyProject", "An error occurred: ...")


All subscribed users will receive the message in Telegram.

# Dependencies

Python 3.10+

aiogram

python-dotenv

# License

MIT License
