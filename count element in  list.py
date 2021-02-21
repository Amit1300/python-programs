l=[10,10,20,30,10,40]
l2=[]
for i in l:
    if not(i in l2):
        l2.append(i)
c=0        
for n in l2:
    c=0
    for i in range(0,6):
        if n==l[i]:
            c+=1
    print(str(n)+':'+ str(c))
