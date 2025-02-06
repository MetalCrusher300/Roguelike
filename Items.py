import json

with open("itemDesc.json", "r") as file:
    data = json.load(file)

itemList = data["itemList"]

def itemIsOwned(itemID, target):
    if itemID in target.item: return True
    else: return False