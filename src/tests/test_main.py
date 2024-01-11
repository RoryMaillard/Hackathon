import unittest
from unittest import mock

import sys
sys.path.append('./src/src')
import main


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_1&group_by=categorie_1&limit=100&apikey=apikey':
        return MockResponse({"results": [{"categorie1":"categorie1"}]}, 200)
    else:
        return MockResponse({"results": [{"categorie1":"categorie2"},{"categorie1":"categorie3"}]}, 200)

def mocked_getenv(*args, **kwargs):
    return "apikey"

class TestStringMethods(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('os.getenv', side_effect=mocked_getenv)
    def test_get_all_categories(self, mock_get):
        json_data = get_all_categories()
        self.assertEqual(json_data, {"results": [{"categorie1":"categorie1"},{"categorie1":"categorie2"},{"categorie1":"categorie3"}]})


if __name__ == '__main__':
    unittest.main()