import json
from datetime import datetime
from unittest import TestCase
from app import create_app
from api.utils import User, FavouriteMovies


class BaseTestCase(TestCase):
    """Contains utilities required in testing."""

    def setUp(self):
        """Setup method to configure test environment."""

        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.remove_all_users()
        self.remove_all_movies()
        self.token = None

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
        self.login_response = json.loads(self.login.get_data(as_text=True))

        self.token = self.login_response['token']
        self.user_id = User.query.get_username('kamjon').first().user_id

        self.header = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

        self.new_movie = FavouriteMovies(
                        user_id=self.user_id,
                        movie_id=789,
                        movie_title='Titanic',
                        popularity=91.27,
                        release_date=datetime.strptime(
                            '2002-07-03', '%Y-%m-%d'),
                        overview='Ship sinking'
        )
        self.new_movie.save()
    
        self.get_favourite_movies = self.client().get('/api/movie/favourites',
                                                      headers=self.header
                                                      )
        self.delete_movie = self.client().delete('/api/movie/delete?id=789',
                                           headers=self.header
                                           )

    def remove_all_users(self):
        users = User.query.all()

        for user in users:
            user.remove()
    
    def remove_all_movies(self):
        movies = FavouriteMovies.query.all()

        for movie in movies:
            movie.remove()
