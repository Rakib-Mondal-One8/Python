from abc import ABC

class User(ABC):

    def __init__(self,name,email,phone_no):
        self.name = name
        self.email = email
        self.phone_no = phone_no

    def view_menu(self,restaurant):
        restaurant.view_menu()


class Employee(User):
    def __init__(self,name,email,phone_no,age,designation,salary):
        self.age = age
        self.designation = designation
        self.salary = salary
        super().__init__(name,email,phone_no)

class Admin(User):
    def __init__(self, name, email, phone_no):
        super().__init__(name, email, phone_no)

    def add_employee(self,restaurant,employee):  # object of Restaurant Class
        restaurant.add_employee(employee)

    def view_employee(self,restaurant):
        restaurant.view_employee()

    def add_menu_item(self, restaurant, item_name,price, quantity):  # object of Restaurant Class
        restaurant.add_menu_item(item_name,price,quantity)

    def remove_item(self,restaurant,item_name):
        restaurant.remove_item(item_name)

class Customer(User):

    def __init__(self, name, email, phone_no):
        super().__init__(name, email, phone_no)
        self.cart = []

    def show_menu(self,restaurant):
        restaurant.view_menu()

    def add_to_cart(self,restaurant,item_name,quantity=1):
        order = restaurant.take_order(item_name,quantity)
        if(order):
            self.cart.append(order)
            print('Order Added to Cart!!')
        else:
            print("Sorry Can't Add to Cart")


    def view_cart(self):
        print("*****View Cart*****")
        print(f"Item Name\tPrice\tQuantity")
        for item in self.cart:
            print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}")
