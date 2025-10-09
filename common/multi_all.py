import asyncio
import math
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from contextlib import contextmanager
from datetime import datetime

import aiohttp
import requests


@contextmanager
def time_block(name):
    start = datetime.now()
    yield
    duration = datetime.now() - start
    print(f"[{name}] Execution time: {duration}")


urls = ["https://example.com", "https://python.org", "https://httpbin.org/get"]


def download(url):
    response = requests.get(url)
    print(f"Downloaded {url}: {len(response.text)} bytes")


if __name__ == "__main__":
    with time_block("ThreadPoolExecutor"):
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(download, urls)
    print("All downloads completed.1")

numbers = [50000, 60000, 70000]


def compute_factorial(n):
    print(f"Computing factorial for {n}")
    math.factorial(n)
    print(f"Finished {n}")


if __name__ == "__main__":
    with time_block("ProcessPoolExecutor"):
        with ProcessPoolExecutor(max_workers=3) as executor:
            executor.map(compute_factorial, numbers)
    print("All computations done.2")

urls = ["https://example.com", "https://python.org", "https://httpbin.org/get"]
semaphore = asyncio.Semaphore(2)  # Ограничиваем параллелизм


async def download(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.text()
                print(f"Downloaded {url}: {len(data)} bytes")


if __name__ == "__main__":

    async def main():
        with time_block("Asyncio"):
            tasks = [download(url) for url in urls]
            await asyncio.gather(*tasks)

    asyncio.run(main())
    print("All computations done.3")
