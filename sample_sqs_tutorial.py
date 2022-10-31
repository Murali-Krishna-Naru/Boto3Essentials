import boto3

sqs_resource = boto3.resource(service_name="sqs", region_name="us-east-1")
created_queue = sqs_resource.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# Get the queue. This returns an SQS.Queue instance
queried_queue = sqs_resource.get_queue_by_name(QueueName='test')

print(queried_queue.url)
print(queried_queue.attributes.get('DelaySeconds'))

for queue in sqs_resource.queues.all():
    print(queue.url)

# Create a new message
response = created_queue.send_message(MessageBody='world')

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))