from abc import ABC,abstractmethod

class Button(ABC):
    def __init__(self,link):
        self.link = link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):
    def click(self):
        print(f'Go to: {self.link}')
    
    @Button.link.setter
    def link(self,input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link

tombol1 = PushButton('https://chatgpt.com')
tombol1.click()