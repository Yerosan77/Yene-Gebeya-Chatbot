
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
import asyncio

BOT_TOKEN = "your-bot-token"

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Add your handlers here

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
