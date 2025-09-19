class Team:
    def setTeam(self,team):
        self.team = team

    def showTeam(self):
        print(self.team)

class TipeHero:
    def setTipe(self,tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)

class Hero(Team,TipeHero):
    def __init__(self,name,health):
        self.name = name
        self.health = health

Ucup = Hero('Ucup',100)

Ucup.setTeam('merah')
Ucup.setTipe('Fighter')

Ucup.showTeam()
Ucup.showTipe()