#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:26:17 2022

@author: linuxlite
"""
'''
self.data looks like
[{'ask': '6050597.440000000000',
  'bid': '5977637.020000000000',
  'change_24_hour': '0.271',
  'high': '6125000.0',
  'last_price': '6051397.510000000000',
  'low': '5900000.5',
  'market': 'BTCINR',
  'timestamp': 1718184420,
  'volume': '12039567.668413848'},
 {'ask': '0.39062',
  'bid': '0.39027',
  'change_24_hour': '0.05',
  'high': '0.3979',
  'last_price': '0.39012',
  'low': '0.3683',
  'market': 'PYTHUSDT',
  'timestamp': 1718184420,
  'volume': '1653448.6508'},

'''


from datetime import datetime
import requests
from pprint import pprint
import time


class ticker:
    
    def __init__(self):     
        #get current ticker
        url = "https://api.coindcx.com/exchange/ticker" # contains data about all the coins in  a single dict
        now = datetime.now()
        try:
            # Start timer
            start_time = time.perf_counter()

            print("\n#fetching from api...")
            response = requests.get(url)
            self.data = response.json()

            # Stop timer
            end_time = time.perf_counter()

            print(f"got new ticker value at : {now} (your machine time) in {end_time - start_time}s")

            # with open ('temp.txt','a+') as f:
            #     pprint(self.data,f)
            # print(data)
    
        except Exception as e:
            print("Exception while gettting ticker: ", e)
    
    
    def get(self):
        '''
        generates the data_li list which hold current ticker value
        used by generate module to push to db
        [(),(),,,]
        '''
        # Start timer
        start_time = time.perf_counter()

        #list of tuples . tuples have individual coin details
        self.data_li=[]
        try:

            for coin in self.data:
                market = coin.get('market')

                if market != 'BTCINR_insta':
                    ask = float(coin.get('ask', 0))
                    bid = float(coin.get('bid', 0))
                    change_24_hour = float(coin.get('change_24_hour', 0))
                    high = float(coin.get('high', 0))
                    last_price = float(coin.get('last_price', 0))
                    low = float(coin.get('low', 0))
                    timestamp = int(coin.get('timestamp', 0))
                    volume = float(coin.get('volume', 0))

                    c=[]
                    
                    if ask and bid and change_24_hour and high and last_price and low and timestamp and volume:
                        
                        c.append(market)
                        c.append(change_24_hour)
                        c.append(high)
                        c.append(low)
                        c.append(volume)
                        c.append(last_price)
                        c.append(bid)
                        c.append(ask)
                        c.append(timestamp)
                    

                        self.data_li.append(tuple(c))
                
        except Exception as e:
            print(f"Exception occured error while extracting values from ticker: {e}")
            print(f'exc while processing {coin}')

        # Stop timer
        end_time = time.perf_counter()    
        # Print time taken to fetch data
        print(f"Data prepared in {end_time - start_time} seconds")    

        return self.data_li
        

def main(): #generates and returns list of coins
    # Initialize the ticker class
    ticker_instance = ticker()
    
    # Get the processed data
    data = ticker_instance.get() # [(),(),,,]
    '''data now looks like 
    [('BTCINR',
        3.15,
        5400000.0,
        5051000.0,
        16829683.670172423,
        5296755.99,
        5296755.99,
        5335000.0,
        1726595485),
        ('SAGAINR',
        11.634,
        164.998,
        135.007,
        917298.8060801151,
        158.472,
        158.681,
        164.4,
        1726595485),'''

    return data
    

if __name__ == "__main__":
    data =main()
    # Print the data
    # for entry in data:
    #     print(entry)
    with open ('temp1.txt','w') as f:
        pprint(data,f)
        print('write to file complete')
    