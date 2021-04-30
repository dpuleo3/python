from matplotlib import pyplot as plt
#provided data in the file sales_times.csv and loaded it into a list called sales_times
from script import sales_times

# Histogram
# plt.hist finds the minimum and the maximum values in your dataset and creates 10 equally-spaced bins between those values.
# range selects the minimum and maximum values to plot
# bins to set how many bins we want to divide the data into.
plt.hist(sales_times, range=(8,22), bins=20)


## Multiple Histograms
# alpha, which can be a value between 0 and 1. This sets the transparency of the histogram. 
# histtype with the argument 'step' to draw just the outline of a histogram
# we can normalize our histograms using normed=True.
from script import sales_times1
from script import sales_times2

plt.hist(sales_times1, bins=20, alpha=0.4, normed=True)
plt.hist(sales_times2, bins=20, alpha=0.4, normed=True)