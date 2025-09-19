class Mangga:
    # magic method
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self):
        return "ini berasal dari magic method __repr__"
    
    def __str__(self):
        return "ini berasal dari magic method __str__"
    
    def __add__(self,objek):
        return self.jumlah + objek.jumlah
    
    @property
    def __dict__(self):
        return "ini berasal dari magic method __dict__"

belanja1 = Mangga('manalagi',10)
belanja2 = Mangga('arumanis',5)
belanja3 = Mangga('arumanis',15)

# ini akan menjalankan event magic method __str__(self), jika tidak ada __str__(self) hanya ada __repr__(self), maka __repr__(self) yang akan dijalankan
print(belanja1)

# ini akan menjalan event maic method __repr__(self)
print(repr(belanja1))

# ini akan menjalankan event magic method __add__. catatan ini hanya bisa menjumlahkan 2 object saja, menggunakan lebih dari dari 2 object akan error
print(belanja1 + belanja2)

# ini akan menjalan event maic method __dict__(self)
print(belanja1.__dict__)