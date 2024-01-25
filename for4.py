n = int(input('Enter the height:'))
for i in range(n+1):
    for j in range(i):
        print(j+1, end=' ')
    print()

for i in range(n-1,0,-1):
    for j in range(i):
        print(j+1,end=' ')
    print()

print('End of prog.')