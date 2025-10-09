from contextlib import contextmanager


@contextmanager
def hello_context_manager():
    print("Entering the context...")
    try:
        yield "Hello, World!"  # код в блоке `with` будет выполнен здесь
    except Exception as e:
        print(f"Caught exception inside context manager: {type(e).__name__} — {e}")
        # Можете проглотить или пробросить дальше:
        # raise  # если хотите пробросить
    finally:
        print("Leaving the context...")


# Пример использования:
with hello_context_manager() as hello:
    print(hello)
    raise ValueError("Something went wrong!")

print("Continue normally.")


class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        if isinstance(exc_value, IndexError):
            # Handle IndexError here...
            print(f"An exception occurred in your with block: {exc_type}")
            print(f"Exception message: {exc_value}")
            return True


with HelloContextManager() as hello:
    print(hello)
    hello[100]

print("Continue normally from here...")


class Indenter:
    def __init__(self):
        self.lvl = -1

    def __enter__(self):
        self.lvl += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.lvl -= 1

    def print(self, text) -> str:
        print(" " * 4 * self.lvl + text)


with Indenter() as indent:
    indent.print("hi!")
    with indent:
        indent.print("hello")
        with indent:
            indent.print("bonjour")
    indent.print("hey")
