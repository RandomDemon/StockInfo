#  Stock Info 
#  Created by Collin Aguiar and Cameron Hagan
#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
import yfinance as yf
from time import sleep as wait

while True:
    stockChoice = input("What stock would you like information on? \n")

    Stock = yf.Ticker(stockChoice)
    market_price = Stock.info['regularMarketPrice']
    previous_close_price = Stock.info['regularMarketPreviousClose']
    mNews = Stock.news
    print(Stock)
    wait(0.5)
    print('Market Price:', market_price)
    wait(0.5)
    print('Previous Close Price:', previous_close_price)
    wait(3)
    doAgain=input('Would you like to research another stock? (y/n) \n')
    if doAgain == 'n':
        break
    elif doAgain == 'y':
        pass
    else:
        print("Couldn't understand that!")