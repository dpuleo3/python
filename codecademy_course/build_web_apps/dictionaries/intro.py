# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. 
# If the key you are trying to .get() does not exist,  it will return None by default:

# Delete a Key
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}

health_points = 20

#add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. 
#If the key does not exist, add 0 to health_points
health_points += available_items.pop("stamina grains", 0)

#add the value of "power stew" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.
health_points += available_items.get("power stew", 0)
available_items.pop("power stew", 0)

#add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.
health_points += available_items.get("mystic bread", 0)
available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)


# Get All Keys
# .keys() method that returns a dict_keys object. A dict_keys object is a view object, 
# which provides a look at the current state of the dicitonary, without the user being able to modify anything.
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)


# Get All Values

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for num in num_exercises.values():
  total_exercises += num

print(total_exercises)


# Get All Items

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for job, num in pct_women_in_occupation.items():
  print("Women make up " + str(num) + " percent of " + job + "s")


# Review
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 
6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 
12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 
19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your "+ key +" is the "+ value +" card.")


# SUMA LOS VALORES DE UN DICCIONARIO
def sum_values(my_dictionary):
  suma = 0
  for num in my_dictionary.values():
    suma += num 
  return suma

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# SUMA LOS NUMEROS PARES DE UN DICCIONARIO
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      total += my_dictionary[key]
  return total

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# SUMA 10 A CADA VALOR
def add_ten(my_dictionary):
  suma = 0
  for i in my_dictionary.keys():
    my_dictionary[i] += 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Largest Value
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# Word Length Dict
def word_length_dictionary(words):
  w_len = {}
  for w in words:
    w_len[w] = len(w)
  return w_len

print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


# Frequency Count
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
    	freqs[word] = 0
    freqs[word] += 1
  return freqs

print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}


# Unique Values
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value in seen_values:
      continue
    else:
      seen_values.append(value)
  return len(seen_values)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


# Count First Letter
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}