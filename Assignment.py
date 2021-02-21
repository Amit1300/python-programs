#empty class
class a:
    pass


#3
class abc:
    c=10# static class variable
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.age)
a=abc("amit",45)
print(a.name)
#answer 4
a.name="amit nagar"
print(a.name)



#answer 5 deleting object
#del a
#a.show()


# copy one object to another
b=abc("amit",45)
c=b

c.show()
# class variable access

print(c.c)


# __call__ we can use call magic method like function example b=acb(),b(10,50)
#we can pass argument to do operation same as like function


class d: 
    def __new__(cls): 
         print("Creating instance") 
         return super(d, cls).__new__(cls) 
  
    def __init__(self): 
        print("Init is called") 
  
d() 

#iter and next


class add:

    def __init__(self,string):
        self.string=string
        self.data=len(string)


    def __iter__(self):
        return self

    def __next__(self):
        if self.data == 0:
            pass
        
        else:
            self.data = self.data- 1
            return self.string[self.data]
s=add("amit")
s=iter(s)
print(next(s))


#How super() works with _init_() method in multiple inheritance?

class a:
    b="amit"
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def show1(self):
        print(self.x)
        print(self.b)

class b(a):
    def __init__(self,z,w,k,x,y):
        super().__init__(x,y)
        self.z=z
        self.w=w
        self.k=k
        
        
    def show(self):
        print(self.w,self.x)
class c:
    b=6
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
        print(self.b)
        
    def show1(self):
        return "amit"
        
    def __add__(self,other):
        return self.x+self.y
    
    def __str__(self):
        return "(%s,%s)"%(self.x,self.y)
    def __len__(self):
        return len(self.show1())
    















        
        









