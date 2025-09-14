class Hero :
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def serang(self,lawan) :
        print(f'{self.name} menyerang {lawan.name}')
        lawan.diserang(self)

    def diserang(self, lawan) :
        print(f'{self.name} diserang {lawan.name}')
        attack_diterima = lawan.power / self.armor
        print(f'serangan terasa : {attack_diterima}')
        self.health -= attack_diterima
        print(f'darah {self.name} tersisa : {self.health}')

sniper = Hero("sniper", 100, 10, 5)
rikimaru = Hero("rikimaru", 100, 20, 10)

sniper.serang(rikimaru)
print()
rikimaru.serang(sniper)