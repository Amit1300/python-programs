def decorator_fun(fun):
    def wrapper_fun(*args):
        print("Hello Decorator")
        r=fun(*args)
        #return fun(*args)
        return r
    return wrapper_fun

@decorator_fun
def fun(a):
    print(str(a))

@decorator_fun
def sum(a,b):
    #print(50+90)
    return a+b

fun(3)
print (sum(2,3))
