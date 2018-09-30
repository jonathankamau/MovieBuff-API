import json
from tests.base_test import BaseTestCase


class TestViewFavouritesList(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)

    def test_retrieve_movies_list(self):
        """
        Test that the favourite movies list for a user is
        retrieved successfully.
        """
        response_message = json.loads(
                                      self.get_favourite_movies.get_data(
                                                                as_text=True
                                                                )
                                      )

        self.assertEqual(self.get_favourite_movies.status_code, 200)
 
        self.assertEqual('Your movie list has been retrieved successfully',
                         response_message['message'],
                         msg="Movie list has not been retrieved!"
                         )
