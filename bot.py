import os
from aiogram import Bot
from aiogram.enums import ParseMode

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables!")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

# ...rest of your code...
