import mysql.connector
from datetime import datetime
import cmd
import time

'''
commands:
cryptokaka> show BTCINR ADAUSDT ETHINR
cryptokaka> show -v BTCINR ADAUSDT ETHINR
cryptokaka> show BTCINR ADAUSDT ETHINR
cryptokaka> ticker 30 -v BTCINR ADAUSDT ETHINR

'''

'''
feature

ctrl+c to stop ticker
ctrl +c to exit terminal 

'''


'''
to do 
ctrl c to go back

'''
class CryptoKakaShell(cmd.Cmd):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt = 'cryptokaka> '

    def do_show(self, coin_pairs):
        '''Show the latest prices for one or more coins.'''
        verbose = '-v' in coin_pairs
        if verbose:
            coin_pairs = coin_pairs.replace('-v', '').split()
        else:
            coin_pairs = coin_pairs.split()
        latest_prices = get_latest_prices(coin_pairs, verbose)
        if verbose:
            for coin_pair, values in latest_prices.items():
                print(f"{coin_pair}:")
                for key, value in values.items():
                    print(f"\t{key}: {value}")
        else:
            for coin_pair, price in latest_prices.items():
                print(f"The latest price for {coin_pair} is {price}")

    def do_ticker(self, args):
        '''Show the latest prices for one or more coins every n seconds.'''
        print("Ctrl+c to stop the run and return to cryptokaka>")
        interval, *coin_pairs = args.split()
        try:
            interval = int(interval)
        except ValueError:
            print('Invalid interval. Please enter a positive integer.')
            return
        if len(coin_pairs) == 0:
            print('Please enter one or more coin pairs.')
            return
        verbose = '-v' in coin_pairs
        if verbose:
            coin_pairs = [coin_pair.replace('-v', '') for coin_pair in coin_pairs]
        else:
            coin_pairs = coin_pairs


        try:
            while True:
                latest_prices = get_latest_prices(coin_pairs, verbose)
                print("")
                if verbose:
                    for coin_pair, values in latest_prices.items():
                        print(f"{coin_pair}:")
                        for key, value in values.items():
                            print(f"\t{key}: {value}")
                else:
                    for coin_pair, price in latest_prices.items():
                        print(f"The latest price for {coin_pair} is {price}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print('Ticker command stopped.')

    def postloop(self):
        print('Exiting CryptoKaka Shell. Goodbye!')
    
    def do_exit(self, args):
        '''Exit the shell.'''
        return True
    

def get_latest_prices(coin_pairs, verbose=False):
    # Connect to the database
    cnx = mysql.connector.connect(user='user_dbadmin', password='121212',
                                  host='localhost',
                                  database='crypto_data')
    cursor = cnx.cursor()

    # Execute the SQL query to retrieve the latest prices for the specified coin pairs
    query = f"SELECT * FROM ticker_data WHERE coin_pair IN ({','.join(['%s'] * len(coin_pairs))}) ;"
    cursor.execute(query, tuple(coin_pairs))

    # Fetch the results and return them as a dictionary
    results = cursor.fetchall()
    latest_prices = {}
    for row in results:
        coin_pair, change_24_hour, high, low, volume, last_price, bid, ask, timestamp = row
        if verbose:
            latest_prices[coin_pair] = {
                'change_24_hour': float(change_24_hour),
                'high': float(high),
                'low': float(low),
                'volume': float(volume),
                'last_price': float(last_price),
                'bid': float(bid),
                'ask': float(ask),
                'timestamp': timestamp
            }
        else:
            latest_prices[coin_pair] = float(last_price)
    return latest_prices

if __name__ == "__main__":
    try: 
        shell = CryptoKakaShell()
        shell.cmdloop()
    except KeyboardInterrupt:
            print('byeee')