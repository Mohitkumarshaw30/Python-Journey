# Write a recursive function fibonacci(n) that prints the first n Fibonacci
# numbers.

def fibonaci(n):
    if(n==0):
        return 0 
    if(n==1):
        return 1
    
    return fibonaci(n-2)+fibonaci(n-1)

for i in range(7):
    print(fibonaci(i))
