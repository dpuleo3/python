import pandas as pd
#glob can open multiple files by using regex matching to get the filename
import glob

#goes through any file that starts with 'exams' and has an extension of .csv.
student_files = glob.glob("exams*.csv")

df_list = []

for filename in student_files:
  data = pd.read_csv(filename)
  df_list.append(data)

students = pd.concat(df_list)
print(students)
print(len(students))

# We can use pd.melt() to do this transformation. .melt() takes in a DataFrame, and the columns to unpack:

# pd.melt(frame=df, id_vars='name', value_vars=['Checking','Savings'], value_name="Amount", var_name="Account Type")

# frame: the DataFrame you want to melt
# id_vars: the column(s) of the old DataFrame to preserve
# value_vars: the column(s) of the old DataFrame that you want to turn into variables
# value_name: what to call the column of the new DataFrame that stores the values
# var_name: what to call the column of the new DataFrame that stores the variables
print(students.columns)

students = pd.melt(frame=students, id_vars=['full_name', 'gender_age', 'grade'], value_vars=['fractions','probability'], 
value_name="score", var_name="exam")

print(students.head())
print(students.columns)
print(students.exam.value_counts())

#To check for duplicates, we can use the pandas function .duplicated(), 
# which will return a Series telling us which rows are duplicate rows
duplicates = students.duplicated()
print(duplicates.value_counts())

students = students.drop_duplicates()

duplicates = students.duplicated()
print(duplicates.value_counts())

#separar datos de una columna en dos columnas
print(students.gender_age.head())

students['gender'] = students.gender_age.str[0:1]
students['age'] = students.gender_age.str[1:3]
students = students[['full_name',	'grade',	'exam',	'score',	'gender',	'age']]
print(students.head())

#separar datos de una columna en dos columnas
name_split = students.full_name.str.split(' ')

students['first_name'] = name_split.str[0]
students['last_name'] = students.full_name.str.split(' ').str.get(1)
print(students.head())

#elimina el signo % del string en score
students.score = students['score'].replace('[\%,]', '', regex=True)
#convert column to a numerical type 
students.score = pd.to_numeric(students.score)
#elimina el numero de la columna
students.grade = students.grade.str.split('(\d+)', expand=True)[1]
#rellena los vacios con el valor '0'
students = students.fillna(0)