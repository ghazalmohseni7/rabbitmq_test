import pika



def on_message(channel,method,properties,body):
    print(f'message recieved : {body}')
def on_message2(channel,method,properties,body):
    print(f'message recieved from publisher 2 : {body}')
def on_message3(channel,method,properties,body):
    print(f'message recieved from publisher 3 : {body}')

# Replace <your_ip> with your system's IP address
rabbitmq_host = '192.168.10.77'
credentials = pika.PlainCredentials('admin', 'admin')

# Establish a connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq_host, credentials=credentials)
)

channel = connection.channel()


channel.queue_declare('face_queue')
channel.basic_consume(queue='face_queue',auto_ack=True,on_message_callback=on_message)

channel.queue_declare('pa2')
channel.basic_consume(queue='pa2',auto_ack=True,on_message_callback=on_message2)

channel.queue_declare('pa3')
channel.basic_consume(queue='pa3',auto_ack=True,on_message_callback=on_message3)
print("start consumingdddddddddddddddddddddddd")
channel.start_consuming()
# Send or receive messages
