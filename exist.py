#element exist in list
a=[]
n=int(input("enter number of element u want to put in the empty list:"))
for i in range(0,n):
    element=int(input("enter numbers:"))
    a.append(element)
print(a)
m=int(input("enter the number:"))
if m in a:
    print("number is exist:")
else:
    print("number not found:")
    
    
