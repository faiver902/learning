import asyncio
import random

async def produce(queue, count_consumers):
    print('produce running')
    for i in range(10):
        value = random.random()
        print('produced', value)
        await queue.put(value)
    for i in range(count_consumers):
        await queue.put(None)

async def consume(queue):
    print('consume running')
    while True:
        await asyncio.sleep(3)
        value = await queue.get()
        if value is None:
            queue.task_done()
            break
        await asyncio.sleep(1)
        print('consumed', value)
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=3)
    consumers = [asyncio.create_task(consume(queue)) for _ in range(10)]
    cons_len = len(consumers)
    print('consumers', cons_len)
    producer = asyncio.create_task(produce(queue, cons_len))

    await asyncio.gather(producer, *consumers)

    await queue.join()

asyncio.run(main())