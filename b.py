for i in range(1,6):
    for j in range(1,6):
        if j==6-i or i==5:
            print("*",end="")
        else:
            print(" ",end="")
    for l in range(1,i):
        if l==i-1 or i==5:
             print("*",end="")
        else:
             print(" ",end="")

    print()
        
     
