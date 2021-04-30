import pandas as pd

inventory =  pd.read_csv('inventory.csv')
# print(inventory.head(10))

staten_island = inventory.iloc[0:10]
# print(staten_island)

product_description = inventory.product_description
product_request = product_description.iloc[0:10]
# print(product_request)

seed_request = inventory[(inventory.location == 'Brooklyn') &
(inventory.product_type == 'seeds')]
# print(seed_request)

inventory['in_stock'] = inventory.apply(lambda x: True if x.quantity > 0 else False, axis= 1)

inventory['total_value'] = inventory.price * inventory.quantity

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = combine_lambda