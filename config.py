"""App environment configurations."""

import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Development():
    """Model Development enviroment config object."""

    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('LOCAL_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Testing():
    """Model Testing environment config object."""

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Staging():
    """Model Development enviroment config object."""

    DEBUG = True
    STAGING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('STAGING_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Production():
    """Model Development enviroment config object."""

    DEBUG = True
    PRODUCTION = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE')


env_configuration = {
    'development': Development,
    'testing': Testing,
    'staging': Staging,
    'production': Production

}
