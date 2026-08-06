import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database import init_db

from handlers import (
    start_router,
    help_router,
    profile_router,
    chat_router,
    payments_router,
    admin_router,
)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Подключаем обработчики
dp.include_router(start_router)
dp.include_router(help_router)
dp.include_router(profile_router)
dp.include_router(payments_router)
dp.include_router(admin_router)
dp.include_router(chat_router)


async def main():
    # Создаем базу данных и таблицы
    await init_db()

    # Запускаем бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())