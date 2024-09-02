# function is a first class object
def double_decker():
    print('starting the double decker')
    def inner_func():
        print('inside the inner func')
        return 300
    return inner_func
# print(double_decker())
# print(double_decker()())

def do_somthing(work):
    print('work started')
    # print(work)
    work()
    print('work ended')

# do_somthing(2)
# do_somthing('ami busy')
def coding():
    print("coding in python")
def sleeping():
    print("sleeping")
do_somthing(coding)
do_somthing(sleeping)