import threading


class ThreadSafeSingleton:
    _instance: "ThreadSafeSingleton | None" = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # быстрый путь без блокировки
            with cls._lock:  # «double-checked locking»
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value: str) -> None:
        if hasattr(self, "_initialized"):  # инициализируем ровно один раз
            return
        self.value = value
        self._initialized = True


s1 = ThreadSafeSingleton("первый вызов")
s2 = ThreadSafeSingleton("второй вызов")

print(s1 is s2)  # True — объекты идентичны
print(s1.value)  # первый вызов
print(s2.value)  # первый вызов — __init__ отработал лишь однажды


def singleton(cls):
    _cache = {}

    def wrapper(*a, **kw):
        if cls not in _cache:
            _cache[cls] = cls(*a, **kw)
        return _cache[cls]

    return wrapper


@singleton
class Logger:
    def __init__(self, name="app"):
        self._name = name

    def info(self, msg):
        print(f"[{self._name}] {msg}")


class SingletonBase:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


import threading


class SingletonMeta(type):
    _instances: dict[type, object] = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:  # быстрая ветка
            with cls._lock:
                if cls not in cls._instances:  # двойная проверка
                    inst = super().__call__(*args, **kwargs)
                    cls._instances[cls] = inst
        return cls._instances[cls]


class Settings(metaclass=SingletonMeta):
    def __init__(self, source="config.yaml"):
        self.source = source
