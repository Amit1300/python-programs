a=[12,4,56,7,7,7,7,7,7,7,75,5,5,5,75333,1,45,66,67]
l=[]
for x in a:
    if x not in l:
        l.append(x)
        k=set(a)
print(l)
print(k)



def common(list1,list2):
    for i in list1:
        t=0
        for j in list2:
            if i==j:
                t=1
                break;
    if t==1:
        print("true")
    else:
        print("false")
x=common([1,4,5],[1,5])
print(x)
        
