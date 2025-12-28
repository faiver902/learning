import asyncio
from multiprocessing.pool import worker

import aio_pika

from async_ver.conn import async_conn
from settings import get_settings

settings = get_settings()


async def on_message(message: aio_pika.IncomingMessage) -> None:
    # manual ack через контекст-менеджер
    async with message.process(requeue=True):
        print(" [x] Received %r" % message.body)
        # если тут будет исключение — сообщение будет requeue (из-за requeue=True)


async def main() -> None:
    connection = await async_conn(settings.rabbit.user_name,
                                  settings.rabbit.password,
                                  settings.rabbit.host,
                                  settings.rabbit.port)

    channel = await connection.channel()

    # ограничиваем сколько сообщений одновременно "в полёте" у этого consumer
    await channel.set_qos(prefetch_count=10)

    exchange = await channel.declare_exchange(
        name="orders",
        type=aio_pika.ExchangeType.TOPIC,
        durable=True,
    )

    queue = await channel.declare_queue(
        name="notification_analytics",
        durable=True,
    )

    await queue.bind(exchange, routing_key="notification.#")

    for i in  range(5):
        await queue.consume(on_message)

    print("Waiting for messages. Press CTRL+C to exit.")
    try:
        await asyncio.Future()  # жить вечно
    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
