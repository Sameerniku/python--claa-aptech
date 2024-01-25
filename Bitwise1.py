''''''
'''
Bitwise operators
-----------------
Bitwise AND(&)
--------------
A   B   &
---------
T   T   T
T   F   F
F   T   F
F   F   F

Bitwise OR(|)
--------------
A   B   |
---------
T   T   T
T   F   T
F   T   T
F   F   F

Bitwise XOR(^)
--------------
A   B   ^
---------
T   T   F
T   F   T
F   T   T
F   F   F

'''
a = int(input('Enter 1st no:'))
b = int(input('Enter 2nd no:'))

print(a,' & ',b,' = ',a&b)

print(a,' | ',b,' = ',a|b)

print(a,' ^ ',b,' = ',a^b)

print(45,' >> ',2,' = ',45>>2)

print(23,' << ',2,' = ',23<<2)

print(' ~(-5) = ',~(-5))