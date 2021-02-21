# assignment 1 remaining parts
#How to access private members in Child class?

class A:
    __y=34
    def __init__(self):
        self.__x=10

    def __show(self):
        print("AMIT NAGAR")

b=A()
print(b._A__y)
print(b._A__show())


