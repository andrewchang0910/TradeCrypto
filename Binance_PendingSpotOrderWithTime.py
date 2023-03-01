import time
from binance.client import Client
import configparser


def PandingOrder(client, symbol, side, quantity, price, time_in_force):
    # Place a limit order
    # symbol = 'BUSDUSDT'  # symbol to trade
    # side = 'BUY'  # side of the order
    # quantity = 100  # amount to buy/sell
    # price = 0.2  # price to buy/sell at
    # time_in_force = 'GTC'  # time in force of the order
    response = client.create_order(
        symbol=symbol,
        side=side,
        type='LIMIT',
        timeInForce=time_in_force,
        quantity=quantity,
        price=price
    )
    # Print the response
    return response


if __name__ == '__main__':
    # Read Env config
    config = configparser.ConfigParser()
    config.read('config.ini')
    # Set up the Binance API client
    api_key = config['Binance']['binance_api']  # Fill the key in config file
    api_secret = config['Binance']['binance_secret']  # Fill the key in config file
    client = Client(api_key, api_secret)
    timestamp = 1655834  # timestamp(fill the time with the coin can be exchange)

    # main
    while (True):
        try:
            if (timestamp < time.time()):
                res = PandingOrder(client=client, symbol='BUSDUSDT', side='BUY', quantity=100, price=0.2,
                                   time_in_force='GTC')
                if res['orderId'] > -1:
                    print("Successful Pending Limit Order")
                    print(res)
                    break
            else:
                print("Waiting for time up...")
        except Exception:
            print("Something Error")
