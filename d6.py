from functools import wraps

def decorator_fun(fun):
    @wraps(fun)
    def wrapper_fun(*args):      
        dt=[]
        for i in args:
            dt.append(type(i)==int)
        if all(dt):
            return fun(*args)
        else:
            print("Invalid value")
    return wrapper_fun

@decorator_fun
def sum(*args):
    '''This is doc string of sum'''
    s=0
    for i in args:
        s+=i
    return s
print (sum(10,20,30,40,50,[22,33,44]))


'''
def sum(*a):
    s=0
    for i in a:
        s+=i
    return s
print (sum(10,20,30,40,50,[44,55,66]))
'''
