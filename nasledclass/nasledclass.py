class Car:
    price = 1000000

    def horse_powers(self):
        return 100  
class Nissan(Car):
    def __init__(self):
        super().__init__() 
        self.price = 2000000  

    def horse_powers(self):
        return 200 

class Kia(Car):
    def __init__(self):
        super().__init__()  
        self.price = 3000000  

    def horse_powers(self):
        return 300  
