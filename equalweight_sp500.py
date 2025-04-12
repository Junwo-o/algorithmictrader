import numpy as np
import pandas as pd
import yfinance as yf
import time


start_time = time.time()
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

# df.append() removed after pandas 2.0

tickers = [t.replace('.', '-') for t in tickers] # yfinance formats tickers like BRK.B as BRK-B

# this way of getting info from yfinance is slow

# def spinning(loading):
#     spinner = ['-', '\\', '|', '/', '-', '\\', '|', '/']
#     while loading:
#         for line in spinner:
#             sys.stdout.write('\r' + line)
#             sys.stdout.flush()
#             time.sleep(0.3)


print("Retrieving S&P 500 data, may take up to 5 minutes")
rows = []
for ticker in tickers:
    stock = yf.Ticker(ticker)
    try:
        price = stock.info['currentPrice']
        market_cap = stock.info['marketCap']
        rows.append([ticker, price, market_cap, 'N/A'])
    except KeyError:
        print(f"Data missing for {ticker}")
        continue
    # final_df = pd.concat([
    #     final_df,
    #     pd.DataFrame([[ticker, price, market_cap, 'N/A']], columns=columns)
    # ], ignore_index=True)
columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares to Buy']
final_df = pd.DataFrame(rows, columns=columns)

end_time = time.time()
elapsed = end_time - start_time
minutes, seconds = int(elapsed // 60), int(elapsed % 60)
print(f"\nTask completed in {minutes} minutes and {seconds} seconds.")
print(final_df)

# attempted to make groups of calls to yfinance but found out to get fundamental data the only option is to loop through each ticker
# from https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
# def chunks(lst, n):
#     """Yield successive n-sized chunks from lst."""
#     for i in range(0, len(lst), n):
#         yield lst[i:i + n]
# tickers_grouped = list(chunks(tickers, 100))
# tickers_combined = []
# for i in range(len(tickers_grouped)):
#     tickers_combined.append(','.join(tickers_grouped[i]))