from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

# Токен Telegram-бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ID владельца
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Проверка, что токен найден
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден! Проверьте файл .env")