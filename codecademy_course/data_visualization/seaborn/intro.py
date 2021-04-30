# Seaborn is a Python data visualization library that provides simple code to create elegant visualizations 
# for statistical exploration and insight. 
# Seaborn is based on Matplotlib, but improves on Matplotlib in several ways:

# Seaborn provides a more visually appealing plotting style and concise syntax.
# Seaborn natively understands Pandas DataFrames, making it easier to plot data directly from CSVs.
# Seaborn can easily summarize Pandas DataFrames with many rows of data into aggregated charts.
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt

import seaborn as sns # <<----

df = pd.read_csv('survey.csv')
sns.barplot(x='Age Range', y='Response', hue='Gender', data=df)
plt.show()

# The Seaborn function sns.barplot(), takes at least three keyword arguments:

# data: a Pandas DataFrame that contains the data (in this example, data=df)
# x: a string that tells Seaborn which column in the DataFrame contains otheur x-labels (in this case, x="Gender")
# y: a string that tells Seaborn which column in the DataFrame contains the heights we want to plot 
#   for each bar (in this case y="Mean Satisfaction")
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('results.csv')
print(df)

sns.barplot(
	data= df,
	x= 'Gender',
	y= 'Mean Satisfaction'
)
plt.show()


import numpy as np

gradebook = pd.read_csv("gradebook.csv")
print(gradebook)

# guarda los datos de 'Assignment 1'
assignment1 = gradebook[gradebook.assignment_name == 'Assignment 1']
print(assignment1)

# se una numpy para calcular el promedio
asn1_median = np.median(assignment1.grade)
print(asn1_median)

# plot the average grade for each assignment. 
sns.barplot(
	data= gradebook,
	x= 'assignment_name',
	y= 'grade'
)
plt.show()

# error bars represent one standard deviation (ci="sd"), rather than 95% confidence intervals.
sns.barplot(data=gradebook, x="name", y="grade", ci="sd")
plt.show()

# Estimator accepts any function that works on a list
df = pd.read_csv("survey.csv")
print(df)

sns.barplot(
  data= df,
  x= 'Gender',
  y= 'Response',
  estimator=len
)
plt.show()

sns.barplot(
  data= df,
  x= 'Gender',
  y= 'Response',
  estimator=np.median
)
plt.show()


# The hue parameter adds a nested categorical variable to the plot.
df = pd.read_csv("survey.csv")

sns.barplot(
  data= df,
  x= 'Age Range',
  y= 'Response',
  hue= 'Gender'
)
plt.show()