import json
with open('cert.json', 'r') as file:
	key_load = json.load(file)

print(key_load["data"]["cert"])
