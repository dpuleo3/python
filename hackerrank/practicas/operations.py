# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

a = int(input())
b = int(input())

print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))



# Task
# The provided code stub reads two integers,  and , from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . 
# The second line should contain the result of float division,  / .

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print('{0} \n{1}'.format((a // b), (a / b)))