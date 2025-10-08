# readonly --> you can not set value
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute
# setter --> set a value of a property through a method. Most of the time , you will set the value of a private property
class User:
    def __init__(self,name,age,money):
        self.name = name
        self._age = age
        self.__money = money

    # getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age

    # getter without any setter is readonly attribute
    @property
    def salary(self):
        return self.__money

    @salary.setter
    def add_salary(self,value):
        if(value<0):return 'salary cannot be negative'
        self.__money += value


samsu = User('kopa',21,12000)
# print(samsu.__money)
# print(samsu.age())
print(samsu.age)
# print(samsu.salary())
print(samsu.salary,1)
samsu.add_salary = 3000
print(samsu.salary,2)