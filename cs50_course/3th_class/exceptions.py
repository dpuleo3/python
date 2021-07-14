import sys # Module to modify error message

try: 
  x = int(input("x= "))
  y = int(input("y= "))
except ValueError:
  print("no puedes dividir entre palabras gafo")
  sys.exit(1) # algo salio mal

try:
  result = x / y
except ZeroDivisionError: # si algo sale mal entonces...
  print("No puedes dividir entre 0 gafo")
  sys.exit(1) # algo salio mal

print(f"{x} / {y} = {result}")

