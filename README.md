# Real-Time Stock Price Monitoring Using Kafka

This project is a real-time stock price monitoring web application built with Flask, Kafka, and Plotly. It allows users to track real-time and historical stock prices of selected companies.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your system.
- Access to a Confluent Cloud Kafka cluster.
- Confluent Kafka Python library installed (included in requirements.txt).
- A valid API key and secret for accessing the Confluent Cloud Kafka cluster.

## Getting Started

To get this project up and running on your local machine, follow these steps:

### 1. Clone the Repository

```sh
git clone https://github.com/Shikha-code36/Real-Time-Stock-Price-Tracker-using-Kafka.git
cd Real-Time-Stock-Price-Tracker-using-Kafka
```

### 2. Set Up a Virtual Environment
It's a good practice to create a virtual environment to isolate project dependencies. Run the following commands to create and activate a virtual environment:
```sh
python -m venv venv
venv\Scripts\activate # On Windows
source ./venv/bin/activate # On Linux & Mac OS X
```
### 3. Install Dependencies
Use pip to install the project's dependencies from the requirements.txt file:
```sh
pip install -r requirements.txt
```
### 4. Configure the Project
Edit the config.py file and provide the following details:

- KAFKA_BOOTSTRAP_SERVERS: The Confluent Cloud 
- Kafka cluster's bootstrap servers.
- KAFKA_TOPIC: The Kafka topic where stock prices will be published and consumed.
- API_KEY: Your Confluent Cloud API key.
- API_SECRET: Your Confluent Cloud API secret.

### 5. Run the Application
Start the Flask web application by running the following command:
```sh
python main.py
```
The app should now be available at http://localhost:5000/.

## Usage
- Visit http://localhost:5000 to access the main dashboard.
- You can start and stop data production and consumption by clicking the respective buttons.
- Real-time and historical stock price charts will be displayed on the dashboard.

## Project Structure
#### The project is organized as follows:

- producer.py: Handles fetching real-time stock prices and publishing them to Kafka.
- consumer.py: Consumes stock price data from Kafka and places it in a queue for the main thread.
- main.py: The main Flask application that serves the web interface.
- config.py: Configuration file for Kafka and API credentials.
- templates/: Contains HTML templates for the web pages.

## Configuration
In the config.py file, you can configure the following settings:

- KAFKA_BOOTSTRAP_SERVERS: The Kafka bootstrap servers.
- KAFKA_TOPIC: The Kafka topic for stock price data.
- API_KEY: Your Confluent Cloud API key.
- API_SECRET: Your Confluent Cloud API secret.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
