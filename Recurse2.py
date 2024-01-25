# Factorial of a num by using recursion

n = int(input('Enter a no:'))

def fact(n):
    if n==0:
        return 1
    else:
        return  n * fact(n-1)

result = fact(n)
print(f"Factorial of {n} is {result}")
