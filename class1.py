class abc:
    a=7
    name="amit"
    def __init__(self,name,age):
        self.name=name 
        self.age=age
        abc.a=abc.a+1
    def a2(self):
        print(self.name,self.age)
    def a5(b):
        print(b.a)

    @classmethod
    def a3(cls,name,page):
        if cls.name==name:
            print("true")
        return False
    
    @classmethod
    def a4(cls):
        print(abc.a)
class b:
    def d():
        print("hello")

b=abc(1,4)
b.a5()
