class a:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
       
        

    def add(self):
       print(self.name,self.age)

class b(a):
    
     def __init__(self,name,age,rollno,photo):
        a.__init__(self,name,age)
        self.n=rollno
        self.a=photo
        a.__init__(self,name,age)
        
     def a1(self):
        print(self.n,self.a)


c=b("amit",50,567,"pic")
c.a1()
c.add()
print(isinstance(c,b))
print(issubclass(b,a))
c.add()
b=a("mohit",56)
b.a11()
