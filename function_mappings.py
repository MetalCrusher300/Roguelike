from CommandFunctions import *

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