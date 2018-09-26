import json
from tests.base_test import BaseTestCase

class TestRegistration(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)
    
    def test_can_register_user(self):
        """ tests if the API can register a user """
        
        self.assertEqual(self.register.status_code, 201)

        response_message = json.loads(self.register.get_data(as_text=True))

        self.assertEqual('user created successfully!',
                         response_message['response'],
                         msg="Not registered!"
                        )
