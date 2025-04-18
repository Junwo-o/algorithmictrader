import yfinance as yf
import pandas as pd
import numpy as np

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
df = pd.read_html(url)
table = df[0]
ticker = table['Symbol'].tolist()
name = table['Security'].tolist()
sector = table['GICS Sector'].tolist()
sub_sector = table['GICS Sub-Industry'].tolist()

tickers = yf.Tickers('MSFT AAPL GOOG')
output = tickers.tickers['MSFT'].info
new_output = yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo', auto_adjust=False)
print(new_output)

data = yf.download(tickers, period="1d", group_by='ticker', threads=True)

# Example: Get today's close for AAPL
print(data['AAPL']['Close'])
data.to_csv("sp500_prices.csv")

import pandas as pd
data = pd.read_csv("sp500_prices.csv", header=[0,1], index_col=0)

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

# Open	The stock’s price at the start of the trading period (day, minute, etc.)
# High	The highest price the stock traded at during the period
# Low	The lowest price during the period
# Close	The final trading price at the end of the period
# Volume	The total number of shares traded during the period
# Dividends (optional)	If a dividend was paid that day
# Stock Splits (optional)	If a split occurred on that day

# Get historical market data
# hist = ticker.history(period="1d", interval="1m")  # options: "1d", "5d", "1mo", "3mo", "1y", etc.

# print(hist)

    # final_df = pd.concat([
    #     final_df,
    #     pd.DataFrame([[ticker, price, market_cap, 'N/A']], columns=columns)
    # ], ignore_index=True)

# def spinning(loading):
#     spinner = ['-', '\\', '|', '/', '-', '\\', '|', '/']
#     while loading:
#         for line in spinner:
#             sys.stdout.write('\r' + line)
#             sys.stdout.flush()
#             time.sleep(0.3)
    