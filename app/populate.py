import pandas

import sqlite3
#cnx = sqlite3.connect(':memory:')
conn = sqlite3.connect("db.sqlite3")

df = pandas.read_csv("C:/Users/r0a01fk/Documents/codebattle/grocery/data/orders.csv",usecols=['order_id','user_id'])
print(df.head())
df.to_sql('grocery_orders', conn, if_exists='append', index=False)

df = pandas.read_csv("C:/Users/r0a01fk/Documents/codebattle/grocery/data/products.csv",usecols=['product_id','product_name','department_id'])
print(df.head())
df.to_sql('grocery_products', conn, if_exists='append', index=False)

df = pandas.read_csv("C:/Users/r0a01fk/Documents/codebattle/grocery/data/order_products__prior.csv",usecols=['order_id','product_id'])
print(df.head())
df.to_sql('grocery_productorders', conn, if_exists='append', index=False)

df = pandas.read_csv("C:/Users/r0a01fk/Documents/codebattle/grocery/data/departments.csv",usecols=['department','department_id'])
print(df.head())
df.to_sql('grocery_departments', conn, if_exists='append', index=False)



conn.close()