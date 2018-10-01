"""Database file."""
import os
import uuid
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

db = SQLAlchemy()

def uuid_generator():
    return str(uuid)

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.String, primary_key=True, default=uuid_generator)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)

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

        user = User.query.get_user(data['user_id']).first()
        return user


class FavouriteMovies(db.Model):
    __tablename__ = 'favourite_movie'

    user_id = db.Column(db.String, db.ForeignKey('user.user_id'))
    movie_id = db.Column(db.String, primary_key=True)
    movie_title = db.Column(db.String)
    popularity = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    overview = db.Column(db.String)
