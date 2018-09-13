import os
import unittest
import coverage

from flask_script import Manager, Shell, prompt_bool
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

@manager.command
def drop_database():
    """Drop all database tables."""
    if prompt_bool("Are you sure you want to delete your database data"):
        try:
            db.drop_all()
            print("Dropped all tables successfully.")
        except Exception:
            print("Failed, make sure your database server is running!")

if __name__ == "__main__":
    manager.run()