#pandas_datareader to get gdp data from the World Bank API.
from pandas_datareader import wb
from datetime import datetime

start = datetime(2005, 1, 1)
end = datetime(2008, 1, 1)
indicator_id = 'NY.GDP.PCAP.KD'

gdp_per_capita = wb.download(indicator=indicator_id, start=start, end=end, country=['US', 'CA', 'MX'])

print(gdp_per_capita)

#importing NASDAQ symbols (tickers)
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols

symbols = get_nasdaq_symbols()

#importing the daily price of the S&P 500 
from datetime import datetime
import pandas_datareader.data as web

start = datetime(2019, 1, 1) # year, month, day
end = datetime(2019, 2, 1)

sap_data = web.DataReader('SP500', 'fred', start, end)

#----------------------------------------------------------------------------------------------------------------

# shifts all rows down by 1
dataframe.shift(1); 
# shifts all rows in name column up 5
dataframe['name'].shift(-5); 
# shifts all rows in the price column down 3
dataframe['price'].shift(3);

# calculate the percentage of growth between one row and the next
start = datetime(2008, 1, 1)
end = datetime(2018, 1, 1)

gdp = web.DataReader('GDP', 'fred', start, end)
#crea la columna growth con los calculos
gdp['growth'] = gdp['GDP'] - gdp['GDP'].shift(1)
print(gdp)

#----------------------------------------------------------------------------------------------------------------

import pandas_datareader.tsp as tsp
from datetime import datetime

start = datetime(2009, 1, 1)
end = datetime(2019, 1, 1)

tsp_data = tsp.TSPReader(start,end).read()
print(tsp_data)
#prints the variance of the values
print(tsp_data.var())
#prints the covariance of the values
#describes the relationship between the returns on two different investments over a period of time, 
#and can be used to help balance a portfolio.
print(tsp_data.cov())


# Python is able to import financial data from csv files as well as public financial APIs.
# The pandas read_csv function can be used to import data from a csv file into a pandas dataframe.
# Pandas-datareader makes it easy to import data from public financial APIs.
# Python’s datetime function can be used to create datetime objects which are often used to specify time ranges for financial data.
# API keys are unique identifiers required for some APIs in order to access data.
# Sometimes APIs can be flaky. To mitigate the damage this might cause it’s best to test your code often and keep up to date with the pandas-datareader documentation and GitHub page.
# The shift function can be used on the rows in a DataFrame column to shift them up or down.
# Pandas provides common statistical functions like var and cov to make it easy to calculate variance and covariance on a dataset.