class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)

  def get_average(self):
    total=0
    for grade in self.grades:
      **total = total + grade.score**
    average = total/len(self.grades)
    return average

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

  def is_passing(self):
    if self.score > self.minimum_passing:
      return True

roger = Student("Roger van der Weyden",10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
average = pieter.get_average()
print(average)