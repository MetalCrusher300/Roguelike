from Entity import *
import json

with open("enemy_preset.json", "r") as file:
    data = json.load(file)

enemyPreset = data["enemies"]

entities = {
    "player" : Player(10, 0, 3, "Rico", [0, 1, 2]),

    "enemy" : Enemy(*enemyPreset.get("Metal Slug").values())
}

fruits = {
    "apple" : {
        "origin" : "greece",
        "number" : 100
    },
    "pear" : {
        "origin" : "china",
        "number" : 50
    }
}

class Fruit:
    def __init__(self, origin, number):
        self.origin = origin
        self.number = number