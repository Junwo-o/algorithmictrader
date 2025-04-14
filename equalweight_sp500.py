import numpy as np
import pandas as pd
import yfinance as yf
import time
import math
import xlsxwriter

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
df = pd.read_html(url)
table = df[0] # choosing first table from the df
tickers = table['Symbol'].tolist() # list of stocks in s&p 500

while True:
    try:
        portfolio = float(input("What is the value of your portfolio?\n"))
        break
    except ValueError:
        print("Please enter a valid number (e.g., 1000000 or 100000.50).")
start_time = time.time()

# df.append() removed after pandas 2.0

tickers = [t.replace('.', '-') for t in tickers] # yfinance formats tickers like BRK.B as BRK-B

# this way of getting info from yfinance is slow however yfinance does not support getting info of a group of tickers unlike apis that allow batch requests

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
    # time.sleep(1.5)

columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares to Buy']
final_df = pd.DataFrame(rows, columns=columns)
position_size = portfolio/len(final_df.index)

for i in range(len(final_df.index)):
    final_df.loc[i, 'Number of Shares to Buy'] = math.floor(position_size/final_df.loc[i, 'Stock Price'])

end_time = time.time()
elapsed = end_time - start_time
minutes, seconds = int(elapsed // 60), int(elapsed % 60)    
print(f"\nTask completed in {minutes} minutes and {seconds} seconds.")
print(final_df)

# exporting to excel
writer = pd.ExcelWriter('recommended_trades.xlsx', engine = 'xlsxwriter')
final_df.to_excel(writer, 'Recommended Trades', index = False)

background_color = '#0a0a23'
font_color = '#ffffff'

string_format = writer.book.add_format(
    {
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)

dollar_format = writer.book.add_format(
    {
        'num_format': '$0.00',
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)

integer_format = writer.book.add_format(
    {
        'num_format': '0',
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)


column_formats = {
    'A': ['Ticker', string_format],
    'B': ['Stock Price', dollar_format],
    'C': ['Market Capitalization', dollar_format],
    'D': ['Number of Shares to Buy', integer_format]
}

# writer.sheets['Recommended Trades'].write('A1', 'Ticker', string_format)
# writer.sheets['Recommended Trades'].write('B1', 'Stock Price', dollar_format)
# writer.sheets['Recommended Trades'].write('C1', 'Market Capitalization', dollar_format)
# writer.sheets['Recommended Trades'].write('D1', 'Number of Shares to Buy', integer_format)

for column in column_formats.keys():
    writer.sheets['Recommended Trades'].write(f'{column}1', column_formats[column][0], column_formats[column][1])

for column in column_formats.keys():
    writer.sheets['Recommended Trades'].set_column(f'{column}:{column}', 18, column_formats[column][1])

# writer.save() doesnt work
writer.close()