from abc import ABC,abstractmethod
# abstract base class
class Animal(ABC):
    @abstractmethod # enforce all derived class to have a eat method
    def eat(self):
        print('I need food')
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name):
        self.catagory = "Monkey"
        self.name = name
        super().__init__()
    def eat(self):
        print("Eating banana")
    def move(self):
        print("Moving monkey")
lyka = Monkey("Lyka")
lyka.eat()