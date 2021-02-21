n=int(input("type any year "))
if((n%4==0 or n%400==0)and (n%100!=0)):
    print("leap year")
else:
    print("0")
