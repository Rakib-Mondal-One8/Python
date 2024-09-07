# Encapsulation --> Hiding details
# access modifiers --> public,protected,private
class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name = holder_name #public
        self._branch = 'Bongaon' #protected
        self.__balance = initial_deposit #private
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if(amount > self.__balance):
            print("No money")
        else :
            self.__balance-=amount
            return self.__balance
rakib = Bank("toye toye",10000)
print(rakib.holder_name)
rakib.holder_name = "boro vai"
print(rakib.holder_name)
rakib.deposit(5000)
# print(rakib._branch)
print(rakib.get_balance())
print(rakib.withdraw(500))