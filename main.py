import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "тестовый post запрос",
    "body": "тестовый контент post запроса",
    "userId": 2
}

response = requests.post(url, json=data)

print(response.status_code)

print(f"ответ - {response.json()}")




# response = requests.get('https://www.google.com')
#
# print(response.status_code)
#
# print(response.headers)
#
# print(response.text)





# import pprint
#
#
# params = {
#     'q': 'python'
#     }
#
# response = requests.get('https://api.github.com/search/repositories', params=params)
#
# response_json = response.json()
#
#
# # pprint.pprint(response_json)
#
# print(f"Количество репозиториев с использованием python: {response_json['total_count']}")


