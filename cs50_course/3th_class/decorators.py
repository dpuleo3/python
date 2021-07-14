# Modifies a function adding more methods
# is a functions that takes a function as input and returns a modified version of that function as output

def announce(f): # Decorater
  def wrapper():
    print("About tu run...") 
    f()
    print("Done running")
  return wrapper

@announce # Decorater
def hello():
  print("I am running!")

hello()
  