from functools import wraps
def decorator_fun(fun):
    @wraps(fun)
    def wrapper_fun(*args):
        
        print("You are calling :",fun.__name__)
        print(fun.__doc__)
        
        return fun(*args)
    return wrapper_fun


@decorator_fun
def sum(a,b):
    '''This is doc string of sum'''
    return a+b

print (sum(10,20))
