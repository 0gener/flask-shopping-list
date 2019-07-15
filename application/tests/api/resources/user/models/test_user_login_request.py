import unittest
from application.api.resources.user.models.user_login_request import UserLoginRequest

class TestUserLoginRequest(unittest.TestCase):
    def setUp(self):
        self.valid_mock = {
            'username': 'test',
            'password': 'test'
        }

        self.missing_username_mock = {
            'password': 'test'
        }

        self.missing_password_mock = {
            'username': 'test'
        }

    def tearDown(self):
        pass

    def test_valid_user_login_request(self):
        request = UserLoginRequest(self.valid_mock)

        request.validate()

        self.assertEqual(request.username, self.valid_mock['username'])
        self.assertEqual(request.password, self.valid_mock['password'])

    def test_missing_username_user_login_request(self):
        request = UserLoginRequest(self.missing_username_mock)

        self.assertRaises(Exception, request.validate)

    def test_missing_password_user_login_request(self):
        request = UserLoginRequest(self.missing_password_mock)

        self.assertRaises(Exception, request.validate)