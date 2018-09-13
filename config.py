"""App environment configurations."""

import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Development():
    """Model Development enviroment config object."""

    DEBUG = True
    DEVELOPMENT = True


env_configuration = {
    'development': Development
}
