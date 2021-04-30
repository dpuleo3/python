import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders.head(10))

#guarda el valor maximo
most_expensive = orders.price.max()
#guarda la cantidad de elementos diferentes
num_colors = orders.shoe_color.nunique()

#guarda los valores maximos del elemento
pricey_shoes = orders.groupby('shoe_type').price.max()
#This will transform our Series into a DataFrame and move the indices into their own column.
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)

#calculate the 25th percentile for shoe price for each shoe_color to help Marketing decide if we have enough cheap shoes on sale. 
#hay que importar numpy para usar np.percentile()
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()
print(cheap_shoes)

# total number of shoes of each shoe_type/shoe_color combination purchased.
#agrupar 2 o mas columnas
shoe_counts = orders.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index()
#crea una tabla pivote para el shoe_counts
shoe_counts_pivot = shoe_counts.pivot(columns='shoe_color', index='shoe_type',values=('id')).fillna(0).astype(int).reset_index()
print(shoe_counts_pivot)