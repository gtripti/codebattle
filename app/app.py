from flask import Flask, jsonify, request, render_template
from sqldb import sql_query,sql_edit_insert,sql_delete,sql_query2
from utils import get_products_incart, makecorpus, suggest_recipes,suggest_ingred
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#set orderid and userid at login
userId=1
orderId=10000001

@app.route("/")
def hello_world():
    q="INSERT INTO grocery_orders (order_id,user_id) VALUES (?,?)"
    val=(orderId,userId)
    sql_edit_insert(q,val)
    return render_template("index.html")

'''
    This function gets all the queries and returns them as a json object.
'''
@app.route("/productlist",methods=['GET','OPTIONS'])
def get_products():
    if (request.method == 'OPTIONS'):
        return("Allowed for CORS policy", 200)

    if request.method == 'GET':
        data = sql_query("select * from grocery_products")
        response = {}
        for row in data:
            key = row['product_id']
            val = row['product_name']
            response[key] = val
        print([key for key in response])
        response=[{'id':key, 'name':response[key]} for key in response]
        #print(response)
        return jsonify(response), 201
    else:
        return jsonify({}), 405

@app.route("/addtocart",methods=['POST','OPTIONS'])
def add_to_cart():
    if (request.method == 'OPTIONS'):
        return("Allowed for CORS policy", 200)

    if request.method == 'POST':
        try:
            product_id = request.json['id']
        except KeyError:
            return jsonify({}),401
        print("before")
        q="INSERT INTO grocery_productorders (order_id,product_id) VALUES (?,?)"
        val=(orderId,product_id)
        sql_edit_insert(q,val)
        print("added")
        q="select * from grocery_productorders where order_id=?"
        val=(orderId,)
        data=sql_query2(q,val)
        print([row['product_id'] for row in data])
        return jsonify({}),201
    else:	
        return jsonify({}),405

@app.route("/getrecipes",methods=['GET','OPTIONS'])
def get_recipes():
    if (request.method == 'OPTIONS'):
        return("Allowed for CORS policy", 200)

    if request.method =='GET':
        incart=get_products_incart(orderId)
        incart=makecorpus(incart)
        #print(incart)
        #here, call get_recipes by sending incart
        recipes=suggest_recipes(incart)
        #print(recipes)
        
        response=[i for i in recipes]



        return jsonify(response),201
    else:
        return jsonify({}),405

@app.route("/getothers",methods=['GET','OPTIONS'])
def get_other_ingredients():
    if (request.method == 'OPTIONS'):
        return("Allowed for CORS policy", 200)
    if request.method == 'GET':
        incart=get_products_incart(orderId)
        incart_corpus=makecorpus(incart)
        recipes=suggest_recipes(incart_corpus)
        #print(incart,recipes)
        
        response=suggest_ingred(recipes,incart)

        #response=[]

        return jsonify(response),201
    else:
        return jsonify({}),405

@app.route("/cartitems",methods=['GET','OPTIONS'])
def cart_items():
    if (request.method == 'OPTIONS'):
        return("Allowed for CORS policy", 200)
    
    if request.method == 'GET':
        response=get_products_incart(orderId)

        return jsonify(response),201
    else:
        return jsonify({}),405

@app.route("/clearcart",methods=['DELETE','OPTIONS'])
def clear_cart():
    if (request.method == 'OPTIONS'):
        return("Allowed for CORS policy", 200)
    if request.method=='DELETE':
        q="delete from grocery_productorders where order_id=?"
        val=(orderId,)
        sql_delete(q,val)
        q="delete from grocery_productorders where order_id=?"
        val=(orderId,)
        print(sql_query2(q,val))

        
        return jsonify({}),201
    else:	
        return jsonify({}),405