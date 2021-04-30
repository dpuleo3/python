#Importing matplotlib
from matplotlib import pyplot as plt

##Basic Line Plot  ------------------------------------------------------------------------------------------------
#Using Matplotlib methods, the following code will create a simple line graph using .plot() and display it using .show():
days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]

#.plot(eje_x, eje_y)
plt.plot(days, money_spent)
#muestra la grafica
plt.show()


#Dos lineas en el mismo grafico
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue)
plt.plot(time, costs)


##Linestyles  ------------------------------------------------------------------------------------------------
#linea punteada de color morado
plt.plot(time, revenue, color = 'purple', linestyle = '--')
#linea con cuadrados de color verde claro
plt.plot(time, costs, color = '#82edc9', marker = 's')


##Axis and Labels
# We use plt.axis() by feeding it a list as input. This list should contain:
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

#.axis([eje_x_min, eje_x_max, eje_y_min, eje_y_max])
plt.axis([0, 12, 2900, 3100])

#Labeling the Axes
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')


##Subplots  ------------------------------------------------------------------------------------------------
#The command plt.subplot() needs three arguments to be passed into it:

# The number of rows of subplots
# The number of columns of subplots
# The index of the subplot we want to create

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]
#plot temperature vs months in the left box (eje 2) of a figure that has 1 row with 2 columns.
plt.subplot(1, 2, 2)
plt.plot(temperature, flights_to_hawaii, "o")
#muestra ambos graficos
plt.show()

#.subplots_adjust() has some keyword arguments that can move your plots within the figure:

# left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label
# right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, or decrease it to make room for a legend
# bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or an x-axis label
# top — the top margin, with a default of 0.9
# wspace — the horizontal space between adjacent subplots, with a default of 0.2
# hspace — the vertical space between adjacent subplots, with a default of 0.2
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

#primer grafico
plt.subplot(2, 1, 1)
plt.plot(x, straight_line)
#segundo grafico en eje 3(abajo a la izquierda)
plt.subplot(2, 2, 3)
plt.plot(x, parabola)
#segundo grafico en eje 4(abajo a la derecha)
plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace = 0.35, bottom = 0.01)
plt.show()


##Legends  ------------------------------------------------------------------------------------------------
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#create your legend
legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]
#loc ubica la leyenda dentro del grafico, 1 (esquina superior derecha)
plt.legend(legend_labels, loc = 8)


##Modify Ticks  ------------------------------------------------------------------------------------------------
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

#guarda la union del grafico en ax  
ax = plt.subplot()
#meses en el eje x
ax.set_xticks(months)
#cambia la lista de range(12) y pone la lista de strings
ax.set_xticklabels(month_names)

#coloca los porcentajes especificos de conversion
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
#modifica los numeros por la lista de strings
ax.set_yticklabels(['10%', '25%', '50%', '75%'])


##Figures ------------------------------------------------------------------------------------------------
word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

# clear all existing plots before you plot a new one.
plt.close('all')

plt.plot(years, word_length)
# guarda el grafico en un archivo png; puede ser png, svg y pdf
plt.savefig('winning_word_lengths.png')

#.figure(figsize = (width, height)) predetermina el tamano del grafico
plt.figure(figsize = (7, 3))

plt.plot(years, power_generated)
plt.savefig('power_generated.png')
