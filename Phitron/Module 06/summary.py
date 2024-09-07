# from abc import ABC,abstractmethod
class Book():
    def __init__(self,name):
        self.name = name
    def read(self):
       raise NotImplementedError # Replacement of ABC (Abstraction base class)

class Physics(Book):
    def __init__(self,name):
        super().__init__(name)
    def read(self):
        print("Reading Physics")

duari = Physics('arihant')
print(duari.name)
duari.read()