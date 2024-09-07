"""
dictonary is key value pair
overlap with set
structure --> {key : value}
"""
person = {'name': 'John', 'address':'jaypur','age':18,'job':'Engineer'}
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name'] = 'Rakib'
del person['language']
print(person)

# Special dictonary looping
for k,v in person.items():
    print(k,v)