class Shopping:
    def __init__(self,tot):
        self.tot_money=tot
        self.cart = []

    def add_wallet_money(self,amount):
        self.tot_money+=amount

    def add_to_cart(self,item,price,quantity):
        self.cart.append({'item':item,'price':price,'quantity':quantity})

    def remove_from_cart(self,item_name,quantity):
        for item in self.cart:
            if (item['item'] == item_name):
                item['quantity'] -= quantity
                if(item['quantity'] <= 0):
                    self.cart.remove(item)
                return

    def cost(self):
        tot = 0
        for item in self.cart:
            a = item['quantity']
            b = item['price']
            tot+=a*b
        return tot

    def deal(self):
        price = self.cost()
        if(price<=self.tot_money):
            self.tot_money-=price
            self.cart.clear()
            print("Congratulations! Enjoy your deal")
        else:
            print("Sorry, you don't have enough money")

rakib = Shopping(10000)
rakib.add_to_cart('mac M3 pro',150000,2)
print(rakib.cost())

rakib.remove_from_cart('mac M3 pro',1)
print(rakib.cart)
rakib.remove_from_cart('mac M3 pro',1)
print(rakib.cart)