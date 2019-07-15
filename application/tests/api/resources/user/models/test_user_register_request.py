import unittest
from application.api.resources.user.models.user_register_request import UserRegisterRequest

class TestUserRegisterRequest(unittest.TestCase):
    def setUp(self):
        self.valid_mock = {
            'username': 'test',
            'password': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com'
        }

        self.missing_username_mock = self.valid_mock.copy().pop('username', None)
        self.missing_password_mock = self.valid_mock.copy().pop('password', None)
        self.missing_first_name_mock = self.valid_mock.copy().pop('first_name', None)
        self.missing_last_name_mock = self.valid_mock.copy().pop('last_name', None)
        self.missing_email_mock = self.valid_mock.copy().pop('password', None)

    def tearDown(self):
        pass

    def test_validate_valid_request(self):
        request = UserRegisterRequest(self.valid_mock)

        request.validate()

        self.assertEqual(request.username, self.valid_mock['username'])
        self.assertEqual(request.password, self.valid_mock['password'])
        self.assertEqual(request.first_name, self.valid_mock['first_name'])
        self.assertEqual(request.last_name, self.valid_mock['last_name'])
        self.assertEqual(request.email, self.valid_mock['email'])

    def test_validate_missing_username_request(self):
        request = UserRegisterRequest(self.missing_username_mock)

        self.assertRaises(Exception, request.validate)

    def test_validate__missing_password_request(self):
        request = UserRegisterRequest(self.missing_password_mock)

        self.assertRaises(Exception, request.validate)

    def test_validate_missing_first_name_request(self):
        request = UserRegisterRequest(self.missing_first_name_mock)

        self.assertRaises(Exception, request.validate)

    def test_validate__missing_last_name_request(self):
        request = UserRegisterRequest(self.missing_last_name_mock)

        self.assertRaises(Exception, request.validate)

    def test_validate__missing_email_request(self):
        request = UserRegisterRequest(self.missing_email_mock)

        self.assertRaises(Exception, request.validate)