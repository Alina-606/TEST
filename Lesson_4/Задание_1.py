import pandas as pd

gr_orders = pd.read_csv('group_orders.csv', sep=',',encoding='utf-8')
orders_city = gr_orders.groupby("city")["order_id"].count().reset_index(name='order_count')
print(orders_city)
