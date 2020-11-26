class Car:

    def __init__(self, make, color, price):
        self.make = make
        self.color = color
        self.price = price

car_1 = Car('Mercedes', 'Black', 100000)
car_2 = Car('Tesla', 'Blue', 60000)

print(car_1.make)
print(car_2.make)
print(car_2.price)

