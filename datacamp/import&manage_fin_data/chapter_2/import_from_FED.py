from pandas_datareader.data import DataReader
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

# Set start date
start = date(1968, 1, 1)

# Set series code
series = 'GOLDAMGBD228NLBM'
data_source = 'fred'

# Import the data
gold_price = DataReader(series, data_source, start)

# Inspect the price of gold
gold_price.info()

# Plot the price of gold
gold_price.plot(title='Gold Price')

# Show the plot
plt.show()


# Set the start date
start = date(1950, 1, 1)

# Define the series codes
series = ['UNRATE', 'CIVPART']
data_source = 'fred'

# Import the data
econ_data = DataReader(series, data_source, start)

# Assign new column labels
econ_data.columns = ['Unemployment Rate', 'Participation Rate']

# Plot econ_data
econ_data.plot(subplots=True, title='Labor Market')

# Show the plot
plt.show()


# Set the start date
start = date(2008, 1, 1)

# Set the series codes
series = ['BAMLHYH0A0HYM2TRIV', 'SP500']

# Import the data
data = DataReader(series, 'fred', start)

# Plot the results
data.plot(subplots=True, title='Performance Comparison')

# Show the plot
plt.show()