import unittest
from application.api.resources.item.models.create_item_request import CreateItemRequest

class TestCreateGroupRequest(unittest.TestCase):
    def setUp(self):
        self.valid_mock = {
            'name': 'test'
        }

        self.missing_name_mock = self.valid_mock.copy().pop('name', None)

    def tearDown(self):
        pass

    def test_validate_valid_request(self):
        request = CreateItemRequest(self.valid_mock)

        request.validate()

        self.assertEqual(request.name, self.valid_mock['name'])

    def test_validate_missing_name(self):
        request = CreateItemRequest(self.missing_name_mock)

        self.assertRaises(Exception, request.validate)