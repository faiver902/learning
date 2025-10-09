import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t1 = time.perf_counter()
        elapsed = t1 - t0
        print(f"Function '{func.__name__}' executed in {elapsed:.4f} seconds.")
        return result

    return wrapper
