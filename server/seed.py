#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import User, Reviews, Movies
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

def create_movies(users):
    movies = []
    for _ in range(15):
        m = Movies(
            title = fake.name(),
            year = 2023,
            created_by = rc(users).id, 
        )
        movies.append(m)
    return movies

def create_reviews(users, movies):
    reviews = []
    for _ in range(15):
        r = Reviews(
            content = fake.paragraph(),
            user_id = rc(movies).id,
            movie_id = rc(users).id, 
        )
        reviews.append(r)
    return reviews






if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        # delete users
        print("delete data")
        db.session.query(User).delete()
        db.session.query(Reviews).delete()
        db.session.query(Movies).delete()
        db.session.commit()

        print("creating users")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        movies = create_movies(users)
        db.session.add_all(movies)
        db.session.commit()

        reviews = create_reviews(users, movies)
        db.session.add_all(reviews)
        db.session.commit()

        

        
        