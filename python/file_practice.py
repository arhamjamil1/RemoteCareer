import json

file = open("python/user.json", "r")

data = json.load(file)

print(data["name"])
print(data["degree"])
print(data["age"])

file.close()