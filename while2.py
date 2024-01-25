# Factorial of a given no
'''
n = int(input('Enter a no:'))
f=1
while n>0:
    f = f * n
    n-=1

print('Factorial = ',f)
'''

# Prime no. checking
n = int(input('Enter a no:'))
i = 2
k = 0
while i<= n/2:
    if n % i == 0:
        k+=1
    i+=1

if k==0:
    print('Prime no')
else:
    print('Not a prime no :')



