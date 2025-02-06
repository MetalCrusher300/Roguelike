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
        "func": (3, lambda itemID, target: useItem(itemID, target)),
        "desc": "Takes (itemID, target) as arguments"
    }
}

tabulator = "\t"

def checkItems():
    for i in player.items:
        print(f"\t{itemList[str(i)]['name']}")
    print()

def printCommands():
    for key in function_mappings:
        print(f"\t{key} \n"
              f"{tabulator}\t{function_mappings[key]['desc']}")
    print()

def useItem(itemID, target):
    item = itemList.get(str(itemID))  # Ensure itemID is a string to match JSON keys
    if target == "self":
        target = player  # Apply the item to the player if target is "self"

    try: target.items.remove(itemID)
    except:
        print(tabulator + "Item not in inventory")
        return

    if item:
        effect_type = item["effect_type"]
        value = item["value"]

        # Apply the effect based on the effect type
        if effect_type == "health":
            target.changeHealth(value)
            print(f"{tabulator + item['name']} used on {target.name}, changing health by {item['value']}. \n"
                  f"{tabulator + target.name} is now at {target.hp} HP\n")
        else:
            print(f"Effect type '{effect_type}' not implemented.")
    else:
        print(f"Item with ID {itemID} not found.")