def check(n):
    if n<=17:
        return (17-n)
    else:
         return (n-17)*2
print(check(50))



def g(n):
    if n>100 and n<1000:
        print("exist")

g(7)


def sum1(x,y,z):
    sum=x+y+z
    if x==y==z:
        return sum*3
    return sum
print(sum1(4,56,6))
