import os

from flask_script import Manager
from flask_migrate import Migrate
from setup import create_app

movie_app = create_app(environment=os.environ.get('APP_SETTINGS'))
manager = Manager(movie_app)
migrate = Migrate(movie_app)


if __name__ == "__main__":
    manager.run()
