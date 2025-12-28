import asyncio
import aio_pika

from async_ver.conn import async_conn
from settings import get_settings

settings = get_settings()


async def main() -> None:
    connection = await async_conn(settings.rabbit.user_name,
                                  settings.rabbit.password,
                                  settings.rabbit.host,
                                  settings.rabbit.port)

    async with connection:
        channel = await connection.channel()

        # 1) exchange
        exchange = await channel.declare_exchange(
            name="orders",
            type=aio_pika.ExchangeType.TOPIC,
            durable=True,
        )

        # 2) queue
        queue = await channel.declare_queue(
            name="hello",
            durable=True,
        )

        # 3) bind queue -> exchange
        await queue.bind(exchange, routing_key="hello")

        # 4) publish
        await exchange.publish(
            aio_pika.Message(
                body=b"Hello World!",
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,  # чтобы переживало рестарт (при durable queue)
            ),
            routing_key="hello.send_hello",
        )

        print(" [x] Sent 'Hello World!'")


if __name__ == "__main__":
    asyncio.run(main())
