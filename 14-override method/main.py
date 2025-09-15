class Hero : 
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self) :
        lines = [
            f"{self.name} : ",
            f"health = {self.health}",
        ]
        print(f'{"\n\t".join(lines)}')

class HeroIntelligent(Hero) :
    def __init__(self, name):
        super().__init__(name, 100)
    
    def showInfo(self):
        lines = [
            f"{self.name} : ",
            f"tipe: Intelligent",
            f"health = {self.health}",
        ]
        print(f'{"\n\t".join(lines)}')

class HeroStrength(Hero) :
    def __init__(self, name):
        super().__init__(name, 100)

lina = HeroIntelligent('lina')
axe = HeroStrength('axe')

lina.showInfo()