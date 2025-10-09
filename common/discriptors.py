class ValidateAge:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Возраст должен быть между 0 и 100 годами")
        setattr(instance, self.private_name, value)


class Person:
    age = ValidateAge()

    def __init__(self, name, age):
        self.name = name
        self.age = age


try:
    p = Person("Kolya", 30)  # валидный возраст
    print(p.age)
    p.age = -5  # невалидный возраст, будет вызвано исключение ValueError
except ValueError as e:
    print(e)


class Descriptor:
    def __get__(self, instance, owner):
        print(f"self = {self}")
        print(f"instance = {instance}")
        print(f"owner = {owner}")
        return "descriptor value"


class MyClass:
    attr = Descriptor()


obj = MyClass()
print(obj.attr)  # Доступ через экземпляр
print(MyClass.attr)  # Доступ через класс


class Validatename:
    private_name = None

    def __set_name__(self, owner, name):
        print("name")
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        print("et")
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        print("set")
        if len(value) > 10:
            raise ValueError("Name is long")
        setattr(instance, self.private_name, value)


class Money:
    def __init__(self, amount, currency="USD"):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.amount = amount
        self.currency = currency


class Product:
    def __init__(self, product_id, name, price: Money):
        self.id = product_id
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return Money(
            self.product.price.amount * self.quantity, self.product.price.currency
        )


class Order:
    customer_name = Validatename()

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.status = "NEW"

    def add_item(self, product: Product, quantity: int):
        self.items.append(OrderItem(product, quantity))

    def total_price(self):
        total = sum(item.total_price().amount for item in self.items)
        return Money(total)

    def complete(self):
        if not self.items:
            raise ValueError("Order must have at least one item")
        self.status = "COMPLETED"


laptop = Product(1, "Asus", Money(1000))
wheels = Product(2, "Cube", Money(500))
order = Order("Al")
order.add_item(laptop, 1)
order.add_item(wheels, 3)
print(order.total_price().currency)
print(order.total_price().amount)

import time


class CachedAttribute:
    def __init__(self, method):
        self.method = method
        self.cache = {}

    def __get__(self, instance, owner):
        print(instance, owner)
        if instance not in self.cache:
            self.cache[instance] = self.method(instance)
        return self.cache[instance]


class HeavyComputation:
    @CachedAttribute
    def compute(self):
        time.sleep(2)
        return "Результат вычисления"


hc = HeavyComputation()
start_time = time.time()
print(hc.compute)
print(f"Выполнено за {time.time() - start_time} секунд")

start_time = time.time()
print(hc.compute)
print(f"Выполнено за {time.time() - start_time} секунд")


class LoggedAttribute:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        print(f"Установка {self.private_name} в {value}")
        setattr(instance, self.private_name, value)


class User:
    name = LoggedAttribute()
    age = LoggedAttribute()

    def __init__(self, name, age):
        self.name = name
        self.age = age


u = User("Katya", 30)
u.name = "Katyuha"  # Логируется изменение
u.age = 31  # Логируется изменение


class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __get__(self, instance, owner):
        if self.instance is None:
            self.instance = self.cls()
        return self.instance


class Database:
    def __init__(self):
        print("Создание базы данных")


# применение дескриптора Singleton
class AppConfig:
    db = Singleton(Database)


# тестирование паттерна Singleton
config1 = AppConfig()
config2 = AppConfig()
config3 = AppConfig()
db1 = config1.db  # создание БД
db2 = config2.db  # не создает новый экземпляр, использует существующий
db3 = config3.db  # не создает новый экземпляр, использует существующий

print(db1 is db2)  # выведет True, подтверждая, что db1 и db2 - один и тот


# же объект


class VehicleFactory:
    def __init__(self, cls):
        self.cls = cls

    def __get__(self, instance, owner):
        # Возвращаем функцию, которая умеет создавать объект с аргументами
        def creator(*args, **kwargs):
            return self.cls(*args, **kwargs)

        return creator


class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f"Вождение автомобиля модели {self.model}")


class Bike:
    def __init__(self, color):
        self.color = color

    def ride(self):
        print(f"Езда на велосипеде цвета {self.color}")


class AppConfigCar:
    vehicle = VehicleFactory(Car)


class AppConfigBike:
    vehicle = VehicleFactory(Bike)


car_config = AppConfigCar()
car = car_config.vehicle("Tesla Model S")
car.drive()

bike_config = AppConfigBike()
bike = bike_config.vehicle("красный")
bike.ride()


class Item:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price is bad")
        self._price = value


i = Item(8)
# i.price = -8
