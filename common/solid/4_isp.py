from abc import ABC, abstractmethod


class RunAnimal(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError


class SayAnimal(ABC):
    @abstractmethod
    def say(self):
        raise NotImplementedError


class Animal(ABC):
    def __init__(self, type_animal):
        self.type_animal = type_animal

    def live(self):
        return f"animal {self.type_animal} is live"


class Cat(Animal, SayAnimal):
    def say(self):
        return "cat say miau"


class Dog(Animal, SayAnimal):
    def say(self):
        return "dog say gav"


class Fish(Animal):
    pass


def make_animal_speak(animal: Animal | SayAnimal):
    return animal.say()


def animal_is_live(animal: Animal):
    return animal.live()


print(make_animal_speak(Cat("cat")))
print(make_animal_speak(Dog("dog")))
print(animal_is_live(Fish("fish")))
