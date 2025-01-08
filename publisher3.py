import pika
connection_parameters=pika.ConnectionParameters(host='localhost')
connection=pika.BlockingConnection(connection_parameters)
channel=connection.channel()
channel.queue_declare('pa3')
message='hello im publisher 3'
channel.basic_publish(exchange='',routing_key='pa3',body=message)
print('message sends from publisher3')
connection.close()