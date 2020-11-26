class Car:

    DISCOUNT = 0.10

    def __init__(self, make, color, price):
        self.make = make
        self.color = color
        self.price = price

    def start_engine(self):
        return f'Vroom! {self.make} is ready to go !'

    def give_discount(self):
        self.price = int(self.price * (1 - self.DISCOUNT))

    @classmethod
    def set_discount(cls, discount):
        cls.DISCOUNT = discount

    @classmethod
    def from_string(cls, car_string):
        make, color, price = car_string.split(',')
        return cls(make, color, int(price))

    @staticmethod
    def is_taxed(state):
        if state in ['Maryland', 'North Carolina', 'Iowa', 'South Dakota']:
            return False
        return True

car_string = 'Kia, Red, 80000'

Car_3 = Car.from_string(car_string)
print(Car_3.make)

car_1 = Car('Mercedes', 'Black', 100000)
car_2 = Car('Tesla', 'Blue', 60000)

Car.set_discount(.15)

print(car_1.make)
print(car_2.make)
print(car_2.price)

print(car_1.start_engine())
print(car_2.start_engine())

print(car_1.price)
car_1.give_discount()
print(car_1.price)

print(Car.DISCOUNT)
print(car_1.DISCOUNT)
print(car_2.DISCOUNT)

print(Car.is_taxed('Ohio'))

