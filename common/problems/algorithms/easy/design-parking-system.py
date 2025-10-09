from collections import defaultdict


class ParkingSystem:
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """

        self.counter = defaultdict(int)
        self.mapping_limit = {3: small, 2: medium, 1: big}

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType not in self.counter:
            self.counter[carType] = 1

        if self.counter[carType] <= self.mapping_limit[carType]:
            self.counter[carType] += 1
        else:
            return False

        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

parking_system = ParkingSystem(1, 1, 0)
print(parking_system.addCar(1))
print(parking_system.addCar(2))
print(parking_system.addCar(3))
print(parking_system.addCar(1))


# class ParkingSystem:
#     def __init__(self, big, medium, small):
#         self.slots = {1: big, 2: medium, 3: small}
#
#     def addCar(self, carType):
#         if self.slots.get(carType, 0) > 0:
#             self.slots[carType] -= 1
#             return True
#         return False
