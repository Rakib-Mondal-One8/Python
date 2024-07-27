"""
class Calculator:
    brand = 'Casio fx991 ex plus'
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

res = Calculator()
print(res.add(5,6))
print(res.subtract(5,6))
print(res.multiply(5,6))
print(res.divide(5,6))

"""

class Pen:
    manufectured = 'India'
    def __init__(self,brand,ink,price):
        self.brand = brand
        self.ink = ink
        self.price = price
    def show(self,pen):
        print(pen.brand,pen.ink,pen.price)

pen1 = Pen('Parker','blue',10000)
pen1.show(pen1)
