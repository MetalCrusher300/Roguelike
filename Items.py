import json

with open("itemDesc.json", "r") as file:
    data = json.load(file)

itemList = data["itemList"]