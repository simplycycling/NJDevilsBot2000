import unittest
import requests

API_URL = "https://statsapi.web.nhl.com/api/v1"


class TestNHLAPI(unittest.TestCase):

    def test_api_response(self):
        response = requests.get(API_URL + "/teams/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("teams", data)
        self.assertIsInstance(data["teams"], list)
        self.assertGreater(len(data["teams"]), 0)

    def test_api_response_contains_teams(self):
        response = requests.get(API_URL + "/teams/1")
        data = response.json()
        self.assertIn('teams', data.keys())


if __name__ == '__main__':
    unittest.main()
