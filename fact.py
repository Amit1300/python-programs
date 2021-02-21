n=int(input("enter any number"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)

#function
def factorial(n): 
      
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  
# Driver Code 
num = 5; 
print("Factorial of",num,"is", 
factorial(num)) 
