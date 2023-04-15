from kafka import *
from kafka.admin import *

# here we create a topic
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id='test'
)

topic_list = [NewTopic(name="loay_12", num_partitions=1, replication_factor=1)]

admin_client.create_topics(new_topics=topic_list, validate_only=False)

_input = input('press enter to send message')
# Create a producer. broker is running on
producer = KafkaProducer(retries=5, bootstrap_servers=['localhost:9092'])

# To produce to Loay-topic
#
producer.send('loay_12', key='loay-key'.encode('utf-8'), value=_input.encode('utf-8'))

producer.flush()

# To consume from Loay-topic

consumer = KafkaConsumer('loay_12', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest',
                         enable_auto_commit=True)

# To consume latest messages and auto-commit offsets
for message in consumer:
    # print('the key =' + str(message.key))
    print(message.value.decode('utf-8'))
