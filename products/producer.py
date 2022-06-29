# amqps://wjdihkuz:13LRz2uHVsbK80oPLnLmPfwwowPFbdBs@cougar.rmq.cloudamqp.com/wjdihkuz
import pika

params = pika.URLParameters('amqps://wjdihkuz:13LRz2uHVsbK80oPLnLmPfwwowPFbdBs@cougar.rmq.cloudamqp.com/wjdihkuz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')
