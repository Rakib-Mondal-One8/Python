from users import *
from restaurant import *
from menu import *
from food_item import *
from order import *
restaurant = Restaurant("Rizzs")
def customer_menu():
    name = input('Enter Name: ')
    email = input('Enter Email: ')
    phone_no = input('Enter Phone No: ')
    customer = Customer(name,email,phone_no)

    while (True):
        print(f"Welcome {name} !!")
        print("1. View Menu")
        print("2. Add an item to cart")
        print("3. View Cart")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        if (choice == 1):
            customer.view_menu(restaurant)
        elif (choice == 2):
            item_name = input("Enter your item name: ")
            item_quantity = int(input("Enter your item quantity: "))
            customer.add_to_cart(restaurant, item_name, item_quantity)
        elif (choice == 3):
            customer.view_cart()
        elif (choice == 4):
            break
        else:
            print("Invalid choice")


def admin_menu():
    name = input('Enter Name: ')
    email = input('Enter Email: ')
    phone_no = input('Enter Phone No: ')
    admin = Admin(name, email, phone_no)

    while (True):
        print(f"Welcome {admin.name} !!")
        print("1. View Menu")
        print("2. Add New Food Item")
        print("3. Add New Employee")
        print("4. Remove Item")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if (choice == 1):
            admin.view_menu(restaurant)
        elif(choice == 2):
            item_name = input("Enter Item Name: ")
            price = int(input(f"Enter {item_name} Price: "))
            quantity = int(input("Enter Quantity: "))
            admin.add_menu_item(restaurant,item_name,price,quantity)

            print("Congratulations!!! Now Restaurant has a new Item in it's menu card!!")
        elif(choice == 3):
            print("*****Enter Employee Details*****")
            name = input("Enter name: ")
            email = input("Enter email no.: ")
            phone_no = input("Enter phone_no: ")
            age = int(input("Enter the Age: "))
            designation = input("Enter the Designation: ")
            salary = int(input("Enter the salary: "))

            e = Employee(name,email,phone_no,age,designation,salary)
            admin.add_employee(restaurant,e)

        elif(choice == 4):
            item_name = input("Enter Item name: ")
            admin.remove_item(restaurant,item_name)
        elif(choice == 5):
            break
        else:
            print("Invalid choice")


while(True):
    print("*****Welcome to Rizzs*****")
    print("Welcome !!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        customer_menu()
    elif (choice == 2):
        admin_menu()
    elif (choice == 3):
        break
    else:
        print("Invalid choice")
