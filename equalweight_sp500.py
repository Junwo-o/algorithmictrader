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

# symbol = 'MSFT'
# stock = yf.Ticker(symbol)
# price = stock.info['currentPrice']
# market_cap = stock.info['marketCap']


# tickers = yf.Tickers('MSFT AAPL GOOG')
# dat = yf.Ticker("BRK.B")
# print(dat.info)

# yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo')

columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares to Buy']
final_df = pd.DataFrame(columns = columns)

# df.append() removed after pandas 2.0
# new_row = pd.DataFrame([
#     [symbol, price, market_cap, 'N/A']
# ], columns = columns)
# final_df = pd.concat([final_df, new_row], ignore_index=True)
# for ticker in tickers:
#     stock = yf.Ticker(ticker)
#     final_df = pd.concat([final_df, pd.DataFrame([[ticker, stock.info['currentPrice'], stock.info['marketCap'], 'N/A']], columns = columns)], ignore_index=True)
# print(final_df)

tickers = [t.replace('.', '-') for t in tickers]
for ticker in tickers:
    stock = yf.Ticker(ticker)
    try:
        price = stock.info['currentPrice']
        market_cap = stock.info['marketCap']
    except KeyError:
        print(f"Data missing for {ticker}")
        continue

    final_df = pd.concat([
        final_df,
        pd.DataFrame([[ticker, price, market_cap, 'N/A']], columns=columns)
    ], ignore_index=True)
print(final_df)