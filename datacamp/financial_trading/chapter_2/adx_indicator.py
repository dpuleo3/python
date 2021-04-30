import talib
import matplotlib.pyplot as plt

# Calculate the ADX with the default time period
stock_data['ADX_14'] = talib.ADX(stock_data['High'],
                            stock_data['Low'], 
                            stock_data['Close'])

# Calculate the ADX with the time period set to 21
stock_data['ADX_21'] = talib.ADX(stock_data['High'],
                            stock_data['Low'], 
                            stock_data['Close'],
                            timeperiod=21)

# Print the last five rows
print(stock_data.tail())


# Calculate ADX
stock_data['ADX'] = talib.ADX(stock_data['High'], stock_data['Low'], stock_data['Close'])

# Create subplots
fig, (ax1, ax2) = plt.subplots(2)

# Plot ADX with the price
ax1.set_ylabel('Price')
ax1.plot(stock_data['Close'])
ax2.set_ylabel('ADX')
ax2.plot(stock_data['ADX'], color='red')

ax1.set_title('Price and ADX')
plt.show()