


class Cart:
    def __init__(self,bag1,bag2,bag3):
        self.clothes = bag1
        self.electronics = bag2
        self.furniture = bag3
    def __len__(self):
        print('Total no.of items :')
        return len(self.clothes+self.furniture+self.electronics)

c1 = Cart(['T-shirts','Jeans'],['mobile','earphone'],['chairs','Tables'])

print('Length of c1 = ',len(c1)) # Error, as Obj. has no len() method
# When we redefine the len() method of our own then, the method is
# overridden, so no error will arise and a specific o/p will generated.

