def s2(func):
    def inner():
        print("hi")
        x=func()
        y=x.lower()
        return y
    return inner
    


@s2
def s1():
    return "MY NAME IS AMIT"
print(s1())


def a1(func):
    def inner(x,y):
        x=func(x,y)
        y=5*x
        print(y)
        print("decorator")
        print(y**2)
        
    return inner
    

@a1
def add(x,y):
    print("addition")
    print("helooooooooooooo")
    return x+y
print(add(5,7))
print(add._name_)


