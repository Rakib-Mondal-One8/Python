class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name} {self.price}'
    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self,name,price,seat,weight,temperature):
        self.seat = seat
        self.weight = weight
        self.temperature = temperature
        super().__init__(name,price)

    def __repr__(self):
        print(f'{self.seat} {self.weight} {self.temperature}')
        return super().__repr__()


class Truck(Bus):
    def __init__(self,name,price,seat,weight,temperature):
        super().__init__(name,price,seat,weight,temperature)
    def __repr__(self):
        return super().__repr__()

class PickUpTruck(Truck):
    def __init__(self,name,price,seat,weight,temperature):
        super().__init__(name,price,seat,weight,temperature)
    def __repr__(self):
        return super().__repr__()

class ACBus(Bus):
    def __inti__(self,name,price,weight,seat,temperature):
        super().__init__(name,price, seat,weight,temperature)
    def __repr__(self):
        return super().__repr__()

green_line = ACBus('Green',100,5,10000,28)
trc = Truck('Truc',100,5,283,35)
print(green_line)
print(trc)