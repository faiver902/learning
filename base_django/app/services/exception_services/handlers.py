from django.core.exceptions import ObjectDoesNotExist
from pydantic import ValidationError

# Любые кастомные или системные исключения:
EXCEPTION_HANDLERS = {
    ObjectDoesNotExist: {"status": 404, "message": "Объект не найден"},
    ValidationError: {"status": 422, "message": "Ошибка валидации"},
    ValueError: {"status": 400, "message": "Некорректное значение"},
    PermissionError: {"status": 403, "message": "Доступ запрещён"},
    KeyError: {"status": 400, "message": "Отсутствует необходимый ключ"},
    Exception: {"status": 500, "message": "Внутренняя ошибка сервера"},
}
