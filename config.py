"""App environment configurations."""

import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Development():
    """Model Development enviroment config object."""

    DEBUG = True
    DEVELOPMENT = True
    POSTGRES_DBNAME = os.environ.get('POSTGRES_DBNAME')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')


class Testing():
    """Model Testing environment config object."""

    DEBUG = True
    TESTING = True
    POSTGRES_DBNAME = os.environ.get('POSTGRES_DBNAME_TEST')
    POSTGRES_USER = os.environ.get('POSTGRES_USER_TEST')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD_TEST')


class Staging():
    """Model Development enviroment config object."""

    DEBUG = True
    STAGING = True
    POSTGRES_DBNAME = os.environ.get('POSTGRES_DBNAME')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')


class Production():
    """Model Development enviroment config object."""

    DEBUG = True
    PRODUCTION = True
    POSTGRES_DBNAME = os.environ.get('POSTGRES_DBNAME')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')


env_configuration = {
    'development': Development,
    'testing': Testing,
    'staging': Staging,
    'production': Production

}
