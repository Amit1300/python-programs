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
    

a=c(10,20)
a1=c(2,5)
print(a+a1)
print(str(a))
print(len(a))
