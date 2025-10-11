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
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = perf_counter()
        if inspect.iscoroutinefunction(func):
            await func(*args, **kwargs)
        else:
            print("run else")
            await asyncio.to_thread(func(*args, **kwargs))
        end = perf_counter()
        print(end - start)
        return end - start

    return wrapper


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
