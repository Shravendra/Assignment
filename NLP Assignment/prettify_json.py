import json

with open('tweets.json', 'r+') as f:
    data = json.load(f)
    json.dump(data, f, indent=4)