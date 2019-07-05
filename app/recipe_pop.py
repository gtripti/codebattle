import json
import sqlite3
import csv
import re
with open('C:/Users/r0a01fk/Documents/codebattle/grocery/data/recipes_ar.json') as json_file:  
    data = json.load(json_file)

    # conn = sqlite3.connect("db.sqlite3")

    # create_table_sql = """ CREATE TABLE IF NOT EXISTS recipe (name text NOT NULL,ingredients text); """

    # c = conn.cursor()
    # c.execute(create_table_sql)

    f = csv.writer(open('C:/Users/r0a01fk/Documents/codebattle/grocery/data/recipes.csv', "w"))

    # Write CSV Header, If you dont need that, remove this line
    f.writerow(['title','ingredients'])
    query = "insert into recipe values (?,?)"
    columns = ['name','ingredients']
    i=0
    for row in data:
        corpus=[]
        # print(data[row]['title'],data[row]['ingredients'])

        if 'ingredients' in data[row]:
            for item in data[row]['ingredients']:
                item=item.split()
                corpus.extend(item)
            corpus=list(set(corpus))
            corpus=" ".join(corpus)
            corpus=re.split(r"[^a-zA-Z]", corpus)
            corpus=[i.lower() for i in corpus if i]  
            corpus=" ".join(corpus)
            print(corpus)
            f.writerow([data[row]['title'],corpus])
            # keys=(data[row]['title'],corpus)
            # c = conn.cursor()
            # c.execute(query, keys)
            # c.close()