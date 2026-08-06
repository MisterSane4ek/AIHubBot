from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "📚 <b>Справка AIHubBot</b>\n\n"
        "Доступные команды:\n\n"
        "🏠 /start — Запустить бота\n"
        "👤 /profile — Просмотреть профиль\n"
        "💳 /payments — Раздел оплаты\n"
        "❓ /help — Показать эту справку\n\n"
        "💬 Просто отправьте сообщение, чтобы начать общение с AIHub.\n\n"
        "🚧 Бот находится в активной разработке. Новые возможности будут добавляться постепенно.",
        parse_mode="HTML"
    )