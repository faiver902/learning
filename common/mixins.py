# import functools
# import logging
# import time
#
# logging.basicConfig(level=logging.INFO)
#
#
# class LoggingMixin:
#     """
#     Добавляет логирование каждого публичного метода.
#     Считать публичным всё, что не начинается с «_».
#     """
#
#     def __getattribute__(self, name):
#         attr = super().__getattribute__(name)
#         if callable(attr) and not name.startswith("_"):
#             @functools.wraps(attr)
#             def wrapper(*args, **kwargs):
#                 logging.info("%s.%s", self.__class__.__name__, name)
#                 return attr(*args, **kwargs)
#
#             return wrapper
#         return attr
#
#
# class UserService(LoggingMixin):
#     def create(self, name): ...
#
#     def delete(self, user_id): ...
#
#
# srv = UserService()
# srv.create("Ivan")  # INFO:root:UserService.create
# srv.delete(5)  # INFO:root:UserService.delete
#
# print('#########################')
#
# from datetime import datetime
#
#
# class TimestampMixin:
#     created_at: datetime
#     updated_at: datetime
#
#     def __init__(self, *args, **kwargs):
#         now = datetime.utcnow()
#         self.created_at = self.updated_at = now
#         super().__init__(*args, **kwargs)
#
#     def touch(self):
#         """Обновить updated_at на текущее время."""
#         self.updated_at = datetime.utcnow()
#
#
# class Post(TimestampMixin):
#     def __init__(self, title, text):
#         super().__init__()
#
#         self.title = title
#         self.text = text
#
#
# p = Post("Mixins", "— это удобно")
# print(p.created_at, p.updated_at)
# # time.sleep(5)
# p.touch()
#
# print(p.updated_at)
#
# print('#########################')
#
#
# class ValidateTitleMixin:
#     def __init__(self, *a, **kw):
#         super().__init__(*a, **kw)
#         if not self.title:
#             raise ValueError("title is required")
#
#
# class Article(ValidateTitleMixin, TimestampMixin):
#     def __init__(self, title, text):
#         self.title = title  # должен быть ПО-РАНЬШЕ super()
#         self.text = text
#
#         super().__init__()  # ValidateTitleMixin увидит title
#
#
# f = Article('Title', 'text')
# print(f.text, f.title)
#
# print('#########################')
#
# import json
# from typing import Any
#
#
# class JSONMixin:
#     def to_json(self, *, ensure_ascii: bool = False) -> str:
#         return json.dumps(self.__dict__, ensure_ascii=ensure_ascii, indent=4)
#
#     @classmethod
#     def from_json(cls, data: str) -> "JSONMixin":
#         return cls(**json.loads(data))
#
#
# class Config(JSONMixin):
#     def __init__(self, host: str, port: int):
#         self.host, self.port = host, port
#
#
# cfg = Config("localhost", 5432)
# raw = cfg.to_json()
# print(raw)
# same = Config.from_json(raw)
# print(vars(same))


# class EqualityMixin:
#     __eq_fields__: tuple[str, ...] = ()
#
#     def __eq__(self, other):
#         if other.__class__ is not self.__class__:
#             return NotImplemented
#         return all(
#             getattr(self, f) == getattr(other, f) for f in self.__eq_fields__)
#
#     def __hash__(self):
#         return hash(tuple(getattr(self, f) for f in self.__eq_fields__))
#
#
# class Point(EqualityMixin):
#     __eq_fields__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#
# print(Point(1, 2) == Point(1, 2))  # True
# print(Point(1, 9) in {Point(1, 2), Point(1, 2)})
#
#
# class CacheMixin:
#     _cache: dict[str, object] = {}
#
#     def cache(self, key: str, factory):
#         print(f"→ cache(): key = {key!r}")              # показываем ключ
#         if key not in self._cache:                      # сравнение строк!
#             print("  добавляем в кэш")
#             self._cache[key] = factory()
#         else:
#             print("  берём из кэша")
#         return self._cache[key]
#
#
# class Fibonacci(CacheMixin):
#     def fib(self, n: int) -> int:
#         if n < 2:
#             return n
#         return self.cache(f"fib{n}",
#                           lambda: self.fib(n - 1) + self.fib(n - 2))
#
#
# f = Fibonacci()
# print("Результат:", f.fib(10))
# print("\nСодержимое кэша:", f._cache.keys())
