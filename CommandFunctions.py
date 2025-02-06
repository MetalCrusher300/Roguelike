from Items import *
from entity_manager import *
# from Calculations import *
from function_mappings import function_mappings

def checkItems():
    for i in player.items:
        print(f"\t{itemList[str(i)]['name']}")
    print()

def printCommands():
    tabulator = "\n\t\t"
    for key in function_mappings:
        print(f"\t{key} {tabulator + function_mappings[key]['desc']}")
    print()

def useItem(itemID, target):
    item = itemList.get(str(itemID))  # Ensure itemID is a string to match JSON keys
    if target == "self":
        target = player  # Apply the item to the player if target is "self"

    if item:
        effect_type = item["effect_type"]
        value = item["value"]

        # Apply the effect based on the effect type
        if effect_type == "health":
            target.changeHealth(value)
            print(f"{item['name']} used on {target.name}, changing health by {item['value']}.\n"
                  f"{target.name} is now at {target.hp} HP\n")
        else:
            print(f"Effect type '{effect_type}' not implemented.")
    else:
        print(f"Item with ID {itemID} not found.")