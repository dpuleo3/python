import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ["t-shirt", "t-shirt", "skirt", "skirt"],
  'Color': ["blue", "green", "red", "black"]
})

print(df1)
#--------------------------------------------------------------------
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=[
    #add column names here
    'Store ID', 'Location', "Number of Employees"
  ])

print(df2)
#---------------------------------------------------------------------
#Load CSV a DataFrame in Pandas
df = pd.read_csv('sample.csv')
print(df)

#Save de CSV file in the directory
di = pd.to_csv('new.csv')

df = pd.read_csv('imdb.csv')
#Devuelve las primeras 5 filas de un DataFrame
#si quieres mas filas se coloca df.head(10)
print(df.head())
#Devuelve algunas estadisticas de cada columna
print(df.info())
#--------------------------------------------------------------------
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north  = df.clinic_north
print(clinic_north)

print(type(clinic_north))
print(type(df))

clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))
#guarda solo la data de la columna 3-march
march = df.iloc[2]
print(march)
#guarda la data desde la 4ta a la 6ta columna
april_may_june = df.iloc[3:6]
april_may_june = df.iloc[-3:]
print(april_may_june)
#guarda las primeras 3 columnas
jan_feb_ma = df.iloc[0:3]
print(jan_feb_ma)
#guarda la fila elegida

#guarda la data del mes con el nombre "January"
january = df[df.month == 'January']
print(january)
#guarda la data de los meses elegidos
march_april = df[(df.month == 'March') | (df.month == 'April')]
march_april = df[df.month.isin(['March', 'April'])]
print(march_april)
#guarda las columnas con id 1, 3 y 5
df2 = df.iloc[[1, 3, 5]]
print(df2)


