from abc import ABC


class Car(ABC):
    def __init__(self, type_car):
        self.type_car = type_car
        self.properties = {}

    def set_properties(self, color, gear):
        self.properties = {"color": color, "gear": gear}

    def get_properties(self):
        return self.properties


class PetrolCar(Car):
    pass


def find_color_car(color):
    for i in cars:
        if i.properties.get("color") == color:
            print(i.properties)


car = PetrolCar("SUV")
car.set_properties("blue", "manual")

petrol_car_1 = PetrolCar("sedan")
petrol_car_1.set_properties("blue", "automat")

petrol_car_2 = PetrolCar("sedan")
petrol_car_2.set_properties("black", "automat")

cars = [petrol_car_1, petrol_car_2, car]
find_color_car("blue")
print(car.get_properties())
