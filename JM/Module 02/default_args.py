def sum(num1,num2):
    result = num1+num2
    return result
# total = sum(99,11,4) #TypeError: sum() takes 2 positional arguments but 3 were given
# print(total)


def sum2(num1,num2,num3=0):
    result = num1+num2
    return result
# total = sum2(99,11)
# print(total)

#args
def all_sum(n1,n2,*n):
    print(n)
    sum = 0
    for i in n:
        sum += i
    return sum
# tot = all_sum(46,45,18,11)
# print(tot)