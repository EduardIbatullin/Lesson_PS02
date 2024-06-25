import requests
import pprint

params = {
    'q': 'html'
    }

response = requests.get('https://api.github.com/search/repositories', params=params)

print(f"Статус-код ответа: {response.status_code}")
print(f"\nСодержимое ответа в формате JSON:\n")
response_json = response.json()
pprint.pprint(response_json)
