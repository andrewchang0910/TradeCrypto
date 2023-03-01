import os
from binance.client import Client
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
# Set up the Binance API client
api_key = config['Binance']['binance_api']
api_secret = config['Binance']['binance_secret']
client = Client(api_key, api_secret)

# Place a limit order
symbol = 'BUSDUSDT'  # symbol to trade
side = 'BUY'  # side of the order
quantity = 100  # amount to buy/sell
price = 0.2  # price to buy/sell at
time_in_force = 'GTC'  # time in force of the order
response = client.create_order(
    symbol=symbol,
    side=side,
    type='LIMIT',
    timeInForce=time_in_force,
    quantity=quantity,
    price=price
)

# Print the response
print(response)
