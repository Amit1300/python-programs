from functools import wraps
def decorator_fun(fun):
    @wraps(fun)
    def wrapper_fun(*args):
        """This is doc string of wrapper fun"""
        print("Hello Decorator")
        return fun(*args)
    return wrapper_fun


@decorator_fun
def sum(a,b):
    '''This is doc string of sum'''
    return a+b

print (sum.__doc__)
print (sum.__name__)
