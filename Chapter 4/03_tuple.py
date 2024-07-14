a = (1,3434.42,True,"Rakib","Rakib","Rakib")
# a[0] = 7865 Not possible because tuple is immutable
print(a)

# Methods of tuple
no = a.count("Rakib") # count of elements in tuple
print(no)
idx = a.index("Rakib") # first index of element in the tuple
print(idx)

print(len(a))

# find any element in tuple
print(2 in a)
print('Rakib' in a)