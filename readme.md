start from terminal.py for full funtionality. 
start from db_insert.py to only save data. 
use db_read.py to read the latest data of some selected coins.

Needs the following packages to function:
- mysql (from terminal, pip install mysql)
- requests (from terminal, pip install mysql)


## File working:

### Ticker.py
run as script (as >python Ticker.py) to fetch data at current time, ONCE and write to file temp1 (for debugging)
can be used by other scripts to fetch data from main(). main() throws the processed cleaned data.
this files __name__="__main__" writes to file.

### db_insert.py
uses Ticker.py
run only this file (as >python db_insert.py) to save data per 30 secs to db

### db_read.py
run only this file (as >python db_read.py) to read the latest price of ["BTCINR", "ETHINR", "ADAUSDT"]

### terminal.py


### db_test.py
for debugging only. uses sqlite3 ddatabase, NOT mysql as used in other scripts.
