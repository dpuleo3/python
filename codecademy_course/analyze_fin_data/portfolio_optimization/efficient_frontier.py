import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
# The function returns a DataFrame with 5,000 portfolios of random asset weights.
from rf import return_portfolios

##Efficient Frontier I
returns_quarterly = pd.read_csv('stock_data.csv')
expected_returns = returns_quarterly.mean()
cov_quarterly = returns_quarterly.cov()

random_portfolios = return_portfolios(expected_returns, cov_quarterly)

print(random_portfolios.head().round(4))


##Efficient Frontier II
path='stock_data.csv'

stock_data = pd.read_csv(path)
selected=list(stock_data.columns[1:])

returns_quarterly = stock_data[selected].pct_change()
expected_returns = returns_quarterly.mean()
#se usa para medir la volatilidad
cov_quarterly = returns_quarterly.cov()

random_portfolios = return_portfolios(expected_returns, cov_quarterly) 

random_portfolios.plot.scatter(x='Volatility', y='Returns')
plt.xlabel('Volatility (Std. Deviation)')
plt.ylabel('Expected Returns')
plt.title('Efficient Frontier')
plt.show()


##Efficient Frontier III
# The optimal_portfolio() function has one parameter:
# returns — the returns for all assets over a specified timeframe
# weights — the weights for each asset in the portfolio
# returns — the expected returns of each portfolio
# risks — the risk of each portfolio, measured as standard deviation
from rf import return_portfolios, optimal_portfolio

path='stock_data.csv'
stock_data = pd.read_csv(path)
selected=list(stock_data.columns[1:])

returns_quarterly = stock_data[selected].pct_change()
expected_returns = returns_quarterly.mean()
cov_quarterly = returns_quarterly.cov()

random_portfolios = return_portfolios(expected_returns, cov_quarterly) 

weights, returns, risks = optimal_portfolio(returns_quarterly[1:])

random_portfolios.plot.scatter(x='Volatility', y='Returns', fontsize=12)

try:
	plt.plot(risks, returns, 'y-o')
except:
  pass
plt.ylabel('Expected Returns',fontsize=14)
plt.xlabel('Volatility (Std. Deviation)',fontsize=14)
plt.title('Efficient Frontier', fontsize=24)
plt.show()