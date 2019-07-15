import unittest
from application.api.resources.group.models.create_group_request import CreateGroupRequest

class TestCreateGroupRequest(unittest.TestCase):
    def setUp(self):
        self.valid_mock = {
            'name': 'test'
        }

        self.missing_name_mock = self.valid_mock.copy().pop('name', None)

    def tearDown(self):
        pass

    def test_validate_valid_request(self):
        request = CreateGroupRequest(self.valid_mock)

        request.validate()

        self.assertEqual(request.name, self.valid_mock['name'])

    def test_validate_missing_name(self):
        request = CreateGroupRequest(self.missing_name_mock)

        self.assertRaises(Exception, request.validate)