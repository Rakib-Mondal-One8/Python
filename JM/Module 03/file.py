"""
.csv --> comma separated value
.txt --> text file
"""

with open('message.txt','w') as file: # w for only write
    file.write('Hello python rakib is here ')

with open('message.txt','a') as file: # a for append
    file.write('Hello python rakib is here ')


with open('message.txt','r') as file:
    text = file.read()
    print(text)