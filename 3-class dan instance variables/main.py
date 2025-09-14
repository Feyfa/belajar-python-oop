class Hero :
    # class varible, ini seperti static attribute
    jumlah = 0

    def __init__(self, name, health, power, armor):
        # instance variable
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah += 1
        print(f'membuat hero dengan nama {self.name}')

hero1 = Hero("sniper", 100, 10, 4)
print(hero1.jumlah)
hero2 = Hero("mirana", 100, 15, 1)
print(hero1.jumlah)