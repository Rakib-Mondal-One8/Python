from fooditem import Fooditem
from menu import Menu
from restaurent import Restaurent
from users import Customer ,Admin,Employee
from order import  Order

aunty_restaurent = Restaurent("Rasida")
def customer_menu():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    customer = Customer(name, phone, email, address)

    while(True):
        print(f"Welcome {name} !!")
        print("1. View Menu")
        print("2. Add an item to cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if(choice==1):
            customer.view_menu(aunty_restaurent)
        elif (choice==2):
            item_name = input("Enter your item name: ")
            item_quantity = int(input("Enter your item quantity: "))
            customer.add_to_cart(aunty_restaurent,item_name, item_quantity)
        elif (choice==3):
            customer.view_cart()
        elif (choice==4):
            customer.pay_bill()
        elif (choice==5):
            break
        else:
            print("Invalid choice")

def admin_menu():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    admin = Admin(name, phone, email, address)

    while(True):
        print(f"Welcome {name} !!")
        print("1. Add new item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View items")
        print("5. Delete an item")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if(choice==1):
            item_name = input("Enter your new item name: ")
            item_price = int(input("Enter your new item price: "))
            item_quantity = int(input("Enter your new item quantity: "))
            admin.add_new_item(aunty_restaurent,Fooditem(item_name, item_price, item_quantity))
        elif (choice==2):
            name = input("Enter employee name: ")
            phone = input("Enter employee phone number: ")
            email = input("Enter employee email: ")
            age = input("Enter employee age: ")
            designation = input("Enter employee designation: ")
            address = input("Enter employee address: ")
            salary = input("Enter employee salary: ")
            emp = Employee(name=name, phone=phone, email=email, age=age, designation=designation, address=address,salary=salary)
            admin.add_employee(aunty_restaurent,emp)

        elif (choice==3):
            admin.view_employee(aunty_restaurent)
        elif (choice==4):
            admin.view_menu(aunty_restaurent)
        elif (choice==5):
            item_name = input("Enter an item name that you want to delete: ")
            admin.delete_item(aunty_restaurent,item_name)
        elif (choice==6):
            break
        else:
            print("Invalid choice")

while(True):
    print("Welcome !!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if(choice==1):
        customer_menu()
    elif (choice==2):
        admin_menu()
    elif (choice==3):
        break
    else:
        print("Invalid choice")
