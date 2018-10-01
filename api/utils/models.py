"""Database file."""
import os
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

db = SQLAlchemy()


class User(db.Model):
    user_id = db.Column(db.String, nullable=False)
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
    user_id = db.Column(db.String, nullable=False)
    movie_id = db.Column(db.String)
    movie_title = db.Column(db.String)
    popularity = db.Column(db.String)
    release_date = db.Column(db.String)
    overview = db.Column(db.String)
