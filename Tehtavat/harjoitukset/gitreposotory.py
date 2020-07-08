import requests
from pprint import pprint

data = requests.get("https://api.github.com/search/repositories?q=language:python").json()
#for fork in sorted(data['items'], key=lambda x: x["forks"]):
lista = []
for fork in data['items']:
    lista.append(f'Fork: {fork["forks"]}, Name: {fork["name"]}, Description: {fork["description"]}')
lista.sort()

for num in lista:
    print(num)
