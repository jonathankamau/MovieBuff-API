"""Database file."""

import os
from flask_mongoalchemy import BaseQuery, MongoAlchemy
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

db = MongoAlchemy()


class MyQueries(BaseQuery):

    def get_username(self, user_name):
        return self.filter(self.type.username == user_name)


class User(db.Document):
    query_class = MyQueries

    first_name = db.StringField()
    last_name = db.StringField()
    username = db.StringField()
    password = db.StringField()

    def generate_token(self, expiration=6000):
        serial = Serializer(os.getenv('SECRET'), expires_in=expiration)
        return "Bearer "+serial.dumps({'id': self.password}).decode('utf-8')   
