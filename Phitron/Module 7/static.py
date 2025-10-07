# static attributes (Class attributes)
# static method @staticmethod
# class method @classmethod
# differences between classmethod and staticmethod
class Shopping:
    cart = [] #class attribute or Static attribute
    origin = 'china'

    def __init__(self,name, location):
        self.name = name
        self.location = location
    def purchase(self,item,price,amount):
        rem = amount - price
        print(f'buying: {item} for price: {price} and amount: {rem}')
    @staticmethod
    def multiply(a,b): # static method don't use self parameter
        return a*b
    @classmethod
    def hudai_dekhi(cls,item):
        print(f'hudai dekhi kintu kinmu na just ac er hau khete esechi')

basu = Shopping('dokan','kolkata')
basu.purchase('lungi',500,1200)
basu.hudai_dekhi(4)
Shopping.hudai_dekhi('lungi')
print(Shopping.multiply(5,5))
