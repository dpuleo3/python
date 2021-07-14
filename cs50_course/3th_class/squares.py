# Use imported function from function
from functions import square

for i in range(4):
     print(f"The square of {i} is {square(i)}")
     
# Another way to import functions
import functions

for i in range(4):
     print(f"The square of {i} is {functions.square(i)}")