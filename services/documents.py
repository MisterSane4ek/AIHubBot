import os


ALLOWED_EXTENSIONS = {
    ".txt",
    ".pdf",
    ".docx",
    ".md"
}


def is_allowed(filename: str) -> bool:
    """
    Проверяет, поддерживается ли формат файла.
    """
    _, extension = os.path.splitext(filename)
    return extension.lower() in ALLOWED_EXTENSIONS


async def get_file_info(file_name: str) -> dict:
    """
    Возвращает информацию о документе.
    """
    return {
        "name": file_name,
        "extension": os.path.splitext(file_name)[1].lower(),
        "supported": is_allowed(file_name)
    }


async def process_document(file_name: str) -> str:
    """
    Заглушка обработки документа.
    """

    if not is_allowed(file_name):
        return "❌ Этот формат файла пока не поддерживается."

    return (
        f"📄 Документ: {file_name}\n\n"
        "⚙️ Обработка документов пока находится в разработке."
    )