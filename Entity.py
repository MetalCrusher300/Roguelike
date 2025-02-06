class Entity:
    def __init__(self, entityType, maxHealthPoint, defenceValue, attackDamage, name = None, items = None):
        match entityType:
            case "Player": self.type = 0
            case "Enemy": self.type = 1

        self.maxHealth = maxHealthPoint
        self.hp = self.maxHealth
        self.dp = defenceValue
        self.atk = attackDamage

        self.name = name
        if self.name is None: self.name = "Enemy"

        self.items = items

    def changeHealth(self, change):
        self.hp = max(0, min(self.hp + change, self.maxHealth))