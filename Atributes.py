class House:
    def __init__(self):
        self.numberOfFloors = 10

house = House()

for floor in range(1, house.numberOfFloors + 1):
    print(f"Текущий этаж равен {floor}")
