import json
path = 'Desktop/Wesley/Python_learnings/json/configs.json'

with open(path, 'r') as json_file:
    dados = json.load(json_file)

print(dados)
print(type(dados))