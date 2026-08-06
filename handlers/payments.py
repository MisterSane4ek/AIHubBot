from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("payments"))
async def payments(message: Message):
    await message.answer(
        "💳 Раздел платежей находится в разработке.\n"
        "Скоро здесь появятся подписки и другие способы оплаты."
    )