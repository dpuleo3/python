
class Point():
    # is a method that is automaticly called every time a Point is created 
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
        
p = Point(4, 19)
print(p.x) #prints 4
print(p.y) #prints 19

# ---------------------------------------------------------------------

class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passenger = []

  def add_passenger(self, name):
    if not self.open_seats(): # if there aren't open seats return False
      return False
    self.passenger.append(name) # puts a name in the list passenger
    return True

  def open_seats(self):
    return self.capacity - len(self.passenger) # tells the number of seats available

flight = Flight(3)

people = ["Daniel", "German", "Valeria", "Luba"]
for person in people:
  if flight.add_passenger(person):
    print(f"Added {person} to flight")
  else:
    print(f"No available seats for {person}")