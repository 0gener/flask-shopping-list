import unittest
import os

from application import create_app

class TestRootEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config="testing")
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_root_endpoint(self):
        res = self.client.post("/")

        self.assertEqual(res.status_code, 404)