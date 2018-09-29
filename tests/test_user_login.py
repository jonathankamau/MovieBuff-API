import json
from tests.base_test import BaseTestCase

class TestLogin(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)
    
    def test_user_can_login(self):
        """ tests if the API can login a user """
        
        self.assertEqual(self.login.status_code, 200)

        response_message = json.loads(self.login.get_data(as_text=True))

        self.assertEqual('You have logged in successfully',
                         response_message['message'],
                         msg="User could not log in!"
                         )
