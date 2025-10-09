from abc import ABC, abstractmethod


class DiscountCalculator(ABC):
    @abstractmethod
    def get_discount_price(self):
        raise NotImplementedError("Method must realisation")


class DiscShirt(DiscountCalculator):
    def __init__(self, price):
        self.price = price

    def get_discount_price(self):
        return self.price * 0.4


class DiscTshirt(DiscountCalculator):
    def __init__(self, price):
        self.price = price

    def get_discount_price(self):
        return self.price * 0.5


def get_price(item: DiscountCalculator):
    return item.get_discount_price()


print(get_price(DiscTshirt(100)))
print(get_price(DiscShirt(100)))
