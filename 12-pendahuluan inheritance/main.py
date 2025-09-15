class Hero :
    def __init__(self, name, health):
        self.name = name
        self.health = health

class HeroIntelegent(Hero) :
    pass

class HeroStrength(Hero) :
    pass

lina = Hero('lina', 100)
techies = HeroIntelegent('techies', 50)
axe = HeroStrength('axe', 50)

print(lina.name)
print(techies.name)
print(axe.name)