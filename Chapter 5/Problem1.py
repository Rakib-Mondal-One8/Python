# Q. 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).
s = set();
for i in range(0,8):
    x = int(input("Enter a number: "))
    s.add(x)
print(s);