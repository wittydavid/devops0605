# Rest is a subset of http
# anyone that says he implemented REST basically declares that he works in the REST standard

# JS backend
# css and html are frontend

import requests

# response = requests.get("https://api.github.com/users/avielb/repos")
# all_repos = response.json()
# for i in all_repos:
#     if "name" in i.keys():
#         print(i['name'])

response = requests.post("http://127.0.0.1:5001/whatismyname")
print(response.text)

response = requests.get("http://127.0.0.1:5001/whatismyname")
