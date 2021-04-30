import talib
import matplotlib.pyplot as plt

# Define the Bollinger Bands with 1-sd
upper_1sd, mid_1sd, lower_1sd = talib.BBANDS(bitcoin_data['Close'], 
                                     nbdevup=1,
                                     nbdevdn=1,
                                     timeperiod=20)
# Plot the upper and lower Bollinger Bands 
plt.plot(bitcoin_data['Close'], color='green', label='Price')
plt.plot(upper_1sd, color='tomato', label="Upper 1sd")
plt.plot(lower_1sd, color='tomato', label='Lower 2sd')

# Customize and show the plot
plt.legend(loc='upper left')
plt.title('Bollinger Bands (1sd)')
plt.show()


# Define the Bollinger Bands with 2-sd
upper_2sd, mid_2sd, lower_2sd = talib.BBANDS(bitcoin_data['Close'],
                                                nbdevup=2,
                                                nbdevdn=2,
                                                timeperiod=20)
# Plot the upper and lower Bollinger Bands 
plt.plot(bitcoin_data['Close'], color='green', label='Price')
plt.plot(upper_2sd, color='orange', label='Upper 2sd')
plt.plot(lower_2sd, color='orange', label='Lower 2sd')

# Customize and show the plot
plt.legend(loc='upper left')
plt.title('Bollinger Bands (2sd)')
plt.show()