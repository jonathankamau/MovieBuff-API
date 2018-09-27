import json
from unittest import TestCase
from app import create_app
from api.utils import User, FavouriteMovies, db


class BaseTestCase(TestCase):
    """Contains utilities required in testing."""

    def setUp(self):
        """Setup method to configure test environment."""

        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.remove_all()

        self.client = self.app.test_client

        self.register_data = {'first_name': 'John',
                              'last_name': 'Kamau',
                              'username': 'kamjon',
                              'password': 'kamjon123'
                              }

        self.register = self.client().post('/api/user/register',
                                           data=json.dumps(self.register_data),
                                           content_type='application/json'
                                           )

    def remove_all(self):
        users = User.query.all()
        movies = FavouriteMovies.query.all()

        for user in users:
            user.remove()
