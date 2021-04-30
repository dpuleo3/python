# MEAN-VARIANCE PORTFOLIO OPTIMIZATION
# The percent return is the y-axis of a mean-variance
# Before we can calculate the expected return of a portfolio, we need to find the expected return of each asset.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


##Expected Return I
path='stock_data.csv'
stock_data = pd.read_csv(path)

lst = list(stock_data.columns[1:])
quarterly_returns = stock_data[lst].pct_change()
expected_returns_avg = quarterly_returns.mean()

try:
  print(expected_returns_avg)
except:
  print('Calculate the average quarterly expected returns and save it to expected_returns_avg.')


##Expected Return II
# Weight of an Asset
# Fraction of the money invested in the asset (the numerator of the fraction below), 
# divided by the total amount of money in the portfolio (the denominator of the fraction below):

weight_nike = 3000 / 10000

weight_ua = 2000 / 10000

weight_skechers = 5000 / 10000

try:
  print(f'The weight invested in Nike is {weight_nike}')
except:
  print('You did not create the weight_nike variable yet')
try:
  print(f'The weight invested in Under Armour is {weight_ua}')
except:
  print('You did not create the weight_ua variable yet')
try:
  print(f'The weight invested in Skechers is {weight_skechers}')
except:
  print('You did not create the weight_skechers variable yet')


##Expected Return III
#To calculate the expected return of a portfolio, you must find the weighted sum of the return for each individual asset:
expected_return = .8*1.4 + .16*0.8 + .04*7

try:
  print('The expected return is equal to {:.2f}%'.format(expected_return))
except:
  print('You did not create the expected_return variable yet')


##Covariance Matrix I
# Positive covariance — when one asset increases in value, the other usually increases in value. The covariance value will be greater than 0.
# Negative covariance — when one asset increases in value, the other usually decreases in value. The covariance value will be less than 0.
# Uncorrelated assets — when there is no quantifiable pattern to the response of two assets. The covariance value is equal to 0.

##Covariance Matrix II
path='stock_data.csv'

stock_data = pd.read_csv(path)
selected=list(stock_data.columns[1:])

returns_quarterly = stock_data[selected].pct_change()
expected_returns = returns_quarterly.mean()

print(stock_data)
#To calculate the covariance of these assets, we can use the pandas .cov()
returns_cov = returns_quarterly.cov()

try:
	print(returns_cov.round(4))
except:
  pass


