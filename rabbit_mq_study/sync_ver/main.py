from settings import get_settings
from sync_ver.connections import connections

settings = get_settings()

def main():
    conn = connections(
        settings.rabbit.user_name,
        settings.rabbit.password,
        settings.rabbit.host,
        settings.rabbit.port)

    channel  = conn.channel()
    channel.exchange_declare(
        exchange="orders",
        exchange_type="topic",
        durable=True,
    )
    channel.queue_bind(exchange="orders",
                       queue="hello",
                       routing_key="hello")

    channel.queue_declare(queue="hello")
    channel.basic_publish(exchange='orders',
                          routing_key='hello',
                          body=b'Hello World!')

    print(" [x] Sent %r" % ("Hello World!"))

    channel.close()

if __name__ == '__main__':
    main()
