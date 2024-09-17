
def insert_into_db():
    conn = sqlite3.connect('crypto_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ticker_data (coin_pair, change_24_hour, high, low, volume, last_price, bid, ask, timestamp)
        VALUES ('BTC/USDT', 0.01, 50000, 45000, 1000000, 48000, 48500, 47500, '2022-03-18 12:00:00')
    ''')
    conn.commit()
    conn.close()
