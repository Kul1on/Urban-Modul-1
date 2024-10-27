# Родительский класс для животных
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

# Родительский класс для растений
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  # По умолчанию несъедобное

# Класс млекопитающих, наследуется от Animal
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс хищников, наследуется от Animal
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс цветков, наследуется от Plant
class Flower(Plant):
    pass  # Цветы по умолчанию несъедобны, дополнительных изменений не требуется

# Класс фруктов, наследуется от Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем съедобность для фруктов

# Пример использования
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Вывод для проверки
print(a1.name)
print(p1.name)

print(a1.alive)  
print(a2.fed)    
a1.eat(p1)       # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)       # Хатико съел Заводной апельсин
print(a1.alive)  # False
print(a2.fed)    # True
