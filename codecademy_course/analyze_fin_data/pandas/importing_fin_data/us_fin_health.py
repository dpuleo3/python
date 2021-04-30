import pandas as pd
#importing for Nasdaq and S&P data
import pandas_datareader.data as web
#importing for World Bank data
import pandas_datareader.wb as wb 
#importing datetime
from datetime import datetime
#to calculate log_returns
import numpy as np

gold_prices = pd.read_csv('gold_prices.csv')
print(gold_prices)

crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
print(crude_oil_prices)

start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)

#nasdaq data
nasdaq_data = web.DataReader('NASDAQ100', 'fred', start, end)
#s&p data
sap_data = web.DataReader('SP500', 'fred', start, end)
#world bank data
gdp_data = wb.download(indicator= 'NY.GDP.MKTP.CD', country = ['us'], start = start, end = end )
export_data = wb.download(indicator = 'NE.EXP.GNFS.CN', country = ['US'], start = start, end = end)

#Calculating Log Return
def log_return(prices):
  return np.log(prices / prices.shift(1))

gold_returns = log_return(gold_prices.Gold_Price)
crud_oil_returns = log_return(crude_oil_prices.Crude_Oil_Price)
nasdaq_returns = log_return(nasdaq_data.NASDAQ100)
sap_returns = log_return(sap_data.SP500)
gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])
export_returns = log_return(export_data['NE.EXP.GNFS.CN'])

#Comparing Return Volatility
print('gold:', gold_returns.var())
print('oil:', crud_oil_returns.var())
print('nadaq:', nasdaq_returns.var())
print('s&p500:', sap_returns.var())
print('gdp_returns:', gdp_returns.var())
print('export_returns:', export_returns.var())