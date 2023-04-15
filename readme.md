# README.md

## Kafka Producer and Consumer in Python

This Python script demonstrates how to create a Kafka topic, produce messages to it, and consume messages from it using the `kafka-python` library.

### Prerequisites

- Python 3.6 or higher
- Kafka running on your local machine or accessible via a network
- `kafka-python` library installed (`pip install kafka-python`)

### Usage

1. Make sure your Kafka server is running and accessible via the `bootstrap_servers` parameter in the script (default: `localhost:9092`).
2. Run the Python script.
3. When prompted, press Enter to send a message.
4. Type your message and press Enter again.
5. The message will be sent to the Kafka topic, and the consumer will print the received message.

### Code Overview

The script does the following:

1. Imports necessary modules from the `kafka-python` library.
2. Creates a Kafka topic with one partition and replication factor 1.
3. Initializes a Kafka producer with the specified `bootstrap_servers`.
4. Sends a user-entered message to the Kafka topic with a specified key (encoded in UTF-8).
5. Initializes a Kafka consumer with the specified `bootstrap_servers` and topic name.
6. Continuously consumes messages from the topic, printing the message value (decoded from UTF-8).

### Example

```python
from kafka import *
from kafka.admin import *

# Create a topic
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
topic_list = [NewTopic(name="loay_12", num_partitions=1, replication_factor=1)]
admin_client.create_topics(new_topics=topic_list, validate_only=False)

# Get user input
_input = input('press enter to send message')

# Create a producer
producer = KafkaProducer(retries=5, bootstrap_servers=['localhost:9092'])

# Produce a message
producer.send('loay_12', key='loay-key'.encode('utf-8'), value=_input.encode('utf-8'))
producer.flush()

# Create a consumer
consumer = KafkaConsumer('loay_12', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=True)

# Consume messages and print them
for message in consumer:
    print(message.value.decode('utf-8'))
```

### Troubleshooting

- Ensure the Kafka server is running and accessible via the `bootstrap_servers` parameter.
- If you encounter any issues with the script or library, refer to the [official `kafka-python` documentation](https://kafka-python.readthedocs.io/en/master/).
