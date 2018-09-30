import json
from tests.base_test import BaseTestCase


class TestDeleteMovie(BaseTestCase):
    """Test delete movie endpoint."""
    
    def setUp(self):
        BaseTestCase.setUp(self)
    
    def test_movie_deleted_successfully(self):

        response_message = json.loads(
                                      self.delete_movie.get_data(
                                                                as_text=True
                                                                )
                                      )

        self.assertEqual(self.delete_movie.status_code, 200)
 
        self.assertEqual('Movie deleted',
                         response_message['response'],
                         msg="Movie has not been deleted!"
                         )
