"""Database file."""
import os
import uuid

from sqlalchemy.exc import SQLAlchemyError

from flask_sqlalchemy import SQLAlchemy
from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

db = SQLAlchemy()


def uuid_generator():
    return str(uuid.uuid1())


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.String, primary_key=True, default=uuid_generator)

    def save(self):
        saved = None
        try:
            db.session.add(self)
            db.session.commit()
            saved = True
        except Exception:
            db.session.rollback()
            saved = False
        
        return saved

    def delete(self):
        deleted = None
        try:
            db.session.delete(self)
            db.session.commit()
            deleted = True
        except Exception:
            db.session.rollback()
            deleted = False
        
        return deleted


class UserDetails(Base):
    __tablename__ = 'user_details'

    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)

    favourite_movie = db.relationship('FavouriteMovies')

    def generate_token(self, expiration=6000):
        serial = Serializer(os.getenv('SECRET'), expires_in=expiration)
        return serial.dumps({'id': self.id}).decode('utf-8')

    def verify_auth_token(self, token):
        serial = Serializer(os.getenv('SECRET'))
        try:
            data = serial.loads(token)

        except SignatureExpired:
            return "Expired Token!"  # valid token, but expired
        except BadSignature:
            return "Invalid Token!"  # invalid token

        user = UserDetails.query.filter_by(id=data['id']).first()
        return user


class MovieDetails(Base):
    __tablename__ = 'movie_details'

    movie_id = db.Column(db.Integer, unique=True)
    movie_title = db.Column(db.String)
    vote_average = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    overview = db.Column(db.String)
    category_id = db.Column(
                            db.String,
                            db.ForeignKey('movie_category.id')
                            )

    movie_category_details = db.relationship('MovieCategory')
    favourite_movie = db.relationship('FavouriteMovies', 
                                      backref='movie_detail')


class MovieCategory(Base):
    __tablename__ = 'movie_category'

    category_name = db.Column(db.String)

    movie_details = db.relationship('MovieDetails', backref='movie_category')


class FavouriteMovies(Base):
    __tablename__ = 'favourite_movie'

    user_id = db.Column(db.String, db.ForeignKey('user_details.id'))
    movie_id = db.Column(db.String, db.ForeignKey('movie_details.id'))
    ranking_number = db.Column(db.Integer)

    users = db.relationship('UserDetails')
    movie_details = db.relationship('MovieDetails')
