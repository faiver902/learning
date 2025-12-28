import aio_pika

from settings import get_settings


settings = get_settings()


async def async_conn(user_name, password, host, port):
    amqp_url = f"amqp://{user_name}:{password}@{host}:{port}/"

    connection = await aio_pika.connect_robust(amqp_url)

    return connection