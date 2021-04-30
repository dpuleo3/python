import matplotlib.pyplot as plt
import numpy as np
#importing scikit-learn library with the LinearRegression function
from sklearn.linear_model import LinearRegression

temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

plt.plot(temperature, sales, 'o')

#call the function
line_fitter = LinearRegression()
#.fit() method gives the model two variables that are useful
line_fitter.fit(temperature, sales)
#.predict() function to pass in x-values and receive the y-values
sales_predict = line_fitter.predict(temperature)

#create the regression line
plt.plot(temperature, sales_predict, color='')
plt.show()