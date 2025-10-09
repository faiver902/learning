from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ErrDTO:
    exc_type: type[Exception]
    message: str
    code: int = 500  # необязательно, но часто нужен

    def __repr__(self) -> str:  # компактный вывод
        return f"{self.exc_type.__name__} -> {self.message}"


class ErrFactory:
    _registry: dict[type[Exception], ErrDTO] = {}

    # ─────────── регистрация ────────────
    @classmethod
    def register(cls, *items: ErrDTO) -> None:
        for item in items:
            if item.exc_type in cls._registry:
                raise RuntimeError(f"{item.exc_type.__name__} already registered")
            cls._registry[item.exc_type] = item

    # ─────────── получение DTO ───────────
    @classmethod
    def get(cls, exc: Exception) -> ErrDTO:
        """Гарантированно возвращает ErrDTO; для неизвестных типов — дефолт."""
        return cls._registry.get(type(exc), ErrDTO(type(exc), str(exc)))

    # ─────────── «заморозка» реестра ─────
    @classmethod
    def view(cls) -> Mapping[type[Exception], ErrDTO]:
        """Только чтение — для дебага или метрик."""
        return cls._registry.copy()  # или types.MappingProxyType(...)


# ─────────────────────────────────────────
# Регистрация
ErrFactory.register(
    ErrDTO(ValueError, "Некорректное значение", 400),
    ErrDTO(ZeroDivisionError, "Деление на ноль", 400),
    ErrDTO(AttributeError, "Нет такого атрибута", 400),
)

# Использование
try:
    6 / 0
except Exception as e:
    dto = ErrFactory.get(e)
    print(dto.code, dto.message)
