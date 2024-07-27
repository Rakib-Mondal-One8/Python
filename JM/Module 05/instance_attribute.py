class Shop:
    shopping_mall = 'Star mall'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # instance attributes
    def add_cart(self, item):
        self.cart.append(item)

rakib = Shop('rakib')
rakib.add_cart('mackbook')
rakib.add_cart('puma')
print(rakib.cart)

rajesh = Shop('rajesh')
rajesh.add_cart('Ryzen')
rajesh.add_cart('watch')
print(rajesh.cart)