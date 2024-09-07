numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.append(99) # inserting in the back of the list
# print(numbers)
# inserting in a specific index
# numbers.insert(1,100)
numbers.insert(2,200)
# n = int(input("Enter the number you want to remove"))
# if(n in numbers):
#     numbers.remove(100)
n = numbers.pop()
# print(n,numbers)
"""
x = int(input("Enter the number for which you want to know the index :"))
idx = -1
if(x in numbers):
    idx = numbers.index(x)
print(idx)
"""
new_list = [43,3,12,6,45,89,53,111]
sorted_list = sorted(new_list) # new_list.sort() it will also work
print(sorted_list)
sorted_list.reverse();
print(sorted_list)