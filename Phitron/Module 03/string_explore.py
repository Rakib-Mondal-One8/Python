name = 'Rakib\'s Mondal' # \ escape
name2 = "Rakib Mondal"
# Multiline string
name3 = """
    Rakib Mondal
    number one
"""
# print(name)
# print(name3)
for c in name2:
    print(c)
print(name2[3])
print(name2[1:6])
print(name2[-7])
print(name2[::-1])

# mututable means changeable
# immutable means unchangeble
# name[0] ='r'  not supported as name is immutable

if 'Rak' in name2:
    print('Exist')
