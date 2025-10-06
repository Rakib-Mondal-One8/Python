from abc import ABC,abstractmethod

class Shop(ABC):

    @abstractmethod #decorator
    def add_product(self):
        pass
    @abstractmethod #decorator
    def buy_product(self): # instances must implement this method
        pass

    def some_method(self): # Not Enforcing the instances of this class to implement this method
        pass

class Flipkart(Shop):
    products = {}
    availability = {}
    def __init__(self,name,location):
        self.name = name
        self.location = location

    def add_product(self,product):
        key = product.id
        if(key not in self.products):
            self.products[key] = product
        self.availability[key] = self.availability.get(key,0)+1

    def buy_product(self,id,quantity):
        if(id in self.products):
            if(self.availability.get(id) < quantity):
                print(f'Sorry this product is out of stock!')
            else:
                item = self.products[id]
                item_price = item.price
                payment = int(input(f'Pay ${item_price*quantity} to Purchase! :'))
                if(payment >= item_price):
                    self.availability[id]-=quantity
                    print(f'Congratulations!! Enjoy Your day!')
                else:
                    print(f'Not enough money to do this purchase')
        else:
            print(f"Product with id no.{id} does'nt exists")

class Product:
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price

s = Flipkart('Flipkart','Kolkata')
p1 = Product(1,'ArcSaber7 Tour',7000)
s.add_product(p1)

for i in range(2,5):
    name = input('enter product name: ')
    price = int(input('enter product price: '))
    product = Product(i,name,price)
    s.add_product(product)






