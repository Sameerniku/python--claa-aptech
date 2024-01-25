#Armstrong number
n = int(input('Enter a no:'))
n1 = n
sum = 0
while n>0:  #153
    rem = n % 10
    sum = sum + (rem**3)
    n//=10

if n1 == sum:
    print(n1,' is an Armstrong no.')
else:
    print(n1, ' is not an Armstrong no.')










