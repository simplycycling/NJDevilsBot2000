import requests

API_URL = "https://statsapi.web.nhl.com/api/v1"

response = requests.get(API_URL + "/teams/1")

data = response.json()

print(data)
