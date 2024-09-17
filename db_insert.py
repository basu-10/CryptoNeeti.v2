
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# db, table needs to be created first with : mysql> create database crypto_data;
# run only this file (as >python db_insert.py) to save data per 30 secs to db

import time
import mysql.connector
from Ticker import main  # Import the main function from ticker.py
from datetime import datetime

def insert_into_db(data):
    # Start timer
    start_time = time.perf_counter()

    # Connect to MySQL database
    cnx = mysql.connector.connect(user='user_dbadmin', password='121212',
                                  host='localhost',
                                  database='crypto_data')
    cursor = cnx.cursor()

    # Insert data
    cursor.executemany('''
        INSERT INTO ticker_data (coin_pair, change_24_hour, high, low, volume, last_price, bid, ask, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', data)

    # Commit and close
    cnx.commit()
    cursor.close()
    cnx.close()

     # Stop timer
    end_time = time.perf_counter()

    # Print time taken to fetch data
    print(f"Data saved to db in {end_time - start_time} seconds")

if __name__ == "__main__":
    count=1
    while True:
        data = main()
        # print("\n fetching data and inserting to db")
        insert_into_db(data)
        print(f"Data #{count} inserted at {datetime.now()}, timestamp: {int(time.time())}")
        print("sleeping...")
        count+=1
        time.sleep(30)
        
        