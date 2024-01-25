''''''
'''
 Operator Over Loading
 ---------------------
 - We can say when same operator behaves differently depending on the
   input values, then it is called as "Operator Overloading".
 ex:  " + " operator behaves differently in numeric input values and
    String input values.  
        a = 10
        b = 5
        c = a + b # 15
   Incase of Strings:
        s1 = "Good"
        s2 = " Morning"
        s3 = s1 + s2 # Good Morning
        
 - We can assign new meaning to operators and also we can extend 
   the functionality of the operators.
   
 - We can also change the default behaviour of the operator using
   operator-overloading  
   
'''
a = 10
b = 5
print('Sum = ',a+b)

print(a.__add__(b))
print(int.__add__(a,b))

# print(dir(int))

s1 = "Good"
s2 = " Morning"
s3 = s1+s2
# print('s3 = ',s3)
print(s1.__add__(s2))
print(str.__add__(s1,s2))

print('-----------')
print(dir(str))

# x = a + s1 # Error , as type mismatched
# print(x)

