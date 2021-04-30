# Bar Charts Hide Information
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Ploting data:
sns.barplot(
  data= df,
  x= 'label',
  y= 'value'
)
plt.show()

## Kernel Density Estimator (KDE Plots):
# plots are preferable to histograms because depending on how you group the data into bins and the width of the bins, 
# you can draw wildly different conclusions about the shape of the data. Using a KDE plot can mitigate these issues, 
# because they smooth the datasets, allow us to generalize over the shape of our data, and aren’t beholden to specific data points.

# sns.kdeplot().
# data - the univariate dataset being visualized, like a Pandas DataFrame, Python list, or NumPy array
# shade - a boolean that determines whether or not the space underneath the curve is shaded

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# KDEplot
sns.kdeplot(set_one, shade=True)
sns.kdeplot(set_two, shade=True)
sns.kdeplot(set_three, shade=True)
sns.kdeplot(set_four, shade=True)
plt.show()


## Box Plots
# The box represents the interquartile range
# The line in the middle of the box is the median
# The end lines are the first and third quartiles
# The diamonds show outliers

# sns.boxplot()
# data - the dataset we’re plotting, like a DataFrame, list, or an array
# x - a one-dimensional set of values, like a Series, list, or array
# y - a second set of one-dimensional data

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Add your code below:
sns.boxplot(
  data= df,
  x= 'label',
  y= 'value'
)
plt.show()


## Violin Plots

# sns.violinplot()
# data - the dataset that we’re plotting, such as a list, DataFrame, or array
# x, y, and hue - a one-dimensional set of data, such as a Series, list, or array
# any of the parameters to the function sns.boxplot()

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Add your code below:
sns.violinplot(
  data= df,
  x= 'label',
  y= 'value'
)
plt.show()


# KDE plot - Kernel density estimator; shows a smoothed version of dataset. Use sns.kdeplot().

# Box plot - A classic statistical model that shows the median, interquartile range, and outliers. Use sns.boxplot().

# Violin plot - A combination of a KDE and a box plot. Good for showing multiple distributions at a time. Use sns.violinplot().
