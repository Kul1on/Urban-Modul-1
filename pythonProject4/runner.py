# runner.py
class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(speed, (int, float)) or speed < 0:
            raise ValueError("Speed must be a non-negative number.")

        self.name = name
        self.speed = speed

    def walk(self):
        return self.speed * 0.5

    def run(self):
        return self.speed * 2
