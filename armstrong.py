x=153 
temp=x 
sum1=0
while (temp!=0): 
    r = temp%10
    sum1 = sum1 + r**3
    temp = temp//10
if (sum1==x):
    print("number is armstrong")

print()

   
