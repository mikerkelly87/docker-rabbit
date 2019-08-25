#!/usr/bin/python3
  
import pika

# just a blank line to make things look cleaner
print()

# ask the user to put in the IP address with CIDR
print("Type the message you want to send and press Enter :")

# Take the user's input
message = input()


# Set RabbitMQ credentials for login
credentials = pika.PlainCredentials('mkelly', 'mkelly')

# Establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters('172.25.0.200',
                                                               5672,
                                                               '/',
                                                               credentials))
channel = connection.channel()

# Create the queue named 'hello' if it doesn't exist
channel.queue_declare(queue='hello')

# Send the message 'Message02' to the 'hello' queue we created
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent ",message)

# Close the connection
connection.close()