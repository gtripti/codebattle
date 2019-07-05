import pandas

import sqlite3
#cnx = sqlite3.connect(':memory:')
conn = sqlite3.connect("db.sqlite3")

df = pandas.read_csv("C:/Users/r0a01fk/Documents/codebattle/grocery/data/recipes.csv",usecols=['title','ingredients'],encoding="ISO-8859-1")
print(df.head())
df.to_sql('recipe', conn, if_exists='append', index=False)

conn.close()