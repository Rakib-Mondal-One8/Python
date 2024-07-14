# Q. 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

d = {}
for i in range(1,5):
    x = input("Enter the name of the language");
    d.update({x:i});
print(d);