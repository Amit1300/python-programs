
l1=[10,20,30,50]
l2=[20,50,30,10]
l3=[]
for n in l1:
    for m in l2:
        if m==n:
            l3.append(1)
            

if (0 not in l3) and (len(l3)==4):
    print(" same")
else:
    print(' not same')
        
