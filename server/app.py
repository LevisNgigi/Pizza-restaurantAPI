#!/usr/bin/env python3

from flask import Flask, make_response,request, jsonify
from flask_migrate import Migrate

from models import db, Restaurant, RestaurantPizza, Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'PIZZAS , RESTAURANTS, RESTAURANT_PIZZAS'

@app.route('/restaurants',methods = ['GET'])
def restaurants():
    restaurants = []
    for restaurant in Restaurant.query.all():
        restaurant_dict = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
        }
        restaurants.append(restaurant_dict)
    return make_response(jsonify(restaurants), 200)

@app.route('/restaurants/<int:id>',methods = ['GET','DELETE'])
def restaurant_by_id(id):
    restaurant = Restaurant.query.filter_by(id=id).first()
    if request.method == "GET":
        if  restaurant:    
            pizzas = []
            for restaurant_pizza in RestaurantPizza.query.filter_by(restaurant_id = id).all():
                for pizza in Pizza.query.filter_by(id = restaurant_pizza.pizza_id):
                    pizza_dict = {
                        "id": pizza.id,
                        "name": pizza.name,
                        "ingredients": pizza.ingredients,
                    }
                pizzas.append(pizza_dict)
            if request.method == 'GET':
                restaurant_dict = {
                    "id": restaurant.id,
                    "name": restaurant.name,
                    "address": restaurant.address,
                    "pizzas": pizzas,
                }
                return make_response(restaurant_dict,200)
        else:
            error_message = {"error": "Restaurant not found"}
            return make_response(error_message, 404)
            

    elif request.method == 'DELETE':
        if restaurant:
            restaurant_pizzas = RestaurantPizza.query.filter_by(restaurant_id = id).all()
            for restaurant_pizza in restaurant_pizzas:
                db.session.delete(restaurant_pizza)
            db.session.delete(restaurant)
            db.session.commit()

            response = {"":""} 

            return make_response(response, 200)
        else:
            error_message = {"error": "Restaurant not found"}
            return make_response(jsonify(error_message), 404)
        
    
@app.route('/pizzas',methods = ['GET'])
def get_pizzas():
    pizzas = []
    for pizza in Pizza.query.all():
        pizza_dict = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients,
        }
        pizzas.append(pizza_dict)
    return make_response(jsonify(pizzas), 200)

@app.route('/restaurant_pizzas',methods = ['POST'])
def add():
    try:
        data = request.get_json()
        new_rp = RestaurantPizza(
            price = data['price'],
            pizza_id = data['pizza_id'],
            restaurant_id = data['restaurant_id'],
        )

        db.session.add(new_rp)
        db.session.commit()

        pizza = Pizza.query.filter_by(id = new_rp.pizza_id).first()
        pizza_dict = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients,
        }
        return make_response(jsonify(pizza_dict),200)

    except ValueError as e:
            error_message = {
                "errors": ["validation errors"]
            }
            return make_response(jsonify(error_message),400)
    
        
if __name__ == '__main__':
    app.run(port=5555)