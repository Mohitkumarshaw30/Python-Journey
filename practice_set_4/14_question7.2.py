# Write a function safe_divide(a, b) that returns the result of a / b , but
# returns "Cannot divide by zero" if b is 0 .

def safe_divide(a,b):
    if(b==0):
        print("Cannot divide by zero")
    return a/b

res = safe_divide(20,10)
print(res)
