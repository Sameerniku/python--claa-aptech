''''''
'''
 Static Method
 -------------
 - Static methods are the methods which perform operations on external data.
 
 - External data means excess data which are not associated with the class
   or object.

 - It can also perform operations on class data.
 
 - There is no need to pass object or class reference with in static method.
 
 - We can call the static method with the help of class name.
 
 - We can Create the static method is by using a decorator 
   called "@staticmethod"  
'''
class Bank:
    bank_name='SBI'      # static variables
    rate_of_int = 11.5   #   "      "

    @staticmethod
    def simple_interest(p,n):
        si = (p * n * Bank.rate_of_int)/100
        print('Simple Interest : ',si)

p1 = float(input('Enter the Principal Amt:'))
n1 = int (input('Enter the no.of Years:'))

Bank.simple_interest(p1,n1)





