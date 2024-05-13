class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 100


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1200000
        self.vehicle_type = "Nissan"

    def horse_powers(self):
        return 150


nissan = Nissan()
print(nissan.vehicle_type)
print(nissan.price)

