# amqps://wjdihkuz:13LRz2uHVsbK80oPLnLmPfwwowPFbdBs@cougar.rmq.cloudamqp.com/wjdihkuz
import json

import pika

params = pika.URLParameters('amqps://wjdihkuz:13LRz2uHVsbK80oPLnLmPfwwowPFbdBs@cougar.rmq.cloudamqp.com/wjdihkuz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
