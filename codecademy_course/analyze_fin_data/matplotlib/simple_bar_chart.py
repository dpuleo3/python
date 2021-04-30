from matplotlib import pyplot as plt

## Bar Charts
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]
#The x-values of the graph should just be the list with the number of categories (drinks) we are plotting
x_values = [0, 1, 2, 3, 4, 5]
# plt.bar function allows you to create simple bar charts to compare multiple categories of data.
# x-axis — famous buildings, y-axis — heights
# x-axis — different planets, y-axis — number of days in the year
# x-axis — programming languages, y-axis — lines of code written by you
plt.bar(x_values, sales)

ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.show()


## Side-By-Side Bars
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element in range(d)]
plt.bar(store1_x, sales1)

n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element in range(d)]
plt.bar(store2_x, sales2)


##Stacked Bars
plt.bar(range(len(drinks)), sales1)
#definir la posicion de las barras, sales2 arriba y sales1 abajo
plt.bar(range(len(drinks)), sales2, bottom=sales1)

legend_labels = ["Location 1", "Location 2"]
plt.legend(legend_labels, loc = 1)


##Error Bars
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
#lista para hacer el plot con yerr
error = [0.6, 0.9, 0.4, 0, 0.9, 0]
#capsize demuestra visualmente el tamano de los error
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)
