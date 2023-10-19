#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Reviews, Movies


class UserResource(Resource):

    def get(self):
        users_list = User.query.all()
        return [user.to_dict(only=('username','email')) for user in users_list], 200

    # def post(self):
    #     data = request.get_json()

    #     if not data:
    #         return {"message": "No input data provided"}, 400
    #     try:
    #         new_user = User(name=data["name"], age=data['age'])
    #     except ValueError as e:
    #         return {"message": f"Error creating user: {e}"}, 400

    #     db.session.add(new_user)
    #     db.session.commit()

    #     return new_user.to_dict(), 201


api.add_resource(UserResource, '/user')


class UsersByIdResource(Resource):

    def get_user(self, user_id):
        if user := User.query.get(user_id):
            return user, None, None
        else:
            return None, {"message": "user not found"}, 404
    
    def get(self, user_id):
        user, err, status = self.get_user(user_id)
        return (err, status) if err else (user.to_dict(), 200)
        # if user := user.query.get(user_id):
        #     return user.to_dict(), 200
        # else:
        #     return {"message": "user not found"}, 404

    # def patch(self, user_id):
    #     user = User.query.get(user_id)
    #     if not user:
    #         return {"message": "user not found"}, 404

    #     data = request.get_json()
    #     if not data:
    #         return {"message": "No input data provided"}, 400

    #     allowed_fields = {"name", "age"}
    #     try:
    #         for field in data:
    #             if field in allowed_fields:
    #                 setattr(user, field, data[field])
    #             else:
    #                 return {"message": f"Field '{field}' is not allowed to be updated"}, 400
    #     except ValueError as e:
    #         return {"message": f"Error updating field '{field}': {e}"}, 400

    #     db.session.commit()

    #     return user.to_dict(), 202

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "user not found"}, 404

        db.session.delete(user)
        db.session.commit()

        return {}, 204


api.add_resource(UsersByIdResource, '/user/<int:user_id>')


class ReviewsResource(Resource):

    def get(self):
        reviewss_list = Reviews.query.all()
        return [reviews.to_dict() for reviews in reviewss_list], 200

    # def post(self):
    #     data = request.get_json()

    #     if not data:
    #         return {"message": "No input data provided"}, 400
    #     try:
    #         new_reviews = Reviews(name=data["name"], age=data['age'])
    #     except ValueError as e:
    #         return {"message": f"Error creating reviews: {e}"}, 400

    #     db.session.add(new_reviews)
    #     db.session.commit()

    #     return new_reviews.to_dict(), 201


api.add_resource(ReviewsResource, '/reviews')


class ReviewsByIdResource(Resource):

    def get_reviews(self, reviews_id):
        if reviews := Reviews.query.get(reviews_id):
            return reviews, None, None
        else:
            return None, {"message": "reviews not found"}, 404
    
    def get(self, reviews_id):
        reviews, err, status = self.get_reviews(reviews_id)
        return (err, status) if err else (reviews.to_dict(), 200)
        # if reviews := reviews.query.get(reviews_id):
        #     return reviews.to_dict(), 200
        # else:
        #     return {"message": "reviews not found"}, 404

    # def patch(self, reviews_id):
    #     reviews = Reviews.query.get(reviews_id)
    #     if not reviews:
    #         return {"message": "reviews not found"}, 404

    #     data = request.get_json()
    #     if not data:
    #         return {"message": "No input data provided"}, 400

    #     allowed_fields = {"name", "age"}
    #     try:
    #         for field in data:
    #             if field in allowed_fields:
    #                 setattr(reviews, field, data[field])
    #             else:
    #                 return {"message": f"Field '{field}' is not allowed to be updated"}, 400
    #     except ValueError as e:
    #         return {"message": f"Error updating field '{field}': {e}"}, 400

    #     db.session.commit()

    #     return reviews.to_dict(), 202

    def delete(self, reviews_id):
        reviews = Reviews.query.get(reviews_id)
        if not reviews:
            return {"message": "reviews not found"}, 404

        db.session.delete(reviews)
        db.session.commit()

        return {}, 204


api.add_resource(ReviewsByIdResource, '/reviews/<int:reviews_id>')


class MoviesResource(Resource):

    def get(self):
        moviess_list = Movies.query.all()
        return [movies.to_dict() for movies in moviess_list], 200

    # def post(self):
    #     data = request.get_json()

    #     if not data:
    #         return {"message": "No input data provided"}, 400
    #     try:
    #         new_movies = Movies(name=data["name"], age=data['age'])
    #     except ValueError as e:
    #         return {"message": f"Error creating movies: {e}"}, 400

    #     db.session.add(new_movies)
    #     db.session.commit()

    #     return new_movies.to_dict(), 201


api.add_resource(MoviesResource, '/movies')


class MoviessByIdResource(Resource):

    def get_movies(self, movies_id):
        if movies := Movies.query.get(movies_id):
            return movies, None, None
        else:
            return None, {"message": "movies not found"}, 404
    
    def get(self, movies_id):
        movies, err, status = self.get_movies(movies_id)
        return (err, status) if err else (movies.to_dict(), 200)
        # if movies := movies.query.get(movies_id):
        #     return movies.to_dict(), 200
        # else:
        #     return {"message": "movies not found"}, 404

    # def patch(self, movies_id):
    #     movies = Movies.query.get(movies_id)
    #     if not movies:
    #         return {"message": "movies not found"}, 404

    #     data = request.get_json()
    #     if not data:
    #         return {"message": "No input data provided"}, 400

    #     allowed_fields = {"name", "age"}
    #     try:
    #         for field in data:
    #             if field in allowed_fields:
    #                 setattr(movies, field, data[field])
    #             else:
    #                 return {"message": f"Field '{field}' is not allowed to be updated"}, 400
    #     except ValueError as e:
    #         return {"message": f"Error updating field '{field}': {e}"}, 400

    #     db.session.commit()

    #     return movies.to_dict(), 202

    def delete(self, movies_id):
        movies = Movies.query.get(movies_id)
        if not movies:
            return {"message": "movies not found"}, 404

        db.session.delete(movies)
        db.session.commit()

        return {}, 204


api.add_resource(MoviessByIdResource, '/movies/<int:movies_id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)