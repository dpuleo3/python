from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

plt.figure(figsize = (12, 8))

#Primer grafico
ax1 = plt.subplot(2,1,1)
x_values = range(len(months))
plt.plot(x_values, visits_per_month, color = 'red', marker= 'o')
plt.xlabel('Month')
plt.ylabel('Visits per Month')
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.title('Sublime Limes Line Graphs / VISITS')
plt.subplots_adjust(wspace = 0.35, bottom = 0.01)

#Segundo grafico
ax2 = plt.subplot(2,1,2)
plt.plot(x_values, key_limes_per_month, color = 'yellow')
plt.plot(x_values, persian_limes_per_month, color = 'blue')
plt.plot(x_values, blood_limes_per_month, color = 'red')
legend_labels = ["Key", "Persian", "Blood"]
ax2.legend(legend_labels, loc = 1)
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.title('Sublime Limes Line Graphs / SALES')

plt.show()
plt.savefig('sublime_lime_graphs.png')


##Fill Between
# x-values — this works just like the x-values of plt.plot
# lower-bound for y-values — sets the bottom of the shared area
# upper-bound for y-values — sets the top of the shared area
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

plt.plot(months, revenue,  color='red')
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
#real revenue will probably be plus or minus 10% of each value.
y_lower = [i - 0.1 * i for i in revenue]
y_upper = [1.1 * i for i in revenue]
#.fill_between() to shade the error above and below the line we’ve plotted
plt.fill_between(months, y_lower, y_upper, alpha=0.2, color='orange')