from __future__ import annotations

from datetime import datetime
from typing import Any


class ResponseBuilder:
    """Интерфейс строителя."""

    def reset(self) -> None: ...

    def add_status(self, code: int, message: str) -> None: ...

    def add_payload(self, data: Any) -> None: ...

    def add_meta(self) -> None: ...

    def build(self) -> dict[str, Any]: ...


class JsonResponseBuilder(ResponseBuilder):
    def reset(self):
        self._result: dict[str, Any] = {}

    def __init__(self):
        self.reset()

    # шаги — каждый заполняет часть будущего словаря
    def add_status(self, code: int, message: str):
        self._result["status"] = {"code": code, "message": message}
        return self  # fluent-interface

    def add_payload(self, data: Any):
        self._result["data"] = data
        return self

    def add_meta(self):
        self._result["meta"] = {"ts": datetime.utcnow().isoformat()}
        return self

    # финальный продукт
    def build(self) -> dict[str, Any]:
        product = self._result
        self.reset()  # «один объект – один ответ»
        return product


# Клиентский код
builder = JsonResponseBuilder()

response_ok = (
    builder.add_status(200, "OK")
    .add_payload({"id": 42, "name": "Alice"})
    .add_meta()
    .build()
)
print(response_ok)

response_error = (
    builder.add_status(400, "Bad request").add_payload(None).add_meta().build()
)
print(response_error)
