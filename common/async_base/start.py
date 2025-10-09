import asyncio
from asyncio import futures


async def fetch(n):
    await asyncio.sleep(n)
    return n


async def main():
    tasks = [
        asyncio.create_task(fetch(1)),
        asyncio.create_task(fetch(2)),
        asyncio.create_task(fetch(3)),
    ]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        if result:
            for task in tasks:
                if not task.done():
                    task.cancel()
        break

    result = await asyncio.gather(*tasks, return_exceptions=True)
    return result


result: list[futures.Future] = asyncio.run(main())

print(result)
