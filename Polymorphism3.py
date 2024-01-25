# Polymorphism incase of Inheritance
class Vehicle:
    def __init__(self,name,color,price):
        self.name  = name
        self.color = color
        self.price = price
    def get_details(self):
        print('Name:',self.name)
        print('Color:', self.color)
        print('Price:', self.price)
    def max_speed(self):
        print("Max. speed limit : 100km/h")

    def gear(self):
        print('No.of gears : 5')

class Car(Vehicle):
    def max_speed(self):
        print('Max speed limit : 140 km/h')
    def gear(self):
        print('No.of gears : 7')

v1 = Vehicle("Maruti","Red","750000")
c1 = Car("BMW","White","50000000")

v1.get_details()
c1.get_details()
print('\n')
print('Max speed of v1 : ',v1.max_speed())
print('Max speed of c1 : ',c1.max_speed())

print('\n')
print('Max gear of v1 : ')
v1.gear()
print('Max gear of c1 : ')
c1.gear()



