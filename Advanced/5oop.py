class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Car:
    def horn(self):
        print("honk")
animals = [Dog(), Cat(), Car()]

for animal in animals:
    getattr(animal, 'speak', animal.speak)() if hasattr(animal, 'speak') else animal.horn()
    print(getattr(animal, 'alive', animal.alive) if hasattr(animal, 'alive') else False)