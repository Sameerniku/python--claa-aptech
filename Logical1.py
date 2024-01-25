''''''
'''
Logical "and"

Exp1    Exp2    and
-------------------
 T      T       T
 F      T       F
 T      F       F
 F      F       F
 
 IF BOTH THE EXPRESSIONS ARE TRUE THEN ONLY THE RESULT WILL BE "TRUE",
  OTHERWISE "FALSE".
 
 Logical "or"
--------------
Exp1    Exp2    or
-------------------
 T      T       T
 F      T       T
 T      F       T
 F      F       F
 
 IF BOTH THE EXPRESSIONS ARE False THEN ONLY THE RESULT WILL BE "False",
  OTHERWISE "TRUE".
 
 Logical "or"
 ------------
 Exp     or
 ----------
 T      F
 F      T
 
 
 
'''

a = int(input('Enter 1st no:'))
b = int(input('Enter 2nd no:'))
c = int(input('Enter 3rd no:'))

res = (a > b)  and (a > c)
print('AND Result = ',res)

res = (a > b)  or (a > c)
print('OR Result = ',res)

res = not((a > b)  or (a > c))
print('NOT of OR Result = ',res)



