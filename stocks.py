import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tickers = ['BHEL.NS','SAIL.NS','BSE.NS','HAL.NS']
for t in tickers:
    data = yf.download(tickers, start='2024-01-01', end='2025-05-22')['Close']

#Normalization of the datas to avoid noise in the data
(data/data.iloc[0]*100).plot(figsize=(15,8))
plt.show()

#Without Normalization
data.plot(figsize=(15,6))
plt.show()

#Calculating the return of portfolio of securities.
returns = (data/data.shift(1))-1
returns.head()

#Calculating the average annual returns of each stock.
avg_annual_returns = returns.mean()*250
avg_annual_returns.head()

#Logarithmic returns
log_returns = np.log(data / data.shift(1))

log_returns_mean = log_returns.mean()*250

SD = log_returns.std()
SD_main = log_returns.std() * 250 ** 0.5  #In this part we are calculating the standard deviation 
                                #on basis of the number of trading sessions, and taking out out the root of 250.
print("The standard deviations, are directly associated with the risk involved in the securities:",SD_main)