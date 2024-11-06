from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("You stop the motorcycle")


class Boat(Vehicle):
    def go(self):
        print("You sail a boat")
    def stop(self):
        print("You anchor the boat")


vehicle = Car()
vehicle.go()
vehicle.stop()

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()

boat = Boat()
boat.go()
boat.stop()