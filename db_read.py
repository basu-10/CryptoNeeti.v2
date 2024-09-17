# run only this file (as >python db_read.py) to read the latest price of ["BTCINR", "ETHINR", "ADAUSDT"]

import mysql.connector
from datetime import datetime

def get_latest_prices(coin_pairs):
    # Connect to the database
    cnx = mysql.connector.connect(user='user_dbadmin', password='121212',
                                  host='localhost',
                                  database='crypto_data')
    cursor = cnx.cursor()

    # Execute the SQL query to retrieve the latest prices for the specified coin pairs
    query = f"SELECT coin_pair, last_price FROM ticker_data WHERE coin_pair IN ({','.join(['%s'] * len(coin_pairs))});"
    cursor.execute(query, tuple(coin_pairs))

    # Fetch the results and return them as a dictionary
    results = cursor.fetchall()
    latest_prices = {}
    for row in results:
        coin_pair, last_price = row
        latest_prices[coin_pair] = float(last_price)
    return latest_prices

if __name__ == "__main__":
    # Get the latest prices for multiple coins
    coin_pairs = ["BTCINR", "ETHINR", "ADAUSDT"]
    latest_prices = get_latest_prices(coin_pairs)
    for coin_pair, price in latest_prices.items():
        print(f"The latest price for {coin_pair} is {price}")