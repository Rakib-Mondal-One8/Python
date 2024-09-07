def full_name(first_name, last_name):
    name = f'{first_name} {last_name}'
    return name
# name = full_name(last_name = 'kodue', first_name='alu')
# print(name)

def famous_person(first,last,**additional):
    name = f'{first} {last}'
    # print(additional['title'])
    for key, value in additional.items():
        print(key, value)
    return name
# name = famous_person(first='Rakib',last = 'ali',title = 'khan',additional='king')
# print(name)
"""
*args it recieves values as a tuple in a calling function
**agrs it recieves key:value pairs it means the dictonary
"""

# return multiple things for an function
def fun(n1,n2):
    return n1+n2,n1*n2,n1/n2
print(fun(5,3))