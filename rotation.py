a=[3,5,7,9]
b=[]
store=a[0]
c=a[1]
print(store)
for i in range (len(a)-2):
    a[i]=a[i+2]
    b.append(a[i])
print(b)
b.append(store)
b.append(c)
print(b)
