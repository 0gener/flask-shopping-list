import unittest
from application.api.resources.common.common_request import CommonRequest

class TestCommonRequest(unittest.TestCase):
    def setUp(self):
        self.mock = {
            'username': 'test',
            'password': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com'
        }
        self.field_that_exists = 'username'
        self.field_that_does_not_exist = 'this_field_does_not_exist'

    def tearDown(self):
        pass

    def test_load_field_return_field(self):
        field_value = CommonRequest.load_field(self.mock, self.field_that_exists)

        self.assertEqual(field_value, self.mock[self.field_that_exists])

    def test_load_field_return_none(self):
        field_value = CommonRequest.load_field(self.mock, self.field_that_does_not_exist)

        self.assertEqual(field_value, None)