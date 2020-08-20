"""
Checks to see if processes are still running, and sends daily email on progress
"""
import os
import smtplib
import datetime as dt
import time
import subprocess

directory = '/'.join(os.path.realpath(__file__).split('/')[:-1])

# Message wrangling
# Date
today = dt.date.today()
today_str = today.strftime('%B %d, %Y')
yesterday = dt.date.today() - dt.timedelta(days=1)
yesterday_str = yesterday.strftime('%B %d, %Y')

# File Size
btc = f"{directory}/DataFiles/BTCUSD.csv"
bnb = f"{directory}/DataFiles/BNBUSD.csv"
today_btc_size = os.stat(btc).st_size
today_bnb_size = os.stat(bnb).st_size
with open(f"{directory}/DataFiles/sizes.txt", "r") as f:
    yesterday_btc_size = f.readline().strip()
    yesterday_bnb_size = f.readline()
with open(f"{directory}/DataFiles/sizes.txt", "w") as f:
    f.write(f"{today_btc_size}\n{today_bnb_size}")
    
# Memory
with open(f"{directory}/DataFiles/memory.txt", "r") as f:
    yesterday_memory = f.read()
with open(f"{directory}/DataFiles/memory.txt", "w") as f:
    today_memory = subprocess.run(["df", "-h"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    f.write(today_memory)

# Current Processes
processes = subprocess.run(["ps"], stdout=subprocess.PIPE).stdout.decode('utf-8')

# Body that is sent
message = f"{yesterday_str}:\n\tBTCUSD Bytes: {yesterday_btc_size}\n\tBNBUSD Bytes: {yesterday_bnb_size}\n{yesterday_memory}\n\n{today_str}\n\tBTCUSD Bytes: {today_btc_size}\n\tBNBUSD Bytes: {today_bnb_size}\n{today_memory}\n\nRunning Processes:\n{processes}"


# Emailer
with open(f'{directory}/DataFiles/.hidden.txt', "r") as f:
    f.readline()
    f.readline()
    email = f.readline().strip()
    password = f.readline().strip()
    to = f.readline().strip()

sent_from = email
to = [to]
subject = f'Raspberry Pi Scraper Update - {today_str}'
body =f"From: {email}\nTo: {to}\nSubject: {subject}\n\n{message}"
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email, password)
    server.sendmail(sent_from, to, body)
    server.close()
except:
    pass

