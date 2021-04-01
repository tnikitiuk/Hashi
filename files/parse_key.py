import json
with open('key.json', 'r') as file:
	key_load = json.load(file)

print(key_load["data"]["key"])
