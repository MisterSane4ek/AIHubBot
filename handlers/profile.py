from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database import get_user

router = Router()


@router.message(Command("profile"))
async def profile_command(message: Message):
    user = await get_user(message.from_user.id)

    if user is None:
        await message.answer(
            "❌ Профиль не найден.\n"
            "Сначала используйте команду /start."
        )
        return

    telegram_id = user[1]
    username = user[2] or "Не указан"
    first_name = user[3] or "Не указано"
    last_name = user[4] or "Не указана"
    is_admin = "Да" if user[5] else "Нет"

    await message.answer(
        f"👤 <b>Ваш профиль</b>\n\n"
        f"🆔 ID: <code>{telegram_id}</code>\n"
        f"👤 Username: @{username}\n"
        f"📛 Имя: {first_name}\n"
        f"📝 Фамилия: {last_name}\n"
        f"⭐ Администратор: {is_admin}",
        parse_mode="HTML"
    )