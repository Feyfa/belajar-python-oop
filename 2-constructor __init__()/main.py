class Hero :
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

hero1 = Hero("sniper", 100, 10, 4)
hero2 = Hero("mirana", 100, 15, 1)

print(hero1.__dict__)
print(hero2.__dict__)