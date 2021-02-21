l=[10,45,645,3,78]
for i in range(0,len(l)):
    x=0
    while x<len(l)-1:
        if l[x]>l[x+1]:
            t=l[x]
            l[x]=l[x+1]
            l[x+1]=t
        x+=1
print(l)
