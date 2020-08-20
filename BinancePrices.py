"""
stores in the prices as listed in Binance.us real time
"""
from Binance import BinanceAPI
import time

def main():
    with open('DataFiles/.hidden.txt', 'r') as f:
        API_KEY = f.readline().strip()
    client = BinanceAPI(API_KEY)
    
    while True:
        with open("DataFiles/BTCUSD.csv", "a") as csv_file:
            datum = client.get_price("BTCUSD")
            csv_file.write(f"{datum['bidPrice']},{datum['bidQty']},{datum['askPrice']},{datum['askQty']},{datum['timestamp']}\n")
        with open("DataFiles/BNBUSD.csv", "a") as csv_file:
            datum = client.get_price("BNBUSD")
            csv_file.write(f"{datum['bidPrice']},{datum['bidQty']},{datum['askPrice']},{datum['askQty']},{datum['timestamp']}\n")
        time.sleep(.9)

main()