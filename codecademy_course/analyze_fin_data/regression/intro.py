#importing matplotlib
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 6
#intercept:
b = 30
#regression formula
# y = mb + b 
y = [m * x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y, "o")
plt.show()


## Loss
#Number that measures how bad the model’s (in this case, the line’s) prediction was
x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0
#y = 0.5x + 1
m2 = 0.5
b2 = 1
#regression formula
y_predicted1 = [m1 * i + b1 for i in x]
y_predicted2 = [m2 * i + b2 for i in x]

#loss formulas
total_loss1 = 0
for i in range(len(y)):
  total_loss1 += (y[i] - y_predicted1[i]) ** 2
total_loss2 = 0

for i in range(len(y)):
  total_loss2 += (y[i] - y_predicted2[i]) ** 2 

# ------------------------------------------------------------------------------------------------
## Gradient Descent for Intercept / INCLINACION
# N is the number of points we have in our dataset
# m is the current gradient guess
# b is the current intercept guess

def get_gradient_at_b(x, y, m, b):
  diff = 0
  N = len(x)
  for i in range(0, len(x)):
    y_val = y[i]
    x_val = x[i]
    diff += (y_val - ((m * x_val) + b))

  b_gradient = - 2/N * diff
  return b_gradient

## Gradient Descent for Slope / INCLINACION
# N is the number of points you have in your dataset
# m is the current gradient guess
# b is the current intercept guess

def get_gradient_at_m(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += x_val*(y_val - ((m * x_val) + b))
    m_gradient = -2/N * diff
    return m_gradient

# Define your step_gradient function here
def step_gradient(x, y, b_current, m_current):
  b_gradient = get_gradient_at_b(x, y, b_current, m_current)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  b = b_current - (0.01 * b_gradient)
  m = b_current - (0.01 * m_gradient)
  return b, m

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# current intercept guess:
b = 0
# current slope guess:
m = 0

# Call your function here to update b and m
b, m = step_gradient(months, revenue, b, m)
print(b, m)

# ------------------------------------------------------------------------------------------------
##Convergence 
# is when the loss stops changing (or changes very slowly) when parameters are changed.
# the algorithm will converge at the best values for the parameters m and b.

##Learning Rate
# will determine how far down the loss curve we go.
# If the algorithm is taking too long to converge move the learning rate up
def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0
  m = 0
  for i in range(num_iterations):
    b, m = step_gradient(b, m, x, y, learning_rate)
  return [b,m]  

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

b, m = gradient_descent(months, revenue, 0.01, 1000)

y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()