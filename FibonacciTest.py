def Fibonacci(x): 
    if x<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif x==0: 
        return 0
    # Second Fibonacci number is 1 
    elif x==1: 
        return 1
    else: 
        return Fibonacci(x-1)+Fibonacci(x-2) 
  
# Driver Program 
x = int(input('What number do you want to apply fibonacci to?'))

print(Fibonacci(x)) 
