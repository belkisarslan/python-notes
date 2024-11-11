import json

with open("data.json", "r") as d:
    content = json.load(d)
    for data in content["datas"]:
        print(data)
