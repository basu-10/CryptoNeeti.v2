db user/pass:	user='user_dbadmin', password='121212',host='localhost',database='crypto_data'
db cols:		coin_pair, change_24_hour, high, low, volume, last_price, bid, ask, timestamp
db data format:	'BTC/USDT', 0.01, 50000, 45000, 1000000, 48000, 48500, 47500, '2022-03-18 12:00:00'

file working:

## Ticker.py
run as script (as >python Ticker.py) to fetch data at current time, ONCE and write to file temp1
can be used by other scripts to fetch data. main() throws the processed cleaned data.
this files __name__="__main__" writes to file.



## db_insert.py
uses Ticker.py
run only this file (as >python db_insert.py) to save data per 30 secs to db

## db_read.py
run only this file (as >python db_read.py) to read the latest price of ["BTCINR", "ETHINR", "ADAUSDT"]

## terminal.py


## db_test.py