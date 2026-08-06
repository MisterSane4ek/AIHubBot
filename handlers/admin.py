from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import OWNER_ID
from database import get_users_count

router = Router()


@router.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id != OWNER_ID:
        await message.answer("❌ У вас нет доступа к этой команде.")
        return

    users_count = await get_users_count()

    await message.answer(
        "🛠 <b>Панель администратора</b>\n\n"
        f"👥 Пользователей: <b>{users_count}</b>\n\n"
        "Доступные возможности:\n"
        "• Статистика\n"
        "• Рассылка\n"
        "• Управление пользователями\n"
        "• Управление ботом\n\n"
        "⚙️ Новые функции будут добавляться постепенно.",
        parse_mode="HTML"
    )