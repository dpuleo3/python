from matplotlib import pyplot as plt

#Pie Chart
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs)
#.axis('equal') hace el grafico un circulo perfecto
plt.axis('equal')

plt.show()

##Pie Chart Labeling
budget_data = [500, 1000, 750, 300, 100]
budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']
###Primer metodo
# hace una leyenda aparte
plt.pie(budget_data)
plt.legend(budget_categories)

###Segundo metodo
# pone los nombres justo al lado de donde corresponde cada valor
plt.pie(budget_data, labels=budget_categories)

###Tercer metodo
# autopct calcula y muestra el porcentaje que ocupa cada valor en el grafico
# autopct='%1d%%' redondea hacia arriba o hacia abajo
# autopct='%0.1f%%' coloca 2 decimales
plt.pie(budget_data, labels=budget_categories, autopct='%0.1f%%')