class Person:
    def __init__(self, name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("rise,meat,polao")

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name,age,height,weight,team):
        self.team = team
        super().__init__(name,age,height,weight)

    # override
    def eat(self):
        print('vagetables')

    def exercise(self):
        print('gym')

    # + sign operator overload
    def __add__(self, other):
        return self.age  + other.age
    # * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight
    # len overload
    def __len__(self):
        return self.height
    # > operator overload
    def __gt__(self, other):
        return self.age>other.age

rakib = Cricketer('rakib',18,76,58,'IND')
mushi =  Cricketer('mushi',18,75,58,'BD')
rakib.eat()
rakib.exercise()
print(rakib + mushi)
print(rakib * mushi)
print(rakib>mushi)
print(len(rakib))


"""
Plus sign overload
print('Rakib'+'Sakib')
print([13,21]+[31,53,12,18])
"""

