class Hero :
    # class variable, seperti static
    jumlah_hero = 0

    # constructor
    def __init__(self, name, health, power, armor) :
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah_hero += 1

    def siapa(self) :
        print(f"namaku adalah = {self.name}")

    def healthUp(self, up) :
        self.health += up

    def getHealth(self) :
        return self.health

hero1 = Hero("Yuzhong", 1500, 100, 55)
hero2 = Hero("Xborg", 1100, 60, 120)

print(hero1.__dict__)
print(hero2.__dict__)
    
hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
