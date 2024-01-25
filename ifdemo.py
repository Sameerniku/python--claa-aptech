''''''
'''
if<condition>:
   --if block statements--

rest of the code..
'''

n = int(input('Enter a no:'))
'''
if n<0:
    n = n * -1

print('Mod value : ',n)
'''

if n % 2 == 0:
    print(n,' is divisible by 2')

if n % 3 == 0:
    print(n,' is divisible by 3')

if n % 5 == 0:
    print(n,' is divisible by 5')

if n % 7 == 0:
    print(n,' is divisible by 7')

print('Rest of the code')