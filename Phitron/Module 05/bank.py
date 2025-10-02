class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw = 100
        self.max_withdraw = self.balance

    def set_bind(self):
        self.max_withdraw = self.balance

    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if(amount > 0):
            self.balance+=amount
            self.set_bind()
    def withdraw(self,amount):
        if(amount < self.min_withdraw) or (amount > self.max_withdraw):
            print(f'You can\'t withdraw {amount}')
        else:
            self.balance-=amount
            self.set_bind()
            print(f'You withdrawn {amount}')
            print(f'Your balance is {self.balance}')


rakib = Bank(10000)
print(rakib.get_balance())
rakib.withdraw(99)
rakib.withdraw(200)
rakib.withdraw(10000)