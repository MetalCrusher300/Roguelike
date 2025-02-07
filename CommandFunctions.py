from Items import *
from entity_manager import *
# from Calculations import *

function_mappings = {
    "checkItems": {
        "func": (1, lambda: checkItems()),
        "desc": "Returns the current items in inventory"
    },
    "help": {
        "func": (1, lambda: printCommands()),
        "desc": "Prints all functions"
    },
    "useItem": {
        "func": (2, lambda itemID: useItem(itemID)),
        "desc": "Takes (itemID, target) as arguments"
    },

    "debug" : {
        "func" : (2, lambda target : Debug(target)),
        "desc" : "This is the debug function"
    }
}

tabulator = "\t"

def Debug(target):
    entity = entities[target] if target in entities else print(tabulator + "Target not found\n")
    print(entity.items)

def checkItems():
    for i in entities["player"].items:
        print(f"\t{itemList[str(i)]['name']}")
    print()

def printCommands():
    for key in function_mappings:
        print(f"\t{key} \n"
              f"{tabulator}\t{function_mappings[key]['desc']}")
    print()

def useItem(itemIndex):
    try:
        itemIndex = int(itemIndex)

    except:
        print(tabulator + f"'{itemIndex}' is not valid index\n")
        return

    if itemIndex <= 0 or itemIndex > (len(entities["player"].items)):
        print(tabulator + f"'{itemIndex}' is not valid inventory index\n")
        return

    currentInventory = entities["player"].items
    itemID = currentInventory[itemIndex - 1]
    item = itemList[str(itemID)]

    if itemID:
        effect_type = item["effect_type"]
        value = item["value"]

        # Apply the effect based on the effect type
        if effect_type == "health":
            entities["player"].changeHealth(value)
            print(f"{tabulator + item['name']} used on {entities["player"].name}, changing health by {item['value']}. \n"
                  f"{tabulator + entities["player"].name} is now at {entities["player"].hp} HP\n")
        else:
            print(f"Effect type '{effect_type}' not implemented.")
            return
    else:
        print(f"Item with ID {itemID} not found.")
        return

    currentInventory.remove(currentInventory[itemIndex - 1])