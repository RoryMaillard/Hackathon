import unittest
from unittest import mock

from src.main import *


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_1&group_by=categorie_1&limit=100&apikey=apikey':
        return MockResponse({"results": [{"categorie_1":"categorie1"}]}, 200)
    elif args[0] == 'https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_2&group_by=categorie_2&limit=100&apikey=apikey':
        return MockResponse({"results": [{"categorie_2":"categorie2"}]}, 200)
    elif args[0] == 'https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_3&group_by=categorie_3&limit=100&apikey=apikey':
        return MockResponse({"results": [{"categorie_3":"categorie3"}]}, 200)
    elif args[0] == 'https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_4&group_by=categorie_4&limit=100&apikey=apikey':
        return MockResponse({"results": [{"categorie_4":"categorie4"}]}, 200)
    elif args[0] == 'https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_5&group_by=categorie_5&limit=100&apikey=apikey':
        return MockResponse({"results": [{"categorie_5":"categorie5"}]}, 200)
    return MockResponse(None, 404)

def mocked_getenv(*args, **kwargs):
    return "apikey"

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['SERVER_NAME'] = 'localhost:5001'
        cls.client = app.test_client()

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('os.getenv', side_effect=mocked_getenv)
    def test_get_all_categories(self, mock_getenv, mock_requests_get):
        json_data = get_all_categories().get_json()
        self.assertEqual(json_data, {"results": { "categories": ["categorie1", "categorie2", "categorie3", "categorie4", "categorie5"]}})


if __name__ == '__main__':
    unittest.main()