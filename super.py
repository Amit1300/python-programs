class a:
    def __init__(self,name):
        print("hello")
        self.name=name
        print(self.name)


class b(a):
    def add(self):
        print(self.name)



a1=b("Amit")
a1.add()






class arsenalfc:
    def __init__(self,name,title):
        self.name=name
        self.title=title

    def show(self):
        print(self.name,self.title,self.won,self.year)
        
class fc(arsenalfc):
    def __init__(self,name,title,year,won):
        super().__init__(name,title)
        print(self.name)
        self.year=year
        self.won=won

    def show1(self):
        print(self.name,self.title,self.won,self.year)
        
b=fc("arsenal",6,2015,10)
b.show1()           
c=arsenalfc("amit",5)

b.show()
