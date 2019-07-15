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

        self.missing_username_mock = {
            'password': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com'
        }

        self.missing_password_mock = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com'
        }

        self.missing_first_name_mock = {
            'username': 'test',
            'password': 'test',
            'last_name': 'test',
            'email': 'test@test.com'
        }

        self.missing_last_name_mock = {
            'username': 'test',
            'password': 'test',
            'first_name': 'test',
            'email': 'test@test.com'
        }

        self.missing_email_mock = {
            'username': 'test',
            'password': 'test',
            'first_name': 'test',
            'last_name': 'test'
        }

    def tearDown(self):
        pass

    def test_valid_user_login_request(self):
        request = UserRegisterRequest(self.valid_mock)

        request.validate()

        self.assertEqual(request.username, self.valid_mock['username'])
        self.assertEqual(request.password, self.valid_mock['password'])
        self.assertEqual(request.first_name, self.valid_mock['first_name'])
        self.assertEqual(request.last_name, self.valid_mock['last_name'])
        self.assertEqual(request.email, self.valid_mock['email'])

    def test_missing_username_user_register_request(self):
        request = UserRegisterRequest(self.missing_username_mock)

        self.assertRaises(Exception, request.validate)

    def test_missing_password_user_register_request(self):
        request = UserRegisterRequest(self.missing_password_mock)

        self.assertRaises(Exception, request.validate)

    def test_missing_first_name_user_register_request(self):
        request = UserRegisterRequest(self.missing_first_name_mock)

        self.assertRaises(Exception, request.validate)

    def test_missing_last_name_user_register_request(self):
        request = UserRegisterRequest(self.missing_last_name_mock)

        self.assertRaises(Exception, request.validate)

    def test_missing_email_user_register_request(self):
        request = UserRegisterRequest(self.missing_email_mock)

        self.assertRaises(Exception, request.validate)