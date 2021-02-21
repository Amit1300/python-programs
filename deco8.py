#deco8
from functools import wraps
def add(func):
    @wraps(func)
    def inner(x,y):
        if x==0:
         return 0
        else:
            print("the sum of" ,x,",",y,"=",func.__name__)
            return func(x,y)

    return inner




@add
def add(a,b):
    return a+b
print(add(0,0))



def list2(func):
    def inner(a):
        d=[]
        for x in a:
            if x%2==1:
                d.append(x)
                for x in d:
                    return func(a)+6
                
                    print(d)
            else:
                if x%2==0:
                    print("hello")
                    return "error"
               
        
    return inner




@list2
def list1(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum
print(list1([46,6,6,6,66]))
print(list1([1,4]))
