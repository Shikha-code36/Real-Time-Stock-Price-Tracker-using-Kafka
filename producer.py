import yfinance as yf
from confluent_kafka import Producer
from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC, API_KEY, API_SECRET

# Initialize Kafka producer
producer = Producer({
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': API_KEY,
    'sasl.password': API_SECRET,
})

# Define a flag to control the producer thread
produce_data = False

historical_data = []

def fetch_stock_price(symbol):
    global produce_data, historical_data  # Access the global flags 

    while True:
        try:
            if produce_data:  # Check if we should produce data
                stock = yf.Ticker(symbol)
                price = stock.history(period='1m')['Close'].iloc[-1]
                message = f'{symbol}:{price}'  # Combine symbol and price
                producer.produce(KAFKA_TOPIC, value=message)
                print(f'Sent {symbol} price: {price}')

                # Append historical data
                historical_data.append({'symbol': symbol, 'price': price})
        except Exception as e:
            print(f'Error sending data: {e}')

# Function to start or stop data production
def toggle_producer(flag):
    global produce_data
    produce_data = flag
