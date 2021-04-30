# Inner Merge 
import codecademylib
import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

# This will match up all of the customer information to the orders that each customer made.
sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]


men_women = pd.read_csv('men_women_sales.csv')

# Merge all three DataFrames 
all_data = sales.merge(targets).merge(men_women)
print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]
print(results)


# Merge on Specific Columns
# Because the id columns would mean something different in each table, our default merges would be wrong.
# One way that we could address this problem is to use .rename to rename the columns for our merges. 

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

#  merge two DataFrames whose columns don’t match.
orders_products = pd.merge(
    orders,
    products.rename(columns={'id': 'customer_id'}))
print(orders_products)

orders_products = pd.merge(
    orders,
    products,
    #  the “left” table is the one that comes first (orders), and the “right” table is the one that comes second (products)
    left_on = 'product_id',
    right_on = 'id',
    suffixes = ['_orders', '_products']
)
print(orders_products)


# Outer Merge
# An Outer Join would include all rows from both tables, even if they don’t match. 
# Any missing values are filled in with None or nan (which stands for “Not a Number”).

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_outer = pd.merge(
  store_a, store_b, how = 'outer'
)
print(store_a_b_outer)

#  'INNER' merge, which will include only matching rows.

# Left and Right Merge

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

## Left Merge
store_a_b_left = pd.merge(
  store_a, store_b, how = "left"
)
print(store_a_b_left)


# Concatenate DataFrames
# This method only works if all of the columns are the same in all of the DataFrames.
bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

menu = pd.concat([bakery, ice_cream])
print(menu)


# Review
import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

print(visits)
print(checkouts)

v_to_c = pd.merge(
  visits, checkouts
)

# In order to calculate the time between visiting and checking out, define a column of v_to_c called time
v_to_c['time'] = v_to_c.checkout_time - \
                 v_to_c.visit_time
print(v_to_c)

# To get the average time to checkout
print(v_to_c.time.mean())