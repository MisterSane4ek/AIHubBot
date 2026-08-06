from database import get_user


DEFAULT_CREDITS = 100


async def get_credits(user_id: int) -> int:
    """
    Возвращает количество кредитов пользователя.
    """

    user = await get_user(user_id)

    if user is None:
        return 0

    # Пока система кредитов не реализована.
    # Возвращаем стандартное значение.
    return DEFAULT_CREDITS


async def add_credits(user_id: int, amount: int) -> int:
    """
    Заглушка для начисления кредитов.
    """

    current = await get_credits(user_id)
    return current + amount


async def remove_credits(user_id: int, amount: int) -> int:
    """
    Заглушка для списания кредитов.
    """

    current = await get_credits(user_id)

    if current - amount < 0:
        return 0

    return current - amount