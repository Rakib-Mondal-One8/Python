# def multiple():
#     return 18,1
# print(multiple(),type(multiple()))

things = 'pen','phone','laptop'
if('laptop' in things):
    print('laptop is exist')
things[0] = 'marker'  # tuple are immutable
print(len(things))
print(things)

mega = ([1,3,4],[4,10])
mega[0][1]  = 666 # It changed because the list is mutable, it does'nt matter inside what it is
print(mega)


"""
print(things)
print(type(things))
print(things[0])
print(len(things[1]))
print(things[0:3])

"""