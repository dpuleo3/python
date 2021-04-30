from string import lower
import pandas as pd

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

#Crea una columna con los nombres en minuscula gracias al import
df['Lowercase Name'] = df.Name.apply(lower)
print(df)

#------------------------------------------------------------------------------
#Imprime la primera y ultima letra del string
mylambda = lambda x: x[0] + x[-1]
print(mylambda('This is a string'))

#condicional con lambda
mylambda = lambda x: 'Welcome to BattleCity!' if x >= 13 else 'You must be over 13'
print(mylambda(16))
print(mylambda(11))
#------------------------------------------------------------------------------
df = pd.read_csv('employees.csv')
#separa el string escrito en la columna 'name' y crea 'last_name' con lo que separo
df['last_name'] = df.name.apply(
  lambda x : x.split()[-1]
)
print(df)

#Lambda que crea total_earned con las condiciones para calcular el salario con horas extra
total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
  #condional de horas extra
	if row.hours_worked > 40 \
  #los que no hicieron horas extra
  else row.hourly_wage * row.hours_worked

df['total_earned'] = df.apply(total_earned, axis = 1)

#esta funcion hacce lo mismo
def total_earned(row):
   if row['hours_worked'] <= 40:
       return row['hours_worked'] * \
           row['hourly_wage']
    else:
        return (40 * row['hourly_wage'])\
            + (row['hours_worked'] - 40) * \
            (row['hourly_wage'] * 1.50)

print(df)
#------------------------------------------------------------------------------
df = pd.read_csv('imdb.csv')
#cambia los strings de la primera fila de titulos
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df)
#modifica el string del titulo elegido
df = df.rename(columns={'Title': 'movie_title'})
print(df)


orders = pd.read_csv('shoefly.csv')
print(orders.head())

#Add a new column called shoe_source, which is vegan if the materials is not leather and animal otherwise.
orders['shoe_source'] = orders.shoe_material.apply(
  lambda x: 'animal' if x == 'leather' else 'vegan')

# Using the columns last_name and gender create a column called salutation which contains Dear Mr. <last_name> for men and Dear Ms. <last_name> for women.
orders['salutation'] = orders.apply(lambda row: 'Dear Mr. ' + row['last_name'] 
  if row['gender'] == 'male' 
  else 'Dear Ms. ' + row['last_name'], axis=1)