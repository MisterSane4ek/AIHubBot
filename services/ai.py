class AIService:
    """
    Сервис для работы с искусственным интеллектом.
    """

    def __init__(self):
        self.model = "AIHub"

    async def generate_response(self, user_id: int, prompt: str) -> str:
        """
        Генерация ответа ИИ.
        Пока используется заглушка.
        """

        return (
            "🤖 AIHub\n\n"
            "Искусственный интеллект пока не подключён.\n\n"
            f"Ваш запрос:\n{prompt}"
        )

    async def change_model(self, model_name: str):
        """
        Смена модели ИИ.
        """

        self.model = model_name

    async def get_model(self) -> str:
        """
        Возвращает текущую модель.
        """

        return self.model


ai_service = AIService()