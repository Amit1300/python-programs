k=1
for i in range(1,6):
    for j in range(5,i):
        print("*",end="")        
    for  k in range(1,i+1):
        if k==i+1:
            print("*",end="")
        else:
            print(" ",end="")
    for l in range(1,i):
            if l==i-1:
                print("*",end="")
            else:
                print(" ",end="")
    print()
