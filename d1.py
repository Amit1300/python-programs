'''
def outerfun(function_Args):
    def innerfun():
        .......
        .....
        function_Args()
    return innerfun
'''

def decorator_fun(fun):
    def wrapper_fun():
        print("Hello Decorator")
        fun()
    return wrapper_fun

def f1():
    print("F1")
    
def f2():
    print("F2")

f=decorator_fun(f1)
f()
f=decorator_fun(f2)
f()
