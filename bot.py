import asyncio
from aiogram import Dispatcher, Bot
from config import TOKEN
import logging
from handlers import start_handlers, profile_handlers
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(start_handlers.router, profile_handlers.router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())