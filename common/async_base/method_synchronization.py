import asyncio

# lock = asyncio.Lock()
#
# shared_counter = 0
#
#
# async def worker(name):
#     global shared_counter
#     print(f"{name} ждёт блокировку...")
#     async with lock:
#         print(f"{name} получил доступ.")
#         current = shared_counter
#         await asyncio.sleep(1)
#         shared_counter = current + 1
#         print(f"{name} обновил счётчик: {shared_counter}")
#
#
# async def main():
#     await asyncio.gather(*(worker(f"Задача-{i}") for i in range(3)))
#
#
# asyncio.run(main())
#
#
# cache = dict()
# sem = asyncio.Semaphore(5)
#
#
# async def request_remote():
#     print("Will request the website to get status.")
#     async with aiohttp.ClientSession() as session:
#         response = await session.get("https://www.example.com")
#         return response.status
#
#
# async def get_value(key: str):
#     async with sem:
#         async with lock:
#             if key not in cache:
#                 print(f"The value of key {key} is not in cache.")
#                 value = await request_remote()
#                 cache[key] = value
#             else:
#                 print(f"The value of key {key} is already in cache.")
#                 value = cache[key]
#             print(f"The value of {key} is {value}")
#             return value
#
#
# async def main():
#     tasks = [asyncio.create_task(get_value("status")) for _ in range(1000)]
#     return await asyncio.gather(*tasks)
#
#
# if __name__ == "__main__":
#     start = datetime.datetime.now()
#     asyncio.run(main())
#     print(datetime.datetime.now() - start)


async def task_1(event):
    await event.wait()
    print("Anything task")


async def main():
    event = asyncio.Event()
    tasks = [asyncio.create_task(task_1(event)) for _ in range(5)]
    await asyncio.sleep(2)
    event.set()
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
