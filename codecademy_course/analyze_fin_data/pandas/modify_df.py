import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)

#Arega una columna completa con Yes de valor
df['Is taxed?'] = 'Yes'
print(df)

#Crea la columna Margin
df['Margin'] = df.Price - df['Cost to Manufacture']
df['Revenue'] = df.Price - df['Cost to Manufacture']
print(df)

#Crea una columna con los valores de 'Name' en minuscula
def lowercase(my_string):
  return my_string.lower()

df['Lowercase Name'] = df['Name'].apply(lowercase)
print(df)