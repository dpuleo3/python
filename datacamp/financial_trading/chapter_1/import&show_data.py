import matplotlib.pyplot as plt

# Resample the data to daily by calculating the mean values
eurusd_daily = eurusd_4h.resample('D').mean()

# Print the top 5 rows
print(eurusd_daily.head())


# Resample the data to weekly by calculating the mean values
eurusd_weekly = eurusd_4h.resample('W').mean()

# Print the top 5 rows
print(eurusd_weekly.head())


# Calculate daily returns
tsla_data['daily_return'] = tsla_data['Close'].pct_change() * 100

# Plot the histogram
tsla_data['daily_return'].hist(bins=100, color='red')
plt.ylabel('Frequency')
plt.xlabel('Daily return')
plt.title('Daily return histogram')
plt.show()


# Calculate SMA
aapl_data['sma_50'] = aapl_data['Close'].rolling(window=50).mean()

# Plot the SMA
plt.plot(aapl_data['sma_50'], color='blue', label='SMA_50')
# Plot the close price
plt.plot(aapl_data['Close'], color='red', label='Close')

# Customize and show the plot
plt.title('Simple moving averages')
plt.legend()
plt.show()