#Double
nums = [4, 8, 15, 16, 23, 42]
double_nums = [x * 2 for x in nums]

#Squares
nums = range(11)
squares = [y**2 for y in nums]

#Add Ten
nums = [4, 8, 15, 16, 23, 42]
add_ten = [z + 10 for z in nums]

#Devide by 2
nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [w / 2 for w in nums]

#Parity
nums = [4, 8, 15, 16, 23, 42]
parity = [i % 2 for i in nums]

#Add Hello
names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, " + f for f in names]

#First Character
names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [n[0] for n in names]

#Size
names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(t) for t in names]

#Opposite
booleans = [True, False, True]
opposite = [not boo for boo in booleans]

#Same String
names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name == "Jerry" for name in names]

#Greater Than Two
nums = [5, -10, 40, 20, 0]
greater_than_two = [i > 2 for i in nums]

#Product
nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [i * j for (i, j) in nested_lists]

#Greater Than
nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [i > j for (i, j) in nested_lists] 

#Fisrt Only
nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [i for (i, j) in nested_lists]

#Add With Zip
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
added = zip(a, b) 
sums = [i + j for (i, j) in added]

#Devide With Zip
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
divided = zip(a, b)
quotients = [j / i for (i, j) in divided]

#Capitals
capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
locations = [capital + ", " + country for (capital, country) in zip(capitals, countries)]

#Ages
names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]
users = ["Name: " + name + ", Age: " + str(age) for (name, age) in zip(names, ages)]

#Greater Than With Zip
a = [30, 42, 10]
b = [15, 16, 17]
greater_than = [i > j for (i, j) in zip(a, b)]