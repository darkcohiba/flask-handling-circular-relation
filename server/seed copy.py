#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import User, Farmer, Product, Review, Cart, CartItem, Order
from config import db
fake = Faker()

def create_users():
    users = []
    for _ in range(15):
        u = User(
            username = fake.name(),
            email = fake.email(),
            password_hash = "123abc", 
        )
        users.append(u)
    return users

def create_farmer():
    farmers = []
    for _ in range(15):
        f = Farmer(
            name = fake.name(),
            address = fake.address(), 
        )
        farmers.append(f)
    return farmers

CATEGORY = ['Beef', 'Dairy', 'Plant-based']
def create_products(farmers):
    products = []
    for _ in range(15):
        p = Product(
            name = fake.name(),
            price = randint(1, 15),
            category = rc(CATEGORY), 
        )
        products.append(p)
    return products


def create_reviews(users, product):
    reviews = []
    for _ in range(15):
        r = Review(
            content = fake.paragraph(),
            rating = randint(1,10),
            user_id = rc(users).id,
            product_id = rc(product).id, 
        )
        reviews.append(r)
    return reviews

def create_cart(users):
    carts = []
    for _ in range(15):
        r = Cart(
            cart_total = randint(1,200),
            user_id = rc(users).id,
        )
        carts.append(r)
    return carts

def create_cart_item(carts, product):
    cart_item = []
    for _ in range(15):
        r = CartItem(
            product_quantity = randint(1,4),
            cart_id = rc(carts).id,
            product_id = rc(product).id, 
        )
        cart_item.append(r)
    return cart_item


def create_order(carts, user):
    orders = []
    for _ in range(15):
        r = Order(
            exp_delivery_date = fake.date(),
            delivery_address = fake.address(),
            cart_id = rc(carts).id,
            user_id = rc(user).id, 
        )
        orders.append(r)
    return orders




if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        # delete users
        print("delete data")
        db.session.query(User).delete()
        db.session.query(Farmer).delete()
        db.session.query(Product).delete()
        db.session.query(Review).delete()
        db.session.query(Cart).delete()
        db.session.query(CartItem).delete()
        db.session.query(Order).delete()
        db.session.commit()

        print("creating users")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        farmers = create_farmer()
        db.session.add_all(farmers)
        db.session.commit()

        products = create_products(farmers)
        db.session.add_all(products)
        db.session.commit()

        reviews = create_reviews(users, products)
        db.session.add_all(reviews)
        db.session.commit()

        carts = create_cart(users)
        db.session.add_all(carts)
        db.session.commit()

        cartsItems = create_cart_item(carts)
        db.session.add_all(cartsItems)
        db.session.commit()

        orders = create_order(carts, users)
        db.session.add_all(orders)
        db.session.commit()
        