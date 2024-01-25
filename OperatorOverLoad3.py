# Overloaring ">" operator

class Hotel:
    def __init__(self,name,fare):
        self.name = name
        self.fare = fare
    def __gt__(self, other):
        return self.fare > other.fare

h1 = Hotel('Taj',20000)
h2 = Hotel('Mayfair',10000)
print('Taj is higher than Mayfair ? ',h1>h2)
print('Mayfair is higher than Taj ? ',h2>h1)