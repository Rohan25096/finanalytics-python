import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from profile import df_holdings
import yfinance as yf

df_holdings[['tradingsymbol', 'quantity', 'average_price', 'last_price', 'pnl']].to_string(index=False)

#Function to print the total quantities.
def cal_qty():
    qty = df_holdings['quantity']
    arr = qty.to_numpy()

    total_qty=0
    for qty in arr:
        total_qty = total_qty + qty
    print("Total Quantity:",total_qty)

#Weightage of all stocks in portfolio
def cal_weightage():
    weight = df_holdings[['tradingsymbol','quantity']]
    weight['weightage'] = pd.Series(dtype='int')
    weight['weightage'] = (round(((weight['quantity']/43)*100),2))
    print(weight)

#Fetching securities past data
def data_fetching():
    tickers = []
    final_tickers = []
    for i in df_holdings['tradingsymbol']:
        tickers.append(i)
    data = pd.DataFrame
    for t in tickers:
        final_tickers.append(t + '.NS')
        data = yf.download(final_tickers, start='2024-10-01', end='2025-06-18', interval='1mo')['Close']

