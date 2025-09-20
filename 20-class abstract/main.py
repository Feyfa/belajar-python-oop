# membuat class abstract
# abc = abstract base class
from abc import ABC,abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

# saat meng inheritance class abstract, itu harus mengimplementasikan method dari class Button tersebut
class PushButton(Button):
    def click(self):
        print('push button click')

# ini tidak bisa dilakukan
# tombol2 = Button()
# tombol2.click()
# ini tidak bisa dilakukan

tombol1 = PushButton()

tombol1.click()
help(tombol1)