import json

with open("users.json", "r") as in_file:
    users = json.load(in_file)
print(len(users["users"]))
