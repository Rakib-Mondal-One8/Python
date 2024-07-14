d = {} # empty dictonary
marks = {
    "Rakib" : 100,
    "Rajesh" : 56,
    "Raju" : 26,
    0 : "Harry"
}
# print(marks.items());
# print(marks.keys());
# print(marks.values());
# marks.update({"Rajesh" : 100,"Rebeka" : 110})
# print(marks)
print(marks.get("Rebeka")) # prints none
print(marks["Rebeka"]) # return an error if the key is not available