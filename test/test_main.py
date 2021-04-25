import unittest
from main import *


class TestMain(unittest.TestCase):
    def test_message(self):
        with app.test_request_context('/word'):
            self.assertEqual(flask.request.path, '/word')
