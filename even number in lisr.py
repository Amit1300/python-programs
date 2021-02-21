a=[10,4,6,5,4,4,4,4,6,6,6,123]
for num in a:
    if num%2==0:
        print(num)
c=0
for c in range(len(a)):
    if c%2==0:
        print(a[c])
    c+=1

