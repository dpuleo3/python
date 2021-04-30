import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

views = ad_clicks.groupby('utm_source').user_id.count().reset_index()

#muestra True si los valores de la columna 'ad_click_timestamp' son not-null 
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.isnull()

#crea una columna 'percent_clicked' donde calcula el porcentaje de is_click sobre utm_source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]) * 100
print(clicks_pivot)

#agrupa los valores de 'experimental_group'
aprox = ad_clicks.groupby('experimental_group').count().reset_index()
aprox_pivot = aprox.pivot(index='experimental_group',
          columns='is_click',
          values='user_id').reset_index()


a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

day_clicks = ad_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
pivot_day_clicks = day_clicks.pivot(index = 'day', columns = 'is_click').reset_index()
pivot_day_clicks['percent_day_clicks']