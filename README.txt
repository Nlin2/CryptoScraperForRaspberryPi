crontab -e
# be sure to change the absolute
0 0 * * * /Users/{user_name}/anaconda3/bin/python /Users/{user_name}/Documents/GitHub/RaspPi_Crypto_Bot_Trader/EmailUpdater.py >/dev/null 2>&1

python BinancePrices.py
