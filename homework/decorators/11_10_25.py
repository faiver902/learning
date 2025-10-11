import inspect
from functools import wraps
from time import perf_counter

print("\n" + "#" * 80 + "\n")


def log_start_end(func):
    """
    --- Начало выполнения функции ---
    Привет!
    --- Конец выполнения функции ---
    """

    @wraps(func)
    def wrap(*args, **kwargs):
        print("--- Начало выполнения функции ---")
        result = func(*args, **kwargs)
        print("--- Конец выполнения функции ---")

        return result

    return wrap


@log_start_end
def hello():
    print("Привет!")


hello()

print("\n" + "#" * 80 + "\n")


def debug(func):
    """
    Вызов функции add с аргументами: (3, 5), {}
    Результат: 8
    """

    @wraps(func)
    def wrap(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args}, {kwargs}")
        res = func(*args, **kwargs)
        print(f"Результат {res}")
        return res

    return wrap


@debug
def add(a, b):
    return a + b


add(3, 5)

print("\n" + "#" * 80 + "\n")


def memoize(func):
    """
    Вычисляю 5^2 ...
    # второй раз без вывода, потому что результат взят из кэша
    """
    mem = None

    @wraps(func)
    def wrap(*args, **kwargs):
        nonlocal mem
        if mem is not None:
            return mem
        mem = func(*args, **kwargs)
        return mem

    return wrap


@memoize
def slow_square(n):
    print(f"Вычисляю {n}^2 ...")
    return n * n


slow_square(5)
slow_square(5)

print("\n" + "#" * 80 + "\n")


def repeat(times=2):
    """
    Привет, Владимир!
    Привет, Владимир!
    Привет, Владимир!
    """

    def decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrap

    return decorator


@repeat(times=3)
def greet(name):
    print(f"Привет, {name}!")


greet("Владимир")

print("\n" + "#" * 80 + "\n")

import asyncio


def measure_time(func):
    """
    Напиши универсальный декоратор measure_time, который:
        Поддерживает и синхронные, и асинхронные функции.
        Измеряет время выполнения и печатает его в секундах.
    Output:
        Функция async_task выполнена за 1.0012 сек.
        Функция sync_task выполнена за 0.0321 сек.


    Не понял, как сепарировать синхронную функцию. Ругается на нее.
    По итогу все таки спросил у ГПТ. Сам не дошел, что я возвращаю корутину из синк. функции.
    По итогу переделал на два врапера.
    """
    if inspect.iscoroutinefunction(func):

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            start = perf_counter()
            if inspect.iscoroutinefunction(func):
                await func(*args, **kwargs)
            else:
                func(*args, **kwargs)
            end = perf_counter()
            print(end - start)
            return end - start

        return async_wrapper
    else:

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            start = perf_counter()
            func(*args, **kwargs)
            end = perf_counter()
            print(end - start)
            return end - start

        return sync_wrapper


@measure_time
async def async_task():
    await asyncio.sleep(1)
    return "done"


@measure_time
def sync_task():
    for _ in range(1_000_000):
        pass


async def main():
    await async_task()
    sync_task()


asyncio.run(main())


print("\n" + "#" * 80 + "\n")


def trace(prefix: str = "", show_args: bool = False):
    """
    Требования:

    Декоратор trace должен уметь применяться без параметров (@trace) и с параметрами (@trace(prefix="API", show_args=True)).
    Поддержать синхронные функции, асинхронные функции и генераторы (в т.ч. async def-генераторы): логировать «start/stop» и, для генераторов, «yield n».
    Обязательно сохранять:
    __name__, __doc__, аннотации и оригинальную сигнатуру (проверьте inspect.signature).
    Опциональные параметры: prefix: str = "", show_args: bool = False.
    """

    def sync_decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrap

    async def async_decorator(func):
        @wraps(func)
        async def wrap(*args, **kwargs):
            print(prefix, show_args)
            result = await func(*args, **kwargs)
            return result

        return wrap

    if inspect.isfunction(prefix):
        print("sync")
        return sync_decorator(prefix)
    elif inspect.iscoroutinefunction(prefix):
        print("async")
        return async_decorator(prefix)
    return None


@trace
def add(a: int, b: int) -> int:
    return a + b


@trace
async def get_user(uid: int):
    print(f"get_user {uid} was work")


async def main_2():
    print(add(1, 2))
    await get_user(1)


asyncio.run(main_2())
