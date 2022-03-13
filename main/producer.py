import pika
import json


params = pika.URLParameters('Your AMQP URL')
# you can signup from here https://customer.cloudamqp.com/signup


connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin',
                          body=json.dumps(body), properties=properties)
