"""Database file."""
import os
import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

db = SQLAlchemy()


def uuid_generator():
    return str(uuid.uuid1())


class Base(db.Model):
    __abstract__ = True

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            saved = True
        except SQLAlchemyError:
            db.session.rollback()
            saved = False
        
        return saved

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            deleted = True
        except SQLAlchemyError:
            db.session.rollback()
            deleted = False
        
        return deleted




class User(Base):
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

        user = User.query.filter_by(user_id=data['user_id']).first()
        return user


class FavouriteMovies(Base):
    __tablename__ = 'favourite_movie'

    movie_record_id = db.Column(db.String, primary_key=True, 
                                default=uuid_generator)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'))
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    popularity = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    overview = db.Column(db.String)
