"""Database file."""

from flask_mongoalchemy import BaseQuery, MongoAlchemy

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
