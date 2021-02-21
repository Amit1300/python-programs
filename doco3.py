def hello_decorator(func): 
    def inner1(x,y): 
          
        print("before Execution") 
          
        # getting the returned value
        x=func(6,8)
        returned_value = func(4,5) 
        print("after Execution") 
          
        # returning the value to the original frame 
        return returned_value +x
    
          
    return inner1 
  
  
# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b): 
    print("Inside the function") 
    return a + b 
  
a, b = 1, 2
  
# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b)) 
