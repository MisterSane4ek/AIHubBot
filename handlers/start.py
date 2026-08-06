from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database import add_user

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    # Регистрируем пользователя в базе данных
    await add_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Добро пожаловать в <b>AIHubBot</b>!\n\n"
        "🤖 Здесь ты сможешь общаться с искусственным интеллектом,\n"
        "использовать различные сервисы и получать помощь.\n\n"
        "📋 Основные команды:\n"
        "• /profile — профиль\n"
        "• /help — помощь\n\n"
        "Приятного использования!",
        parse_mode="HTML"
    )