import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from api.utils.models import db

movie_app = create_app(environment=os.environ.get('APP_SETTINGS'))
manager = Manager(movie_app)
migrate = Migrate(movie_app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def drop_database():
    try:
        db.drop_all()
        print('Dropped all databases successfully!')
    except Exception:
        db.session.rollback()
        print('DB drop failed')


if __name__ == "__main__":
    manager.run()
