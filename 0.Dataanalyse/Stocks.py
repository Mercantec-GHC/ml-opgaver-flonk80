import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

stocks = pd.read_csv('G:\\git\\Skole\\Machine Learning\\ml-opgaver-flonk80\\0.Dataanalyse\\Data\\Stocks\\Stocks.csv', index_col=0, parse_dates=True) # Dato fra 2022-10-28 til 2024-10-27
stocks = stocks[stocks.index > '2020-01-01']
stocks = 100 * (stocks / stocks.iloc[0, :])

stocksOrdered = (stocks.iloc[-1] - stocks.iloc[0]).sort_values(ascending=False)

#stocks.plot(loglog=True)
#plt.show()

print(stocks)
print(stocksOrdered)