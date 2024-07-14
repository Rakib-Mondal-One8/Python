# sets in python is also like the set of c++ but it does not maintain order,
# Order like increasing or decreasing
s = {1,5,5,5,32 , "Rakib"};
e = set() # Don't use s = {} as it will create an empty dictonary
print(s,type(s));
s.add(18); # For inserting an element in set
s.remove(1);
print(s);