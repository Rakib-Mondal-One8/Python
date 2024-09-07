# lambda

# def doubled(x):
#     return x*2
doubled = lambda x: x*2
squared = lambda x: x**2
result = doubled(44)
# print(squared(9))
# print(result)

add = lambda x,y:x+y
# print(add(4,5))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#doubled_nums = map(doubled, numbers)
# selecting each value from the list and applying the doubled function operation on it
"""
doubled_nums = map(lambda x:x*2,numbers)
squared_nums = map(lambda x:x**2,numbers)
print(numbers)
print(list(squared_nums))
print(list(doubled_nums))
"""
actress = [
    {'name':'sabana','age':18},
    {'name':'sabnam','age':18},
    {'name':'srabonti','age':40},
    {'name':'sharvari','age':34},
]
young = filter(lambda a : a['age']<40,actress)
fivers = filter(lambda a:a['age']%5==0,actress)
print(list(fivers))
print(list(young))