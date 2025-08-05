
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
import asyncio

BOT_TOKEN = "7653628673:AAHm2SsOwnPWeDMc1XoT4BHNOqi2IMWFyuE"

bot = Bot(token=7653628673:AAHm2SsOwnPWeDMc1XoT4BHNOqi2IMWFyuE, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Add your handlers here

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
