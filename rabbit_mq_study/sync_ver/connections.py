import pika

from settings import get_settings

settings = get_settings()


def connections(user_name, password, host, port, **kwargs):
    credentials = pika.PlainCredentials(user_name,
                                        password)
    connection = pika.BlockingConnection(
                                pika.ConnectionParameters(host,
                                port=port,
                                credentials=credentials,
                                **kwargs))

    return connection