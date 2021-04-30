import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('AAPL_data.csv')
print(df.head())

df['Daily Log Rate of Return'] = np.log(df['Adj Close']/df['Adj Close'].shift(1))

print(df['Daily Log Rate of Return'])

stdev = np.std(df['Daily Log Rate of Return'])
print(stdev)

plt.hist(df['Daily Log Rate of Return'].dropna())
plt.title('Histogram of AAPL Daily Log Rates of Return')
plt.xlabel('Log Rate of Return')
plt.ylabel('Number of Days')
plt.show()