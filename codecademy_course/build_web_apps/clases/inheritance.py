# Overriding Methods
# all we have to do to override a method definition is to offer a new definition for the method in our subclass.
class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

class Admin(User):
#Override User‘s .edit_message() method in Admin so that an Admin can edit any messages.
  def edit_message(self,message,new_text):
    message.text = new_text


# Super()
# super() gives us a proxy object. With this proxy object, we can invoke the method of an object’s parent class 
class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

# The difference with your special potato salad is… you add raisins to it!
# You always use the full package of raisins for every potato salad you make, and each package has 40 raisins in it.
class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40


# Interfaces
# When two classes have the same method names and attributes, we say they implement the same interface.
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    rate_1 = .001
    return self.price_of_insured_item * rate_1

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    rate_2 = .00005
    return self.price_of_insured_item * rate_2


# Polymorphism



# Dunder Methods
# __init__, our constructor, which sets a list of users to the instance variable self.user_list and sets the group’s permissions 
# when we create a new UserGroup.
# __iter__, the iterator, we use the iter() function to turn the list self.user_list into an iterator so we can use
#for user in user_group syntax. For more information on iterators, review Python’s documentation of Iterator Types.
# __len__, the length method, so when we call len(user_group) it will return the length of the underlying self.user_list list.
# __contains__, the check for containment, allows us to use user in user_group syntax to check if a User exists in the user_list we have.
class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
    
  def __len__(self):
    return len(self.lawyers)
  
  def __contains__(self, lawyer):
    return lawyer in self.lawyers
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])