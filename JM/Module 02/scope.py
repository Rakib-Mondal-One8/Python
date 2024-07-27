balance = 3000 # global variable
balance = balance * 2
def buy_things(item,price):
    # balance/=2  can't modify the global variable inside a function
    # balance = 500 # locally created
    global balance # Now i can access and modify the global variable with the use of global keyword
    balance /=2
    print(balance)
buy_things('apple',100)