class Hero :
    def __init__(self, name, health) :
        self.name = name
        self.health = health

    def showInfo(self) :
        print(f'{self.name} dengan health: {self.health}')

class HeroIntelligent(Hero) :
    def __init__(self, name) :
        super().__init__(name, 100)
        super().showInfo()

class HeroStrength(Hero) :
    def __init__(self, name) :
        super().__init__(name, 100)
        super().showInfo()

lina = HeroIntelligent('lina')
axe = HeroStrength('axe')