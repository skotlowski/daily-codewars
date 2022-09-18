class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def strike(self, enemy, swings):
        # health cannot go below zero
        enemy.health = enemy.health - (swings * 10) if enemy.health - (swings * 10) >= 0 else 0
