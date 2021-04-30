class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  #string representation
  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + ' to ' + str(self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item]
    return bill


# First Menu
brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu('Brunch', brunch, 11, 16)
print(brunch_menu)
#Testing calculate_bill
print(brunch_menu.calculate_bill(['burger', 'orange juice']))

#Second Menu
early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu('Early Bird', early_bird, 15, 18)
print(early_bird_menu)
#Testing calculate_bill
print(early_bird_menu.calculate_bill(['coffee', 'pizza with quattro formaggi']))

#Third Menu
dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu('Dinner', dinner, 17, 22)
print(dinner_menu)

#Forth Menu (Kids)
kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu("KIDS", kids, 11, 19)
print(kids_menu)


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  #string representation
  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))



class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
print(basta)


arepas = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a'Arepa", arepas, 6, 22)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
arepa = Business("Take a' Arepa", arepas_place)
print(arepa)


