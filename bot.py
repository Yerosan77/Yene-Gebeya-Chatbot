import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message

# Set up logging (optional but recommended)
logging.basicConfig(level=logging.INFO)

# Get the bot token from environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables!")

# Create Bot with new aiogram v3+ syntax
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

# Create Dispatcher
dp = Dispatcher()

# Example handler (you can add more handlers below)
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello! I'm alive and running on Render!")

# Main entrypoint
async def main():
    # Start polling updates from Telegram
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
