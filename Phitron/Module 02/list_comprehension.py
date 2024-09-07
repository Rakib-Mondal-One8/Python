# List Comprehension

"""
list = [1, 2, 3, 4, 5,6,7,8,45,115,70]
odd = []
for num in list:
    if num % 2 != 0 and num%5 == 0:
        odd.append(num)
print(odd)
"""
list = [1, 2, 3, 4, 5,6,7,8,45,115,70]
odd = [n for n in list if n%2 == 1 if n%5 == 0]
print(odd)

"""
cars = ['audi','bmw','mecedes','rolls royals','lamborghini','ferreri']
price = [10,45,31,45,99,76]
cars_comb = []
for c in cars:
    for p in price:
        cars_comb.append([c,p])
print(cars_comb)
"""

cars = ['rolls royals','lamborghini','ferreri']
price = [45,99,76]
cars_comb = [(c,p) for c in cars for p in price ]
print(cars_comb)