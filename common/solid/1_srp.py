from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, type_animal):
        self.type_animal = type_animal

    def live(self):
        print(f"animal {self.type_animal} is live")

    @abstractmethod
    def say(self):
        pass

    def run(self):
        print("animal run")


class Cat(Animal):
    def say(self):
        print("miau")


class Dog(Animal):
    def say(self):
        print("gav")


def make_animal_speak(animal: Animal):
    animal.say()


make_animal_speak(Cat("cat"))
make_animal_speak(Dog("dog"))
