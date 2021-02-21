#Syntactical decorator

def decorator_fun(fun):
    def wrapper_fun():
        print("Hello Decorator")
        fun()
    return wrapper_fun

@decorator_fun
def f1():
    print("F1")

@decorator_fun
def f2():
    print("F2")

f1()
f2()

