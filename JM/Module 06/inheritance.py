# Base class, Parent class, (common attribute + functionality class)
# Derived class, child class, (uncommon attributes + functionality)

class Gadget:
    def __init__(self,brand,price,color,origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    def __repr__(self):
        return (f'Gadget {self.brand} {self.price} {self.color} {self.origin}')

    def run(self):
        pass



class Laptop(Gadget):
    def __init__(self,brand,price,color,origin, memory,ssd):
        self.memory = memory
        self.ssd = ssd
        super().__init__(brand, price, color, origin);
    def __repr__(self):
        print(f'RAM {self.memory} GB , SSD {self.ssd} GB')
        return super().__repr__()

    def coding(self):
        return f'learning python and practicing'


class Phone(Gadget): # (Gadget) means it inherited gadget
    def __init__(self,brand,price,color,origin, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,origin)
    def phone_call(self, number, text):
        return f'Sending sms to {number}'
    def __repr__(self) :
        print(f'{self.dual_sim}')
        return super().__repr__()


class Camera:
    def __init__(self, pixel):
        self.pixel = pixel

    def change_lens(self):
        pass

# my_phone = Phone('iphone',120000,'silver','china',True)
# print(my_phone)
l = Laptop("lenovo",50000,"black","china",16,512)
print(l)