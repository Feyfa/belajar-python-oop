class Hero :
    # class variable
    jumlah = 0

    # variable instance private, tidak bisa di akses dari luar class
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private, tidak bisa di akses dari luar class
        self.__private = "private"

        # variable instance protected
        self._protected = "protected"


lina = Hero('lina', 100)

print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)