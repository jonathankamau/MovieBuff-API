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
        self.remove_all_users()
        self.remove_all_movies()

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
        self.login_data = {
            'username': 'kamjon',
            'password': 'kamjon123'
        }
        self.login = self.client().post('/api/user/login',
                                        data=json.dumps(self.login_data),
                                        content_type='application/json'
                                        )

    def remove_all_users(self):
        users = User.query.all()

        for user in users:
            user.remove()
    
    def remove_all_movies(self):
        movies = FavouriteMovies.query.all()

        for movie in movies:
            movie.remove()
