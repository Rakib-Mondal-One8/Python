import math
import time


def timer(func):
    def inner(*args, **kwargs):
        print('time started')
        start = time.time()
        #print(func)
        func(*args,**kwargs)
        print('time ended')
        end = time.time()
        print(f'total time: {(end - start)}')
    return inner

@timer
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'factorial of {n} is {result}')
get_factorial(n=120)

# timer()()