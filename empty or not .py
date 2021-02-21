l=[]
if not l:
    print("empty")



l1=[10,20,40,40,50]
l2=[9,20,40,40,50]
t=0
for i in range(0,4):
    if l1[i]==l2[i]:
        print(i)
        t=1
        break;
if t==1:
    print("same")
else:
    print("not")







