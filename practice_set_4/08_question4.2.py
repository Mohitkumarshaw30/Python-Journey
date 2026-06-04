# Write a recursive function sum_of_digits(n) that returns the sum of all digits
# of a given number.

def sum_of_digits(n):
    if n==0:
        return 0
    val = n%10
    n = n // 10
    sum = val + sum_of_digits(n)
    return sum

print(sum_of_digits(1237))

