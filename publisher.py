import pika
connection_parameters=pika.ConnectionParameters(host='localhost')
connection=pika.BlockingConnection(connection_parameters)
channel=connection.channel()
channel.queue_declare('face_queue')
message='hello from publisher face'
channel.basic_publish(exchange='',routing_key='face_queue',body=message)
print('message sends from publisher')
connection.close()