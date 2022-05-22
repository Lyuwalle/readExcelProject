import requests


response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
# print(response.json())
# print(type(response.json()))
# print(response.json()[0])

nana_projects = response.json()

for project in nana_projects:
    print(f"project name: {project['name']}\nurl: {project['web_url']}\n")