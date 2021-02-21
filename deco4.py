def a2(func):
    def wrapper():
        func()
        print("AMIT")
    return wrapper





@a2
def a1():
    print( "hello")
print(a1())
    
