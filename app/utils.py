from sqldb import sql_query,sql_edit_insert,sql_delete,sql_query2

import re


def get_products_incart(orderId):
    q="select * from grocery_productorders where order_id=?"
    val=(orderId,)
    data=sql_query2(q,val)
    
    incart_id=[row['product_id'] for row in data]
    incart=[]

    for prod in incart_id:
        q="select * from grocery_products where product_id=?"
        val=(prod,)
        data=sql_query2(q,val)
        data=[row['product_name'] for row in data]
        for i in data:
            incart.append(i)

    return incart


def makecorpus(incart):
    corpus=[]
    for i in incart:
        x=i.split()
        x=list(set(x))
        x=" ".join(x)
        x=re.split(r"[^a-zA-Z]", x)
        x=[i.lower() for i in x if i]
        corpus.extend(x)
    return corpus

def suggest_recipes(incart):
    q="select * from recipe"
    data=sql_query(q)
    #print(data)
    possible=dict()
    for row in data:
        ingred=row['ingredients']
        corpus=ingred.split()
        # corpus=re.split(r"[^a-zA-Z]", ingred)
        # corpus=[i for i in corpus if i]
        
        #print(corpus)
        common=list(set(incart).intersection(corpus))
        #print(common)
        if len(common)>7:
            possible[row['title']]={'count':len(common),'corpus':corpus}
    #print(possible)
    
    return possible

def suggest_ingred(recipes,incart):
    q="select * from grocery_products"
    data=sql_query(q)
    #print(data)
    possible=dict()
    for recipe in recipes:
        possible[recipe]=[]
        print(recipe)
    print(possible)
    for row in data:
        prod=row['product_name']
        prod=re.split(r"[^a-zA-Z]", prod)
        prod=[i.lower() for i in prod if i]
        #print(prod)
        for recipe in recipes:
            ingred=recipes[recipe]['corpus']
            common=list(set(ingred).intersection(prod))
            #print(prod,ingred,common)
            if len(common)>2:
                if row['product_name'] not in incart:
                    possible[recipe].append({'name':row['product_name'],'id':row['product_id']})
        #print(possible)
    
    return possible
