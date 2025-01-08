import pika
connection_parameters=pika.ConnectionParameters(host='localhost')
connection=pika.BlockingConnection(connection_parameters)
channel=connection.channel()
channel.queue_declare('pa2')
message='hello im publisher 2'
channel.basic_publish(exchange='',routing_key='pa2',body=message)
print('message  sends from publisher 2')
connection.close()