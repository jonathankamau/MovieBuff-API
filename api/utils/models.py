"""Database file."""
import os
from flask_mongoalchemy import BaseQuery, MongoAlchemy
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

db = MongoAlchemy()


class MyQueries(BaseQuery):

    def get_username(self, user_name):
        return self.filter(self.type.username == user_name)

    def get_movie(self, user_id, movie_id):
        return self.filter(self.type.user_id == user_id,
                           self.type.movie_id == movie_id)

    def get_user(self, user_id):
        return self.filter(self.type.user_id == user_id)


class User(db.Document):
    query_class = MyQueries
    user_id = db.StringField()
    firstname = db.StringField()
    lastname = db.StringField()
    username = db.StringField()
    password = db.StringField()

    def generate_token(self, expiration=6000):
        serial = Serializer(os.getenv('SECRET'), expires_in=expiration)
        return serial.dumps({'user_id': self.user_id}).decode('utf-8')

    def verify_auth_token(self, token):
        serial = Serializer(os.getenv('SECRET'))
        try:
            data = serial.loads(token)

        except SignatureExpired:
            return "Expired Token!"  # valid token, but expired
        except BadSignature:
            return "Invalid Token!"  # invalid token
        print(data)
        user = User.query.get_user(data['user_id']).first()
        print(user.lastname)
        return user


class FavouriteMovies(db.Document):
    query_class = MyQueries
    user_id = db.StringField()
    movie_id = db.IntField()
    movie_title = db.StringField()
    popularity = db.FloatField()
    release_date = db.DateTimeField()
    overview = db.StringField()
