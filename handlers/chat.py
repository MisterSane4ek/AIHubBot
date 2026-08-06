from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def chat_handler(message: Message):
    # Игнорируем сообщения без текста
    if not message.text:
        await message.answer(
            "❌ Пока я умею работать только с текстовыми сообщениями."
        )
        return

    # Заглушка до подключения ИИ
    await message.answer(
        "🤖 AIHub\n\n"
        f"Вы написали:\n{message.text}\n\n"
        "⚙️ Искусственный интеллект пока не подключён.\n"
        "Скоро здесь будут ответы от AI."
    )