# Write a program to fill in a letter template given below with name and date.
letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''
letter = letter.replace("<|Name|>","Rakib").replace("<|Date|>","18th jan 2006")
print(letter)