#!/usr/bin/env python3

import yfinance as yf
import time
import requests
from datetime import datetime

STOCK_CODE = "AAPL"

def get_stock_data_in_1day(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")
#end_def

def send_telegram_message(msg):
    TOKEN = "7979531835:AAGiJuuOOvzeO_-qbaZt39S45KPmq8Tr6hA"
    CHAT_ID = "5354904842"
    CONTENT = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]\n{msg}'
    reponse = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
        data={"chat_id": CHAT_ID, "text": CONTENT}
        )
    status = 'SUCCESS'
    if (reponse.status_code != 200): 
        status = 'FAILED'
    print(f'[SENT][{status}]')
    print(f'{CONTENT}')
#end_def

def main():
    prev_price = 0

    data = get_stock_data_in_1day(STOCK_CODE)
    curr_price = data['Close'].iloc[-1]

    isSatified = False
    if(curr_price > (prev_price + (0.02*prev_price))):
        isSatified = True
    if(curr_price < (prev_price - (0.02*prev_price))):
        isSatified = True

    if(isSatified):
        msg = f'[{STOCK_CODE}] price: {curr_price}\n'
        send_telegram_message(msg)
        prev_price = curr_price
#end_def

### running ###
main()

