#!/usr/bin/python3

import pika
import mysql.connector

# Set RabbitMQ credentials for login
credentials = pika.PlainCredentials('mkelly', 'mkelly')

# Establish MySQL connection
connection = pika.BlockingConnection(pika.ConnectionParameters('172.25.0.200',
                                                               5672,
                                                               '/',
                                                               credentials))
channel = connection.channel()

# Create the RabbitMQ queue named 'hello' if it doesn't exist
channel.queue_declare(queue='hello')

# Create MySQL Connector Object
mydb = mysql.connector.connect(
  host="172.25.0.201",
  user="rabbitmq",
  passwd="S3cur3",
  database="rabbitmq"
)

# Create MySQL cursor
mycursor = mydb.cursor()

# Create the function to print the contents of the message on the screen
def callback(ch, method, properties, body):
        # Decode the utf formatted incoming message
        val = (body.decode("utf-8"))
        print(" [x] Received %r" % val)
        print("inserting",val,"into MySQL Table")
        # Insert Message (aka val) into the MySQL table
        mycursor.execute(
           """INSERT INTO messages (message) VALUES ('%s')"""
           %(val))
        mydb.commit()

# State the the callback function will receive messages from the 'hello' queue
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

# Go into a never ending loop to wait for data and run the callback function
# whenever necessary
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()