import bt

# Obtain all backtest stats
resInfo = bt_result.stats

# SHARP RATIO
# Get annual return and volatility
yearly_return = resInfo.loc['yearly_mean']
print('Annual return: %.2f'% yearly_return)
yearly_vol = resInfo.loc['yearly_vol']
print('Annual volatility: %.2f'% yearly_vol)

# Calculate the Sharpe ratio manually
sharpe_ratio = yearly_return / yearly_vol
print('Sharpe ratio calculated: %.2f'% sharpe_ratio)

# Print the Sharpe ratio
print('Sharpe ratio %.2f'% resInfo.loc['yearly_sharpe'])


# SORTINO RATIO
# Print annual Sortino ratio
yearly_sortino = resInfo.loc['yearly_sortino']
print('Annual Sortino ratio: %.2f'% yearly_sortino)

# Print monthly Sortino ratio
monthly_sortino = resInfo.loc['monthly_sortino']
print('Monthly Sortino ratio %.2f'% monthly_sortino)