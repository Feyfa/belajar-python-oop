class Hero :
    def __init__(self, name, health, attackPower) :
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    # getter
    def getName(self) :
        return self.__name
    
    def getHealth(self) :
        return self.__health
    
    # setter
    def diserang(self,serangPower) :
        self.__health -= serangPower

    def setAttPower(self, nilaiBaru) :
        self.__attPower = nilaiBaru

# awal dari game
earthShaker = Hero("earthshaker", 50, 5)

# game berjalan
print(earthShaker.getName())
print(earthShaker.getHealth())
earthShaker.diserang(5)
print(earthShaker.getHealth())