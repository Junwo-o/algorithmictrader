import numpy as np
import pandas as pd
import yfinance as yf

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
df = pd.read_html(url)
table = df[0] # choosing first table from the df
tickers = table['Symbol'].tolist() # list of stocks in s&p 500

# apple = yf.Ticker("AAPL")
# hist = apple.history(period="5d")
# close = hist['Close'].tolist()
# print(close)

stock = yf.Ticker("MSFT")
price = stock.info['currentPrice']
market_cap = stock.info['marketCap']
print(market_cap)
