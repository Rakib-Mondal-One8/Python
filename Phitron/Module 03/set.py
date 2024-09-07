"""
list --> []
tuple --> ()
set --> {}
"""

# set : unique items collection
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = {} # type is dictonary
print(type(s))
s = set() # type is set
print(type(s))
numbers_set = set(numbers)
"""
print(numbers)
numbers_set.add(11)
numbers_set.remove(1)
print(numbers_set)
"""

for item in numbers_set:
    print(item)
a = {1,3,5,7}
b = {1,2,3,4,5}
print(a&b) # & is for intersection operation
print(a|b) # | is for union operation