# Goal: Save a dictionary to a file.

import json
data = {"a":1}
with open("data.json", "w") as f:
    json.dump(data, f)
with open("data.json", "r") as f:
    data = json.load(f)
print(data)
