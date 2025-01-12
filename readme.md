# How to install rabbitmq with docker

# latest RabbitMQ 4.0.x
<pre>
docker run -d --name rabbitmq \
  -p 5672:5672 -p 15672:15672 \
  -v rabbitmq_data:/var/lib/rabbitmq \
  rabbitmq:4.0-management

</pre>


- when the container is running , open a tab on browser go this address : localhost:15672
- login with username:guest , password : guest
- go to Admin tab create a new user with username:admin passwrod :admin
- then click on admin(in the table in the Admin tab) go to set permission 
- Virtual Host : /
- Configure regexp: *
- Write regexp: *
- Read regexp: *
- then click on set permission

# How to run the python project
1. first create a virtual environment and activate it
    - virtualenv venv
    - source venv/bin/activate
2. install pika 
    - pip install pika
3. run the consumer.py 
    - python comsumer.py
    <br>
    or
    <br>
    - python3 consumer.py
4. now you can run each of the publishers 
    - python publisher.py



