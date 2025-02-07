class Player:
    def __init__(self, maxHealthPoint, defenceValue, attackDamage, name = None, items = None):

        self.maxHealth = maxHealthPoint
        self.hp = self.maxHealth
        self.dp = defenceValue
        self.atk = attackDamage

        self.name = name
        if self.name is None: self.name = "Enemy"

        self.items = items

    def changeHealth(self, change):
        self.hp = max(0, min(self.hp + change, self.maxHealth))

class Enemy:
    def __init__(self, maxHealthPoint, physicalDefenceValue, artsDefenseValue, attackDamage, damageType, speed):
        self.maxHealth = maxHealthPoint
        self.hp = self.maxHealth
        self.pdp = physicalDefenceValue
        self.adp = artsDefenseValue
        self.atk = attackDamage
        self.damageType = damageType
        self.speed = speed


    def changeHealth(self, change):
        self.hp = max(0, min(self.hp + change, self.maxHealth))