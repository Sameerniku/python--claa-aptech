''''''
'''
- WAP to withdraw money from  bank ATM according to following conditions:
    i) Balance must not be less than Rs1000/-.
    ii) User account will be blocked for an hour if user puts wrong pin
       for 3 times.
'''

import time
class BalanceExceptionError(Exception):
    pass
class AttemptExceptionError(Exception):
    pass
attempts = 1
def withdraw():
    global attempts
    save_pin = 1234
    balance = 12000
    pin = int(input('Enter the pin:'))
    if pin == save_pin:
        try:
            amt = float(input('Enter amount for withdraw:'))
            temp_balance = balance - amt
            if temp_balance < 1000:
                raise BalanceExceptionError('Insuffecient Balance')
            balance = balance - amt
            print('Remaining balance:',balance)
        except Exception as var:
            print(var)
    else:
        ans = input('Wrong pin, do u want to cont...(y/n):')
        if ans.lower()=='y':
            attempts = attempts + 1
            try:
                if attempts == 4:
                    raise  AttemptExceptionError("Your a/c is blocked for an hour due to wrong pin entry")
            except Exception as var:
                print(var)
                time.sleep(3600)
            else:
                withdraw()

        else:
            print('Thank u, visit again!')
            return

withdraw()


