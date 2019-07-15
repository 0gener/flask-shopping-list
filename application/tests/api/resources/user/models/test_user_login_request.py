import unittest
from application.api.resources.user.models.user_login_request import UserLoginRequest

class TestUserLoginRequest(unittest.TestCase):
    def setUp(self):
        self.valid_mock = {
            'username': 'test',
            'password': 'test'
        }

        self.missing_username_mock = self.valid_mock.copy().pop('username', None)
        self.missing_password_mock = self.valid_mock.copy().pop('password', None)

    def tearDown(self):
        pass

    def test_validate_valid_request(self):
        request = UserLoginRequest(self.valid_mock)

        request.validate()

        self.assertEqual(request.username, self.valid_mock['username'])
        self.assertEqual(request.password, self.valid_mock['password'])

    def test_validate_missing_username_request(self):
        request = UserLoginRequest(self.missing_username_mock)

        self.assertRaises(Exception, request.validate)

    def test_validate_missing_password_request(self):
        request = UserLoginRequest(self.missing_password_mock)

        self.assertRaises(Exception, request.validate)