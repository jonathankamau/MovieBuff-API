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
    MONGOALCHEMY_CONNECTION_STRING = os.environ.get('MONGO_URI')


class Testing():
    """Model Testing environment config object."""

    DEBUG = True
    TESTING = True
    MONGOALCHEMY_DATABASE = os.environ.get('TEST_MONGO_DBNAME')
    MONGOALCHEMY_CONNECTION_STRING = os.environ.get('TEST_MONGO_URI')


class Staging():
    """Model Development enviroment config object."""

    DEBUG = True
    STAGING = True
    MONGOALCHEMY_DATABASE = os.environ.get('MONGO_DBNAME')
    MONGOALCHEMY_CONNECTION_STRING = os.environ.get('MONGO_URI')


class Production():
    """Model Development enviroment config object."""

    DEBUG = True
    PRODUCTION = True
    MONGOALCHEMY_DATABASE = os.environ.get('MONGO_DBNAME')
    MONGOALCHEMY_CONNECTION_STRING = os.environ.get('MONGO_URI')


env_configuration = {
    'development': Development,
    'testing': Testing,
    'staging': Staging,
    'production': Production

}
