import os
import sys

from sync_ver.connections import connections
from settings import get_settings


settings = get_settings()


def callback(channel, method, properties, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print(" [x] Received %r" % body)


def main():
    conn = connections(
        settings.rabbit.user_name,
        settings.rabbit.password,
        settings.rabbit.host,
        settings.rabbit.port)

    channel = conn.channel()

    channel.exchange_declare(
        exchange="orders",
        exchange_type="topic",
        durable=True,
    )
    channel.queue_bind(exchange="orders",
                       queue="hello",
                       routing_key="hello")
    channel.queue_declare(queue="hello")
    channel.basic_consume(queue="hello",
                            on_message_callback=callback,
                            auto_ack=False
                          )

    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)