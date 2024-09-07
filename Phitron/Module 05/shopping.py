class Shopping:
    def __init__(self,tot):
        self.tot_money=tot
        self.cart = []
    def add_to_cart(self,item,price,quantity):
        self.cart.append({'item':item,'price':price,'quantity':quantity})
    def cost(self):
        tot = 0
        for item in self.cart:
            a = item['quantity']
            b = item['price']
            tot+=a*b
        return tot
    def deal(self,price):
        if(price<=self.tot_money):
            print(" Get you money ",self.tot_money-price,"back and enjoy you deal")
        else:
            print("Please give",price-self.tot_money,"more To make this deal")

rakib = Shopping(10000)
rakib.add_to_cart('mac M3 pro',150000,2)
print(rakib.cost())
rakib.deal(rakib.cost())