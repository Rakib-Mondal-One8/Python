class Shop:
    cart = [] # Class attributes
    def __init__(self,buyer):
        self.buyer = buyer
    def add_to_cart(self,item):
        self.cart.append(item)
rakib = Shop('Rakib')
rakib.add_to_cart('Graphic card')
rakib.add_to_cart('mackbook')
print(rakib.cart)

rajesh = Shop('rajesh')
rajesh.add_to_cart('Ryzen')
rajesh.add_to_cart('watch')
print(rajesh.cart)