 # Polymorphism Incase of Objects
class Maruti:
    def fuel_type(self):
        print("Petrol- Maruti car")

    def max_speed(self):
        print("Speed of Maruti car - 120Kmh")


class Mahindra:
    def fuel_type(self):
        print("Diesel- Mahindra car")

    def max_speed(self):
        print("Speed of Mahindra car - 140Kmh")

def car_details(obj):   # A general method available outside of all classes
    obj.fuel_type()
    obj.max_speed()

m1 = Maruti()
m2 = Mahindra()

car_details(m1)
print('------------------------')
car_details(m2)





