class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        wheel_str = ', '.join(str(wheel.size) for wheel in self.wheels)
        return f"My {self.make} {self.model} makes {self.engine.horse_power} with wheel size of {wheel_str}"


car = Car("Ford", "Mustang", 500, 22)

print(car.display_car())