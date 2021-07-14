people = [ 
  {"name": "Daniel", "team": "Man U"},
  {"name": "German", "team": "Liverpool"},
  {"name", "Pichu", "team": "Madrid"}
]

# Sort dictionary by name in alphabetical order
def f(person):
  return person["name"]
people.sort(key = f)
print(people)

# Sort dictionary by name using lambda
people.sort(key=lambda person: person["name"])
print(people)


# Sort dictionary by team in alphabetical order
def f(person):
  return person["team"]
people.sort(key = f)
print(people)