import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
import yfinance as yf
# from tokens import alpaca
# stocks = pd.read_csv('s&p500.csv')
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
df = pd.read_html(url)
table = df[0]
tickers = table['Symbol'].tolist()
ticker = yf.Ticker("AAPL")
hist = ticker.history(period="5d")
close = hist['Close'].tolist()
print(close) 
# symbol = 'APPL'
# api_url = f'apilink{symbol}/quote?token={API_TOKEN}'
# data = requests.get(api_url).json()
# print(data)
# price = data['lastestPrice']
# market_cap = data['marketCap']
# my_columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares']
# final_dataframe = pd.DataFrame(columns = my_columns)
# print(final_dataframe)

# final_dataframe.append(
#     pd.Series(
#     [
#         symbol,
#         price,
#         market_cap,
#         'N/A'
#     ],
#     index = my_columns
#     ),
#     ignore_index=True
# )

# final_dataframe = pd.DataFrame(columns = my_columns)
# for stock in stocks['Ticker'][:5]:
#     api_url = f'apilink{stock}/quote?token={API_TOKEN}'
#     data = requests.get(api_url).json()
#     final_dataframe = final_dataframe.append(
#         pd.Series(
#         [
#             stock,
#             data['lastestPrice'],
#             data['marketCap'],
#             'N/A'
#         ],
#         index = my_columns
#         ),
#         ignore_index=True
#         )
    
# #batch api calls

# def chunks(lst, n):
#     for i in range(0, len(lst), n):
#         yield lst[i:i+n]

# symbol_groups = list(chunks(stocks['Ticker', 100]))
# symbol_strings = []
# for i 