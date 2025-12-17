import asyncio
import inspect
from functools import wraps
from typing import Callable, Hashable


def trace(_func=None, *, prefix=None, show_args=True):
    def collect_args(args, kwargs):
        if not show_args:
            return ""
        arg = [i for i in args]
        for k, v in kwargs.items():
            arg.append(f"{k}={v}")
        return arg

    def decorator(func):
        if inspect.iscoroutinefunction(func):

            @wraps(func)
            async def async_wrap(*args, **kwargs):
                try:
                    return await func(*args, **kwargs)
                finally:
                    print(
                        "args", collect_args(args, kwargs), prefix if prefix else None
                    )
                    print("sign", inspect.signature(func))

            return async_wrap

        elif inspect.isfunction(func):

            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                finally:
                    print(
                        "args", collect_args(args, kwargs), prefix if prefix else None
                    )
                    print("sign", inspect.signature(func))

            return wrapper

    if _func is None:
        return decorator
    return decorator(_func)


@trace(prefix="API", show_args=True)
def add(a: int, b: int) -> int:
    return a + b


@trace(show_args=False)
async def get_user(uid: int): ...


async def main():
    print("async_func", await get_user(1))
    print("add", add(a=2, b=1))


asyncio.run(main())

print("\n" + "#" * 80 + "\n")

def rate_limit(calls: int, per: float, key: Callable[..., Hashable] | None = None, *args, **kwargs) -> None:
    calls_acc = 0
    def decorator(func):
        # if inspect.iscoroutinefunction(func):
        #     @wraps(func)
        #     async def async_wrap(*args, **kwargs):
        #         try:
        #             return await func(*args, **kwargs)
        #         finally:
        #             print("sign", inspect.signature(func))
        #
        #     return async_wrap

        if inspect.isfunction(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                nonlocal calls_acc
                for i in range(calls):
                    try:
                        return func(*args, **kwargs)
                    except Exception:
                        calls_acc += 1
                        if calls_acc < calls:
                            return func(*args, **kwargs)
                    finally:
                        print("sign", inspect.signature(func))

            return wrapper


# @rate_limit(calls=5, per=1.0, key=lambda _, user_id: user_id)
# def send_sms(payload, user_id: int): ...
#
# # @rate_limit(calls=10, per=2.0, key=lambda *a, **kw: kw["token"],)
# # async def fetch_data(token: str): ...
#
# async def main():
#      send_sms({'token_sync': 'token_0987654321'}, 2)
#      # await fetch_data('12345678901')
#
# asyncio.run(main())
la = lambda _, user_id: user_id
print(la('_', 4))