a = int(input('enter a number n :'))

def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact*n
        n = n-1
    return fact
print(factorial(a))