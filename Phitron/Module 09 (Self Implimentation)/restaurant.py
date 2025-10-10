from menu import *
class Restaurant:

    def __init__(self,name):
        self.name = name
        self.menu = Menu() # Menu Class
        self.employees = []

    def add_employee(self,employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List!!")
        for employee in self.employees:
            print(employee.name, employee.age, employee.phone_no)

    def view_menu(self):
       self.menu.view_menu()

    def add_menu_item(self,item_name,price,quantity):
        self.menu.add_menu_item(item_name,price,quantity)

    def remove_item(self,item_name):
        self.menu.remove_item(item_name)

    def take_order(self,item_name,quantity):
        return self.menu.take_order(item_name,quantity)