n = int(input('Enter a no:'))

if n > 0:
    if n> 10:
        if n > 100:
            if n > 1000:
                print(n, ' is >0,10,100 & 1000')
            else:
                print(n, ' is >0,10,100 but < 1000')
        else:
            print(n, ' is >0,10 but <100')
    else:
        print(n, ' is >0 but < 10')
else:
    print(n, ' is  < 0')
