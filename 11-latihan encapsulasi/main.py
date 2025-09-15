class Hero :
    # private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self) :
        lines = [
            f"{self.__name} : ",
            f"level = {self.__level}",
            f"health = {self.__health}/{self.__healthMax}",
            f"attack = {self.__attPower}",
            f"armor = {self.__armor}",
            f"exp = {self.__exp}"
        ]
        return "\n\t".join(lines)
    
    @property 
    def gainExp(self) :
        pass

    @gainExp.setter
    def gainExp(self, addExp) :
        self.__exp += addExp
        if (self.__exp >= 100) :
            print(f'{self.__name} level up')
            self.__level += 1
            self.__exp = self.__exp - 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
        
    def attack(self, musuh) :
        self.gainExp = 50
    

slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 10, 20)

print(slardar.info)

slardar.attack(axe)
print(slardar.info)

slardar.attack(axe)
print(slardar.info)

slardar.attack(axe)
print(slardar.info)
