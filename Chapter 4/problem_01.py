# Write a program to store seven fruits in a list entered by the user.

fruits = []
for i in range(1,8):
    f1 = input("Enter Fruit: ")
    fruits.append(f1)
fruits.sort()
print(fruits)