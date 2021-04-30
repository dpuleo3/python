import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())                       
print(checkout.head())                       
print(purchase.head())

visits_cart = pd.merge(
  visits, cart, how = 'left'
)
print(visits_cart)

visits_cart_rows = len(visits_cart)
cart_null_times = len(visits_cart[visits_cart.cart_time.isnull()])

percent_of_users_visits = float(cart_null_times) / visits_cart_rows
print(percent_of_users_visits)


cart_checkout = pd.merge(
  cart, checkout, how = 'left'
)
print(cart_checkout)

cart_checkout_rows = len(cart_checkout)
checkout_null_times = len(cart_checkout[cart_checkout.checkout_time.isnull()])

percent_of_users_checkouts = float(checkout_null_times) / cart_checkout_rows
print(percent_of_users_checkouts)


cheackout_purchase = pd.merge(
  checkout, purchase, how='left'
)
print(cheackout_purchase)

checkout_purchase_rows = len(cheackout_purchase)
purchase_null_times = len(cheackout_purchase[cheackout_purchase.purchase_time.isnull()])

percentage_checkout_no_purchase = float(purchase_null_times) / checkout_purchase_rows
print(percentage_checkout_no_purchase)


all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head())

#  average time from initial visit to final purchase. 
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.time_to_purchase)

#  average time to purchase
print(all_data.time_to_purchase.mean())