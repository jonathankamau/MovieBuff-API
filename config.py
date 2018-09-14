"""App environment configurations."""

import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Development():
    """Model Development enviroment config object."""

    DEBUG = True
    DEVELOPMENT = True
    MONGOALCHEMY_DATABASE = os.environ.get('MONGO_DBNAME')
    MONGO_URI = os.environ.get('MONGO_URI')


env_configuration = {
    'development': Development
}
