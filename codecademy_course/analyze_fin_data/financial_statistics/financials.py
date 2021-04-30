from utils import *

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

def get_returns(prices):
  returns=[]
  for i in range(len(prices)-1):
    start_price = prices[i]
    end_price = prices[i+1]
    log_returns = calculate_log_return(start_price,end_price)
    returns.append(log_returns)
  return returns

amazon_returns = get_returns(amazon_prices)
ebay_returns = get_returns(ebay_prices)

amzn = [display_as_percentage(returns) for returns in amazon_returns]
ebay = [display_as_percentage(returns) for returns in ebay_returns]
print('Amazon monthly log returns: ', amzn)
print('Ebay monthly log returns: ', ebay)

amazon_average = sum(amazon_returns) / len(amazon_returns)
ebay_average = sum(ebay_returns) / len(ebay_returns)
print("The monthly average of amazon stock is " + display_as_percentage(amazon_average))
print("The monthly average of ebay stock is " + display_as_percentage(ebay_average))

amzn_annual = sum(amazon_returns)
ebay_annual = sum(ebay_returns)
print('Amazon annual log returns: ', display_as_percentage(amzn_annual))
print('Ebay annual log returns: ', display_as_percentage(ebay_annual))

amzn_variance = calculate_variance(amazon_returns)
ebay_variance = calculate_variance(ebay_returns)
print('Amazon variance: ', display_as_percentage(amzn_variance))
print('Ebay variance: ', display_as_percentage(ebay_variance))

amzn_staddev = calculate_stddev(amazon_returns)
ebay_staddev = calculate_stddev(ebay_returns)
print('Amazon Standart Dev: ', display_as_percentage(amzn_staddev))
print('Ebay Standart Dev: ', display_as_percentage(ebay_staddev))

correlation = calculate_correlation(amazon_returns, ebay_returns)
print('AMZN - EBAY Correlation: ', display_as_percentage(correlation))