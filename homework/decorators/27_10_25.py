import asyncio
import inspect
from functools import wraps


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
                    print("args", collect_args(args, kwargs), prefix)
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
