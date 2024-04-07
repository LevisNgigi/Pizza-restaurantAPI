from datetime import datetime
from flask import Flask
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def seed_data():
    with app.app_context():
        # Restaurants
        restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
        restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')
        restaurant3 = Restaurant(name='Suzys', address='Long Island')
        restaurant4 = Restaurant(name='Lucy Lee', address='56 Avenue')
        restaurant5 = Restaurant(name='Pasta House', address='32 Broadway St')

        db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5])
        db.session.commit()

        # Pizzas
        pizza1 = Pizza(name='Margherita', ingredients='Tomato, mozzarella, basil')
        pizza2 = Pizza(name='Pepperoni', ingredients='Pepperoni, cheese, tomato sauce')
        pizza3 = Pizza(name='Hawaiian', ingredients='pizza sauce, cheese, cooked ham, pineapple')
        pizza4 = Pizza(name='Cheese', ingredients='pizza dough, tomato sauce, cheese')
        pizza5 = Pizza(name='Veggie', ingredients='cherry tomatoes, artichoke, bell pepper, olives, red onion')

        db.session.add_all([pizza1, pizza2, pizza3, pizza4, pizza5])
        db.session.commit()

        # Restaurant Pizzas
        restaurant_pizza1 = RestaurantPizza(pizza=pizza1, restaurant=restaurant1, price=15)
        restaurant_pizza2 = RestaurantPizza(pizza=pizza2, restaurant=restaurant2, price=20)
        restaurant_pizza3 = RestaurantPizza(pizza=pizza5, restaurant=restaurant3, price=20)
        restaurant_pizza4 = RestaurantPizza(pizza=pizza3, restaurant=restaurant4, price=20)
        restaurant_pizza5 = RestaurantPizza(pizza=pizza4, restaurant=restaurant5, price=20)

        db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3, restaurant_pizza4, restaurant_pizza5])
        db.session.commit()

if __name__ == "__main__":
    seed_data()
