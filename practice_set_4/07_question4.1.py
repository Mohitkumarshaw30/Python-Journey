# Write a recursive function factorial(n) that returns the factorial of a
# number.

def factorial(n):
    if n==0 or n==1:
        return 1
    
    val = n*factorial(n-1)
    return val

print(factorial(5))