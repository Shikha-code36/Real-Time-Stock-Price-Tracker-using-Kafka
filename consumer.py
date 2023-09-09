from confluent_kafka import Consumer, KafkaError
from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC, API_KEY, API_SECRET
from queue import Queue
import logging


# Initialize Kafka consumer
consumer = Consumer({
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': API_KEY,
    'sasl.password': API_SECRET,
    'group.id': 'stock_price_group',
    'auto.offset.reset': 'latest',
})

# Create a queue to pass data to the main thread
kafka_data_queue = Queue()

def consume_stock_prices():
    consumer.subscribe([KAFKA_TOPIC])

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                logging.error(f'Error while consuming: {msg.error()}')
        else:
            # Parse the received message and put it in the queue
            try:
                value = msg.value().decode("utf-8")
                symbol, price = value.split(":")
                kafka_data_queue.put({'symbol': symbol, 'price': float(price)})
                print(f'Recieved {symbol} price: {price}')
            except Exception as e:
                logging.error(f'Error parsing message: {e}')

# Function to start or stop data consumption
def toggle_consumer(flag):
    global consume_data
    consume_data = flag
