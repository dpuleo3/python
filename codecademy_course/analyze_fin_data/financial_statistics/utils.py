from math import log, sqrt

# Simple Rate of Return
def calculate_simple_return(start_price, end_price, dividend = 0):
  s_return = (end_price - start_price + dividend) / start_price
  return s_return

simple_return = calculate_simple_return(200, 250, 20)
print("The simple rate of return is " + display_as_percentage(simple_return))


# Logarithmic Rate of Return
def calculate_log_return(start_price, end_price):
  return log(end_price / start_price)

log_return = calculate_log_return(200, 250)
print("The log rate of return is " + display_as_percentage(log_return))

## Aggregate Across Time I
daily_return_a = 0.001
monthly_return_b = 0.022

print("The daily rate of return for Investment A is " + display_as_percentage(daily_return_a))
print("The monthly rate of return for Investment B is " + display_as_percentage(monthly_return_b))

def annualize_return(log_return, t):
  r = log_return * t
  return r

annual_return_a = annualize_return(daily_return_a, 252)
print("The annual rate of return for Investment A is " + display_as_percentage(annual_return_a))

annual_return_b = annualize_return(monthly_return_b, 12)
print("The annual rate of return for Investment A is " + display_as_percentage(annual_return_b))

## Aggregate Across Time II
daily_returns = [0.002, -0.002, 0.003, 0.002, -0.001]

def convert_returns(log_returns, t):
  return sum(log_returns) / len(log_returns) * t

annual_return = convert_returns(daily_returns, 252)

print('The annual rate of return is', display_as_percentage(annual_return))

weekly_return = convert_returns(daily_returns, 5)
weekly_return = sum(daily_returns)

print('The weekly rate of return is', display_as_percentage(weekly_return))


# Calculate Variance
def calculate_variance(dataset):
  mean = sum(dataset) / len(dataset)

  numerator = 0

  for data in dataset:
    numerator += (data - mean) ** 2

  return numerator / len(dataset)


# Calculate Standard Deviation
def calculate_stddev(dataset):
  variance = calculate_variance(dataset)
  return sqrt(variance)


# Calculate Correlation Coefficient
def calculate_correlation(set_x, set_y):
  sum_x = sum(set_x)
  sum_y = sum(set_y)

  sum_x2 = sum([x ** 2 for x in set_x])
  sum_y2 = sum([y ** 2 for y in set_y])

  sum_xy = sum([x * y for x, y in zip(set_x, set_y)])

  n = len(set_x)

  numerator = n * sum_xy - sum_x * sum_y
  denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

  return numerator / denominator