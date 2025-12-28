import asyncio
import json

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

        exchange = await channel.declare_exchange(
            name="orders",
            type=aio_pika.ExchangeType.TOPIC,
            durable=True,
        )
        message = {"message": "Send notification error"}

        await exchange.publish(
            aio_pika.Message(
                body=json.dumps(message).encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,  # чтобы переживало рестарт (при durable queue)
            ),
            routing_key="notification.error",
        )

        print(" [x] Sent 'Send notification error!'")


if __name__ == "__main__":
    asyncio.run(main())
