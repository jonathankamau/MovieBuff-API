import json
from tests.base_test import BaseTestCase


class TestLogin(BaseTestCase):
    """Tests for the user endpoint."""

    def setUp(self):
        BaseTestCase.setUp(self)
    
    def test_user_can_login(self):
        """ tests if the API can login a user """
        
        self.assertEqual(self.login.status_code, 200)

        self.assertEqual('You have logged in successfully',
                         self.login_response['message'],
                         msg="User could not log in!"
                         )
