# def my_decorator(func=None, log=True, level="debug"):
#     def out_wrap(f):
#         def inner_wrap(**kwargs):
#             print(log, level)
#             return f(**kwargs)
#
#         return inner_wrap
#
#     if func is not None and callable(func):
#         return out_wrap(func)
#     return out_wrap
#
#
# from functools import wraps
#
#
# class MyDecorator:
#     def __init__(self, **kwargs):
#         self._kwargs = kwargs
#
#     def __call__(self, func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print(f"{self._kwargs} — перед вызовом")
#             return func(*args, **kwargs)
#
#         return wrapper
#
#
# def my_decorator(func=None, **kwargs):
#     if func is not None and callable(func):
#         return MyDecorator()(func)
#     return MyDecorator(**kwargs)
#
#
# @my_decorator
# def a():
#     print("a")
#
#
# @my_decorator()
# def b():
#     print("b")
#
#
# @my_decorator(log=False, level="info")
# def c():
#     print("c")
#
#
# a()
# b()
# c()
#
#
# def buble(li):
#     for i in range(len(li) - 1, 0, -1):
#         swapped = False
#
#         for o in range(i):
#             if li[o + 1] < li[o]:
#                 li[o + 1], li[o] = li[o], li[o + 1]
#                 swapped = True
#         if swapped is None:
#             break
#     return li
#
#
# li = [5, 3, 1]
# print(buble(li))
#
#
# def fact(x):
#     if x <= 1:
#         return 1
#     return x * fact(x - 1)
#
#
# print(fact(3))
#
#
# class Item:
#     def __init__(self, items):
#         self.items = items
#
#     def __getitem__(self, index):
#         print("Вызываем getitem")
#         return self.items[index]
#
#     def __iter__(self):
#         print("Вызываем iter")
#         return iter(self.items)
#
#
# li = [1, 2, 3, 4, 5]
# item = Item(li)
# i = iter(li)
#
# for i in item:
#     print(i)
#
#
# class A:
#     def __getitem__(self, i):
#         if i > 3:
#             raise IndexError
#         return i * 10
#
#
# for x in A():
#     print(x)
#
# h = {4, 1, 24, 14, 11, 3, 7}
# print(h)
#
# print("{0:10} = {1:10}".format("spam", 123.4567))
# print(f"{3.14159:.2f}")
# print(f"{255:x}, {255:o}, {255:b}")
# S = "s,pa,in"
# print(S[2:4])
#
#
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     acc = 0
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target:
#             print(acc)
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#         acc += 1
#     print(acc)
#     return -1
#
#
# print(binary_search([i for i in range(1, 5)], 4))
# import collections
#
# Card = collections.namedtuple("Card", ["rank", "suit"])
# card = Card(1, 5)
# print(card._asdict())
#
#
# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list("JQKA")
#     suits = "spades diamonds clubs hearts".split()
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, position):
#         return self._cards[position]
#
#
# Rec = collections.namedtuple("Rec", ("age", "job"))
# bob = Rec(age=2, job="123456789")
# age, job = bob
#
#
# class F:
#     def __init__(self, *args):
#         self.args = args
#
#     def __str__(self):
#         return f"Возвращаем {' '.join(str(arg) for arg in self.args)}"
#
#
# f = F("123456", "567")
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"Точка с координатами ({self.x}, {self.y})"
#
#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"
#
#
# print(Point(1, 2))  # Точка с координатами (1, 2)
# print(repr(Point(1, 2)))
# print(F())
#
# import json
#
# di = dict(t=1, dd=dict(u=8), r=5, i=0, l=9)
# js = json.dumps(di, ensure_ascii=True, indent=4)
# j = json.loads(js)
# print(type(j))
#
# di = {
#     "u": 7,
#     "p": 9,
#     "r": {
#         "u": 4,
#         "g": {
#             "i": [
#                 {
#                     "g": {
#                         "i": 0,
#                         "e": {"h": 9},
#                     }
#                 }
#             ],
#             "e": {"h": 9},
#         },
#     },
# }
#
#
# def dict_depth(d):
#     if isinstance(d, dict):
#         return 1 + max(dict_depth(v) for v in d.values())
#     elif isinstance(d, list):
#         return 1 + max(dict_depth(v) for v in d)
#     else:
#         return 0
#
#
# print(dict_depth(di))
# import copy
#
# li = [1, 2, 3, [1, 2, 3]]
#
# li_copy = copy.deepcopy(li)
# li_copy[3][0] = 10000
# print(li_copy)
# print(li is li_copy)
#
# [spam, hum] = ["y", "i"]
# print(spam)
# a, c, v, *b = "spa"
# print(a, c, v, b)
#
#
# x = 5
# while c := (1 + x) > 0:
#     print("o", c)
#     x -= 1
#     c += 1
#
#
# def fact(x):
#     if x == 1:
#         return 1
#     return x + fact(x - 1)
#
#
# def sort_buble(arr):
#     for n in range(len(arr) - 1, 0, -1):
#         switch = False
#
#         for i in range(n):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
#                 switch = True
#
#         if not switch:
#             break
#
#     return arr
#
#
# print(sort_buble([5, 3, 2, 1]))
#
## Choice sort
# def find_smaller(arr):
#     smallest_index = 0
#     small = arr[0]
#
#     for i in range(len(arr)):  # 1, len; 0, len -1; [1,2,3], 1,2; 0,1,2
#         if arr[i] < small:
#             small = arr[i]
#             smallest_index = i
#
#     return smallest_index
#
#
# def selection_sort(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         new_arr.append(arr.pop(find_smaller(arr)))
#
#     return new_arr
#
#
# print(find_smaller([9, 9, 9, 9, 99, 4, 5, 6, 7]))
# find_smaller([4, 7, 3, 1])
#
# import collections
# import random
#
# Card = collections.namedtuple("Card", ["rank", "suit"])
#
#
# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list("JQKA")
#     suits = "spades diamonds clubs hearts".split()
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, position):
#         return self._cards[position]
#
#     def __setitem__(self, position, value):
#         self._cards[position] = value
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#
#     @staticmethod
#     def spades_high(card):
#         rank_value = FrenchDeck.ranks.index(card.rank)
#         return rank_value * len(suit_values) + suit_values[card.suit]
#
#     def sort_deck(self):
#         self._cards.sort(key=self.spades_high)
#
#
# suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
#
# deck = FrenchDeck()
# # random.shuffle(deck)
# for card in enumerate(deck):
#     print(card)
# import typing
#
#
# class P:
#     def __init__(self, a):
#         self.a = a
#
#
# p = P(0)
#
#
# def test(message: typing.Any):
#     match message:
#         case P(a=i):
#             print("class P", i)
#         case ["i", [io, oi] as i]:
#             print(io, oi, i)
#         case "rt":
#             print("rt")
#         case _:
#             print("None")
#
#
# test(["i", [1, 2]])
#
#
# class P:
#     def __init__(self, li: list):
#         self.li = li
#
#     def __getitem__(self, item):
#         return self.li[item]
#
#     def __setitem__(self, key, value):
#         self.li[key] = value
#
#     def append(self, v):
#         self.li.append(v)
#
#
# p = P([1, 2, 3, 4, 5])
# p[4] = 7
# p.append(8)
# print([i for i in p])
#
#
# class P:
#     li = []
#
#     def a(self, v):
#         self.li.append(v)
#         return self
#
#     def b(self, v):
#         self.li.append(v)
#         return self
#
#     def __repr__(self):
#         return f"{self.li}"
#
#     def __contains__(self, item):
#         return item in self.li
#
#     def __getitem__(self, item):
#         return self.li[item]
#
#     def __len__(self):
#         return len(self.li)
#
#     def __reversed__(self):
#         return iter(self.li[::-1])
#
#
# p = P()
#
# p.a(1).b(2).a(3)
#
# import array
#
# arr = [i for i in range(18)]
# random.shuffle(arr)
# u = array.array("i", arr)
# y = array.array("i", sorted(arr))
# print(y[-1])
# print(len(u) * u.itemsize)
# import collections
#
# arr = [5, 4, 3, 9, 8, 0]
#
#
# for i in range(1, len(arr)):
#     key = arr[i]
#     j = i - 1
#     while j >= 0 and arr[j] > key:
#         arr[j + 1] = arr[j]
#         j -= 1
#     arr[j + 1] = key
#
# for i in range(len(arr) - 1, -1, -1):
#     swap = False
#     for o in range(i):
#         if arr[o + 1] < arr[o]:
#             arr[o + 1], arr[o] = arr[o], arr[o + 1]
#             swap = True
#
#     if not swap:
#         break
#
#
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for k in range(0, n - 1 - i):
#             if arr[k] > arr[k + 1]:
#                 arr[k], arr[k + 1] = arr[k + 1], arr[k]
#
#
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         gess = (low + high) // 2
#         if arr[gess] == target:
#             return target
#         elif arr[gess] > target:
#             high = gess - 1
#         else:
#             low = gess + 1
#     return -1
#
#
# print(arr)
# bubble_sort(arr)
# print(binary_search(arr, 3))
#
# p = dict(a=8)
# i = dict(g=9)
# i |= p
# print(p | i)
#
#
# def get_creators(record: dict) -> list:
#     match record:
#         case {"type": "book", "api": 2, "authors": [*names]}:
#             return names
#         case {"type": "book", "api": 1, "author": name}:
#             return [name]
#         case {"type": "book"}:
#             raise ValueError(f"Invalid 'book' record: {record!r}")
#         case {"type": "movie", "director": name}:
#             return [name]
#         case _:
#             raise ValueError(f"Invalid record: {record!r}")
#
#
# class HashedObj:
#     def __init__(self):
#         self.data = {}
#
#     def __setitem__(self, key, value):
#         self.data[key] = value
#
#     def __getitem__(self, item):
#         return self.data[item]
#
#     def items(self):
#         return [(k, v) for k, v in self.data.items()]
#
#     def keys(self):
#         return [k for k in self.data.keys()]
#
#
# dic = HashedObj()
# dic[1] = 6
#
# di = {}
#
# print(type(di.setdefault("r", [])))
# dd = collections.defaultdict(list)
# print(dd.get("key"))
# j = dd["key"]
# print(dd)
#
#
# u = collections.Counter()
# u.update("k")
# u.update("k")
# u.update([1, 2, 3, 4, 5])
# u.update([1, 2, 3, 4, 5])
# print(u)
#
#
# class Disc:
#     def __get__(self, instance: dict, owner):
#         instance.update(dict(i=9))
#         print(instance, owner)
#
#
# class StrKeyDict0(collections.UserDict):
#     attr = Disc()
#
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value)
#         print("setitem")
#
#     def __missing__(self, key):
#         if isinstance(key, str):
#             raise KeyError(key)
#         return self[str(key)]
#
#     def get(self, key, default=None):
#         try:
#             return self[key]
#         except KeyError:
#             self[key] = default
#             return default
#
#     def __contains__(self, key):
#         return key in self.keys() or str(key) in self.keys()
#
#
# df = StrKeyDict0()
# df.update(dict(t=9))
# print(df.get(7, 8))
# print(df.attr)
# print(df)
#
# j = {}
# j.setdefault(8)
# print(j)
#
#
# def summ(li: list):
#     if len(li) == 0:
#         return 0
#     else:
#         return li[0] + summ(li[1:])
#
#
# print(summ([1, 2, 3, 34]))
#
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
#
# print(gcd(1680, 640))
# print(1680 % 640)
#
# import functools
# import time
# from dataclasses import dataclass
# from functools import singledispatch
#
#
# def clock(func):
#     @functools.wraps(func)
#     def clocked(*args, **kwargs):
#         t0 = time.perf_counter()
#         result = func(*args, **kwargs)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         arg_lst = [repr(arg) for arg in args]
#         arg_lst.extend(f"{k}={v!r}" for k, v in kwargs.items())
#         arg_str = ", ".join(arg_lst)
#         print(f"[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}")
#         return result
#
#     return clocked
#
#
# @functools.lru_cache(maxsize=2 * 20, typed=True)
# # @functools.cache
# @clock
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 2) + fibonacci(n - 1)
#
#
# print(fibonacci(600))
#
#
# @singledispatch
# def parser(data):
#     raise NotImplementedError("Unsupported type")
#
#
# @dataclass
# class User:
#     name: str
#     age: int
#
#
# @parser.register
# def _(data: User):
#     return {"name": data.name, "age": data.age}
#
#
# user_1 = User("V", 23)
# print(parser(user_1))
# registry = set()
#
#
# def register(active=True):
#     def decorate(func):
#         print(f"running register (active={active})->decorate({func})")
#         if active:
#             registry.add(func)
#         else:
#             registry.discard(func)
#         return func
#
#     return decorate
#
#
# @register(active=False)
# def f1():
#     print("running f1()")
#
#
# @register()
# def f2():
#     print("running f2()")
#
#
# def f3():
#     print("running f3()")
#
#
# DEFAULT_FMT = "[{elapsed:0.8f}s] {name}({args}) -> {result}"
#
#
# def clock(fmt=DEFAULT_FMT):
#     def decorator(func):
#         def clocked(*_args):
#             t0 = time.perf_counter()
#             _result = func(*_args)
#             elapsed = time.perf_counter() - t0
#             name = func.__name__
#             args = ", ".join(repr(arg) for arg in _args)
#             result = repr(_result)
#             print(fmt.format(**locals()))
#             return _result
#
#         return clocked
#
#     return decorator
#
#
# import json
#
#
# def report_to_str(data):
#     return "\n".join(f"{k}: {v}" for k, v in data.items())
#
#
# def report_to_json(data):
#     return json.dumps(data, ensure_ascii=True, indent=4)
#
#
# def get_report(data, reporter):
#     return reporter(data)
#
#
# print(get_report(dict(j=6, n=8), report_to_json))
# import dataclasses
# import json
# from collections.abc import Callable, Sequence
# from decimal import Decimal
# from typing import NamedTuple
#
#
# class Customer(NamedTuple):
#     name: str
#     fidelity: int = 0
#
#
# class LineItem(NamedTuple):
#     product: str
#     quantity: int
#     price: Decimal
#
#     def total(self):
#         return self.price * self.quantity
#
#
# @dataclasses.dataclass
# class Order:
#     customer: Customer
#     cart: Sequence[LineItem]
#     promotion: Callable[["Order"], Decimal] | None = None
#
#     def total(self) -> Decimal:
#         totals = (item.total() for item in self.cart)
#         return sum(totals, start=Decimal(0))
#
#     def due(self) -> Decimal:
#         if self.promotion is None:
#             discount = Decimal(0)
#         else:
#             discount = self.promotion(self)
#         return self.total() - discount
#
#     def __repr__(self):
#         return (
#             f"<Order total: {self.total():.2f} "
#             f"due: {self.due():.2f} "
#             f"discount: {100 - ((self.due() * 100) / self.total()):.2f} >"
#         )
#
#
# Promotion = Callable[[Order], Decimal]
# promos: list[Promotion] = []
#
#
# # promos = [promo for name, promo in globals().items() if name.endswith('_promo') and name != 'best_promo']
# def promotion(promo: Promotion):
#     promos.append(promo)
#     return promo
#
#
# @promotion
# def fidelity_promo(order: Order) -> Decimal:
#     """5%-ная скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""
#     if order.customer.fidelity >= 1000:
#         return order.total() * Decimal("0.05")
#     return Decimal(0)
#
#
# @promotion
# def bulk_item_promo(order: Order) -> Decimal:
#     """10%-ная скидка для каждой позиции LineItem, в которой заказано
#     не менее 20 единиц"""
#     discount = Decimal(0)
#     for item in order.cart:
#         if item.quantity >= 20:
#             discount += item.total() * Decimal(0.1)
#     return discount
#
#
# @promotion
# def large_order_promo(order: Order) -> Decimal:
#     """7%-ная скидка для заказов, включающих не менее 10 различных позиций"""
#     distinct_items = {item.product for item in order.cart}
#     if len(distinct_items) >= 10:
#         return order.total() * Decimal("0.07")
#     return Decimal(0)
#
#
# def best_promo(order: Order) -> Decimal:
#     return max(promo(order) for promo in promos)
#
#
# anna = Customer("Ann", 1000)
# nil = Customer("Nil", 1001)
# brad = Customer("Brad")
# cart_anna = [LineItem(f"banana_{i}", 20, Decimal(15)) for i in range(4)]
# cart_nil = [LineItem("coconut", 10, Decimal(10))]
# cart_brad = [LineItem("car", 20, Decimal(5))]
#
# print(Order(anna, cart_anna, best_promo))
# print(Order(nil, cart_nil, best_promo))
# print(Order(brad, cart_brad, best_promo))
# from __future__ import annotations
#
# from abc import ABC, abstractmethod
#
#
# class Command(ABC):
#     """
#     Интерфейс Команды объявляет метод для выполнения команд.
#     """
#
#     @abstractmethod
#     def execute(self) -> None:
#         pass
#
#
# class SimpleCommand(Command):
#     """
#     Некоторые команды способны выполнять простые операции самостоятельно.
#     """
#
#     def __init__(self, payload: str) -> None:
#         self._payload = payload
#
#     def execute(self) -> None:
#         print(
#             f"SimpleCommand: See, I can do simple things like printing({self._payload})"
#         )
#
#
# class ComplexCommand(Command):
#     """
#     Но есть и команды, которые делегируют более сложные операции другим
#     объектам, называемым «получателями».
#     """
#
#     def __init__(self, receiver: Receiver, a: str, b: str) -> None:
#         """
#         Сложные команды могут принимать один или несколько объектов-получателей
#         вместе с любыми данными о контексте через конструктор.
#         """
#
#         self._receiver = receiver
#         self._a = a
#         self._b = b
#
#     def execute(self) -> None:
#         """
#         Команды могут делегировать выполнение любым методам получателя.
#         """
#
#         print(
#             "ComplexCommand: Complex stuff should be done by a receiver object", end=""
#         )
#         self._receiver.do_something(self._a)
#         self._receiver.do_something_else(self._b)
#
#
# class Receiver:
#     """
#     Классы Получателей содержат некую важную бизнес-логику. Они умеют выполнять
#     все виды операций, связанных с выполнением запроса. Фактически, любой класс
#     может выступать Получателем.
#     """
#
#     def do_something(self, a: str) -> None:
#         print(f"\nReceiver: Working on ({a}.)", end="")
#
#     def do_something_else(self, b: str) -> None:
#         print(f"\nReceiver: Also working on ({b}.)", end="")
#
#
# class Invoker:
#     """
#     Отправитель связан с одной или несколькими командами. Он отправляет запрос
#     команде.
#     """
#
#     _on_start = None
#     _on_finish = None
#
#     """
#     Инициализация команд.
#     """
#
#     def set_on_start(self, command: Command):
#         self._on_start = command
#
#     def set_on_finish(self, command: Command):
#         self._on_finish = command
#
#     def do_something_important(self) -> None:
#         """
#         Отправитель не зависит от классов конкретных команд и получателей.
#         Отправитель передаёт запрос получателю косвенно, выполняя команду.
#         """
#
#         print("Invoker: Does anybody want something done before I begin?")
#         if isinstance(self._on_start, Command):
#             self._on_start.execute()
#
#         print("Invoker: ...doing something really important...")
#
#         print("Invoker: Does anybody want something done after I finish?")
#         if isinstance(self._on_finish, Command):
#             self._on_finish.execute()
#
#
# if __name__ == "__main__":
#     """
#     Клиентский код может параметризовать отправителя любыми командами.
#     """
#
#     invoker = Invoker()
#     invoker.set_on_start(SimpleCommand("Say Hi!"))
#     receiver = Receiver()
#
#     invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))
#
#     invoker.do_something_important()
# from abc import ABC, abstractmethod
#
#
# class Command(ABC):
#     @abstractmethod
#     def execute(self):
#         raise NotImplementedError
#
#
# class CreateItemCommand(Command):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def execute(self):
#         print(f"Create {self.name}, {self.age}")
#
#     def __repr__(self):
#         return f"CreateItemCommand {self.name, self.age}"
#
#
# class DeleteItemCommand(Command):
#     def __init__(self, name):
#         self.name = name
#
#     def execute(self):
#         print(f"Delete {self.name}")
#
#     def __repr__(self):
#         return f"DeleteItemCommand {self.name}"
#
#
# class Invoker:
#     def __init__(self):
#         self.storage = []
#
#     def get_storage(self):
#         li = []
#         for i in self.storage:
#             li.append(i)
#         return li
#
#     def storage_execute(self, command: Command):
#         self.storage.append(command)
#         command.execute()
#
#
# invoker = Invoker()
# cmd_add = CreateItemCommand("v", 67)
# invoker.storage_execute(cmd_add)
# cmd_del = DeleteItemCommand("v")
# invoker.storage_execute(cmd_del)
# print("вся история", invoker.get_storage())
# import math
# from array import array
#
#
# class Vector2d:
#     typecode = "d"
#     __match_args__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.__x = float(x)
#         self.__y = float(y)
#
#     @property
#     def x(self):
#         return self.__x
#
#     @property
#     def y(self):
#         return self.__y
#
#     def __iter__(self):
#         return (i for i in (self.x, self.y))
#
#     def __repr__(self):
#         class_name = type(self).__name__
#         return "{}({!r}, {!r})".format(class_name, *self)
#
#     def __str__(self):
#         return str(tuple(self))
#
#     def __bytes__(self):
#         return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))
#
#     def __eq__(self, other):
#         if isinstance(other, Vector2d):
#             return tuple(self) == tuple(other)
#         return NotImplemented
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#     def __abs__(self):
#         return math.hypot(self.x, self.y)
#
#     def __bool__(self):
#         return bool(abs(self))
#
#     @classmethod
#     def frombytes(cls, octets):
#         typecode = chr(octets[0])
#         memv = memoryview(octets[1:]).cast(typecode)
#         return cls(*memv)
#
#     def __format__(self, fmt_spec=""):
#         if fmt_spec.endswith("p"):
#             fmt_spec = fmt_spec[:-1]
#             coords = (abs(self), self.angle())
#             outer_fmt = "<{}, {}>"
#         else:
#             coords = self
#             outer_fmt = "({}, {})"
#         components = (format(c, fmt_spec) for c in coords)
#         return outer_fmt.format(*components)
#
#     def angle(self):
#         return math.atan2(self.y, self.x)
#
#
# v = Vector2d(9, 4)
#
#
# def positional_pattern_demo(v: Vector2d) -> None:
#     match v:
#         case Vector2d(a, b):
#             print(f"{a, b}")
#         case Vector2d(0, 0):
#             print(f"{v!r} is null")
#         case Vector2d(0):
#             print(f"{v!r} is vertical")
#         case Vector2d(_, 0):
#             print(f"{v!r} is horizontal")
#         case Vector2d(x, y) if x == y:
#             print(f"{v!r} is diagonal")
#         case _:
#             print(f"{v!r} is awesome")
#
#
# positional_pattern_demo(v)
#
#
# my_list = [(10, 20), (30, 40), (50, 60)]
#
#
# def g(li: list[tuple[int, int]]) -> int:
#     return sum(sub[1] for sub in li)
#
#
# print(g(my_list))
# print("".isidentifier())
#
#
# class Root:
#     def ping(self):
#         print(f"{self}.ping() in Root")
#
#     def pong(self):
#         print(f"{self}.pong() in Root")
#
#     def __repr__(self):
#         cls_name = type(self).__name__
#         return f"<instance of {cls_name}>"
#
#
# class A(Root):
#     def ping(self):
#         print(f"{self}.ping() in A")
#         super().ping()
#
#     def pong(self):
#         print(f"{self}.pong() in A")
#         super().pong()
#
#
# class B(Root):
#     def ping(self):
#         print(f"{self}.ping() in B")
#         super().ping()
#
#     def pong(self):
#         print(f"{self}.pong() in B")
#
#
# class Leaf(B, A):
#     def ping(self):
#         print(f"{self}.ping() in Leaf")
#         super().ping()
#
#
# class U:
#     def ping(self):
#         print(f"{self}.ping() in U")
#         super().ping()
#
#
# class LeafUA(U, A):
#     def ping(self):
#         print(f"{self}.ping() in LeafUA")
#         super().ping()
#
#
# u = U()
# l = LeafUA()
# # print(u.ping())
# print(l.ping())
#
# import functools
# import itertools
# import operator
# import reprlib
# from array import array
#
#
# class Vector:
#     typecode = "d"
#     __match_args__ = ("x", "y", "z", "t")
#
#     def __init__(self, components):
#         """Инициализирует вектор, создавая массив компонентов из переданного итерируемого объекта."""
#         self._components = array(self.typecode, components)
#
#     def __len__(self):
#         """Возвращает количество компонентов вектора."""
#         return len(self._components)
#
#     def __getitem__(self, key):
#         """Возвращает элемент по индексу или новый вектор при срезе."""
#         if isinstance(key, slice):
#             cls = type(self)
#             return cls(self._components[key])
#         index = operator.index(key)
#         return self._components[index]
#
#     def __iter__(self):
#         """Возвращает итератор по компонентам вектора."""
#         return iter(self._components)
#
#     def __repr__(self):
#         """Возвращает строковое представление для отладчика."""
#         components = reprlib.repr(self._components)
#         print(type(components))
#         components = components[components.find("[") : -1]
#         return f"Vector({components})"
#
#     def __str__(self):
#         """Возвращает строковое представление в виде кортежа."""
#         return str(tuple(self))
#
#     def __bytes__(self):
#         """Возвращает байтовое представление вектора."""
#         return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))
#
#     def __eq__(self, other):
#         """Сравнивает два вектора на равенство поэлементно."""
#         if isinstance(other, Vector):
#             return len(self) == len(other) and all(
#                 a == b for a, b in zip(self, other, strict=False)
#             )
#         else:
#             return NotImplemented
#
#     def __hash__(self):
#         """Вычисляет хеш вектора, используя XOR для компонент."""
#         hashes = map(hash, self._components)
#         return functools.reduce(operator.xor, hashes)
#
#     def __abs__(self):
#         """Вычисляет длину вектора (евклидова норма)."""
#         return math.hypot(*self)
#
#     def __bool__(self):
#         """Возвращает True, если длина вектора ненулевая."""
#         return bool(abs(self))
#
#     def __neg__(self):
#         return Vector(-x for x in self)
#
#     def __pos__(self):
#         return -Vector(self)
#
#     def __getattr__(self, name):
#         """Позволяет доступ к компонентам по именам (например, x, y)."""
#         cls = type(self)
#         try:
#             pos = cls.__match_args__.index(name)
#         except ValueError:
#             pos = -1
#         if 0 <= pos < len(self._components):
#             return self._components[pos]
#         msg = f"{cls.__name__!r} object has no attribute {name!r}"
#         raise AttributeError(msg)
#
#     def __setattr__(self, name, value):
#         """Запрещает изменение компонент через односимвольные атрибуты."""
#         cls = type(self)
#
#         if len(name) == 1:
#             if name in cls.__match_args__:
#                 error = "readonly attribute {attr_name!r}"
#             elif name.islower():
#                 error = "can't set attributes 'a' to 'z' in {cls_name!r}"
#             else:
#                 error = ""
#             if error:
#                 msg = error.format(cls_name=cls.__name__, attr_name=name)
#                 raise AttributeError(msg)
#         super().__setattr__(name, value)
#
#     @classmethod
#     def frombytes(cls, octets):
#         """Создаёт новый вектор из байтового представления."""
#         typecode = chr(octets[0])
#         memv = memoryview(octets[1:]).cast(typecode)
#         return cls(*memv)
#
#     # def __add__(self, other):
#     #     """Простыми методами решение проблемы складывания векторов"""
#     #     max_len = max(len(self), len(other))
#     #     return Vector((self[i] if i < len(self) else 0) +
#     #                   (other[i] if i < len(other) else 0) for i in range(max_len))
#     def __add__(self, other):
#         try:
#             pairs = itertools.zip_longest(self, other, fillvalue=0.0)
#             return Vector(a + b for a, b in pairs)
#         except TypeError:
#             return NotImplemented
#
#     def __radd__(self, other):
#         return self + other
#
#     def __mul__(self, other):
#         try:
#             scalar = float(other)
#         except TypeError:
#             return NotImplemented
#         return Vector(i * scalar for i in self)
#
#     def __rmul__(self, other):
#         return self * other
#
#     def __matmul__(self, other):
#         try:
#             return sum(a * b for a, b in zip(self, other, strict=True))
#         except ValueError:
#             return ValueError
#
#     def __rmatmul__(self, other):
#         return self @ other
#
#
# v = Vector(range(1, 3))
# v2 = Vector(range(1, 3))
# print(v != v2)
#
# import random
#
#
# class BingoCage:
#     def __init__(self, items):
#         self._randomizer = random.SystemRandom()
#         self._items = []
#         self.load(items)
#
#     def load(self, items):
#         self._items.extend(items)
#         self._randomizer.shuffle(self._items)
#
#     def pick(self):
#         try:
#             return self._items.pop()
#
#         except IndexError:
#             raise LookupError("pick from empty BingoCage")
#
#
# def __call__(self):
#     self.pick()
#
#
# import random
# import re
#
# RE_WORD = re.compile(r"\w+")
#
#
# class Sentence:
#     def __init__(self, text):
#         self.text = text
#         self.words = RE_WORD.findall(text)
#
#     def __getitem__(self, index):
#         return self.words[index]
#
#     def __len__(self):
#         return len(self.words)
#
#     def __repr__(self):
#         return "Sentence(%s)"
#
#     def __iter__(self):
#         li = []
#         for word in self.words:
#             yield word
#             li.append(word * 2)
#
#
# s = Sentence('"The time has come," the Walrus said,')
#
#
# class ArithmeticProgression:
#     def __init__(self, begin, step, end=None):
#         self.begin = begin
#         self.step = step
#         self.end = end  # None -> "бесконечный" ряд
#
#     def __iter__(self):
#         result_type = type(self.begin + self.step)
#         result = result_type(self.begin)
#         forever = self.end is None
#         index = 0
#         while forever or result < self.end:
#             yield result
#             index += 1
#             result = self.begin + self.step * index
#
#
# ap = ArithmeticProgression(0, 1, 6)
# print(list(ap))
# import os
# from pprint import PrettyPrinter
#
# data = list(os.walk("./common/"))
# pp = PrettyPrinter(indent=4, width=60)
# pp.pprint(data[3][2])
#
#
# def sub_gen():
#     yield 1.1
#     yield 1.2
#     return "Done!"
#
#
# def gen():
#     yield 1
#     result = yield from sub_gen()
#     print("<--", result)
#     yield 2
#
#
# for x in gen():
#     print(x)
#
#
# def chain(*iterable):
#     for it in iterable:
#         yield from it
#
#
# def chain(*iterables):
#     for it in iterables:
#         for i in it:
#             yield i
#
#
# print(list(chain([1, 2, 3], "tyu")))
#
#
# def make_avg():
#     total = 0
#     count = 0
#
#     def avg(new_value):
#         nonlocal total, count
#         count += 1
#         total += new_value
#         return total / count
#
#     return avg
#
#
# avg_func = make_avg()
# avg_func(91)
# print(avg_func(190))
# from collections.abc import Generator
# from typing import NamedTuple, Union
#
#
# class Result(NamedTuple):
#     count: int  # type: ignore
#     average: float
#
#
# class Sentinel:
#     def __repr__(self):
#         return "<Sentinel>"
#
#
# STOP = Sentinel()
# SendType = Union[float, Sentinel]
#
#
# def averager2(verbose: bool = False) -> Generator[None, SendType, Result]:
#     total = 0.0
#     count = 0
#     average = 0.0
#     while True:
#         term = yield average
#         if verbose:
#             print("received:", term)
#         if isinstance(term, Sentinel):
#             break
#         total += term
#         count += 1
#         average = total / count
#     return Result(count, average)
#
#
# coro_avg = averager2(True)
# next(coro_avg)
# coro_avg.send(10)
# coro_avg.send(30)
# coro_avg.send(6.5)
#
# try:
#     coro_avg.send(STOP)
# except StopIteration as exc:
#     result = exc.value
#
# print(result)  # Result(count=3, average=15.5)
# import csv
# from itertools import islice
#
# with open("./common/system.csv", newline="", encoding="utf-8") as f:
#     rows = csv.DictReader(f)
#     print(rows.fieldnames)
#     for row in islice(rows, 5):
#         print(row["\ufeffУровень"])
#
# import asyncio
#
#
# async def one():
#     print("start one")
#     await asyncio.sleep(3)
#     print("end one")
#     return 1
#
#
# async def two():
#     print("start two")
#     await asyncio.sleep(2)
#     print("end two")
#     return 2
#
#
# async def three():
#     print("start three")
#     await asyncio.sleep(1)
#     print("end three")
#     return 3
#
#
# async def main():
#     tasks = [
#         asyncio.create_task(one()),
#         asyncio.create_task(two()),
#         asyncio.create_task(three()),
#     ]
#     done, pending = await asyncio.wait(tasks)
#     for i in done:
#         print(i.result())
#
#     print("Все завершены!")
#
#
# asyncio.run(main())
# from threading import Event, Thread
#
#
# def spin(msg: str, done: Event) -> None:
#     for char in itertools.cycle(r"\|/-"):
#         status = f"\r{char} {msg}"
#         print(status, flush=True, end="")
#         if done.wait(0.1):
#             break
#     blanks = " " * len(status)
#     print(f"\r{blanks}\r", end="")
#
#
# def slow(n) -> int:
#     time.sleep(n)
#     return 42
#
#
# def supervisor():
#     done = Event()
#     spinner = Thread(target=spin, args=("thinking!", done))
#
#     print(spinner.name)
#     print("Запускаем спиннер...")
#     spinner.start()
#     result = slow(1)
#     done.set()  # Сообщаем спиннеру, что нужно остановиться
#     spinner.join()
#     print(f"Готово! Результат: {result}")
#
#
# if __name__ == "__main__":
#     supervisor()
#
# from multiprocessing import Event, Process, synchronize
#
#
# def spin(msg: str, done: synchronize.Event) -> None:
#     for char in itertools.cycle(r"\|/-"):
#         status = f"\r{char} {msg}"
#         print(status, flush=True, end="")
#         if done.wait(0.1):
#             break
#     blanks = " " * len(status)
#     print(f"\r{blanks}\r", end="")
#
#
# def slow(n) -> int:
#     time.sleep(n)
#     return 42
#
#
# def supervisor() -> int:
#     done = Event()
#     spinner = Process(target=spin, args=("thinking!", done))
#     print(f"spinner object: {spinner}")
#     spinner.start()
#     result = slow(2)
#     done.set()
#     spinner.join()
#     return result
#
#
# if __name__ == "__main__":
#     result = supervisor()
#     print(f"Answer: {result}")
# import asyncio
#
#
# async def a(t):
#     print("run a")
#     await asyncio.sleep(t)
#     print("fin a")
#
#
# async def b(t):
#     print("run b")
#     await asyncio.sleep(t)
#     print("fin b")
#
#
# async def main():
#     li = [asyncio.create_task(a(2)), asyncio.create_task(b(1))]
#     await asyncio.wait_for(li)
#     # await asyncio.wait()
#
#
# asyncio.run(main())
# import asyncio
#
# import aiohttp
#
#
# async def spin(msg: str) -> None:
#     for char in itertools.cycle(r"\|/-"):
#         status = f"\r{char} {msg}"
#         print(status, flush=True, end="")
#         try:
#             await asyncio.sleep(0.1)
#         except asyncio.CancelledError:
#             break
#     blanks = " " * len(status)
#     print(f"\r{blanks}\r", end="")
#
#
# async def slow() -> int:
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://httpbin.org/delay/2") as response:
#             data = response.status
#     return data
#
#
# def main() -> None:
#     result = asyncio.run(supervisor())
#     print(f"Answer: {result}")
#
#
# async def supervisor() -> int:
#     spinner = asyncio.create_task(spin("thinking!"))
#     print(f"spinner object: {spinner}")
#     result = await slow()
#     spinner.cancel()
#     return result
#
#
# if __name__ == "__main__":
#     main()
#
# from timer_self import timer_decorator
#
#
# @timer_decorator
# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     root = math.isqrt(n)
#     for i in range(3, root + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# print(is_prime(5_000_111_000_222_021))
# import asyncio
#
#
# def blocking_work():
#     time.sleep(2)
#     print("Готово в потоке!")
#     return "Результат из потока"
#
#
# async def g():
#     await asyncio.sleep(1)
#     print("g")
#
#
# async def main():
#     asyncio.create_task(g())
#     loop = asyncio.get_running_loop()
#     result = await loop.run_in_executor(None, blocking_work)
#     print(f"Получено: {result}")
#
#
# asyncio.run(main())
# import asyncio
#
#
# async def task1():
#     await asyncio.sleep(2)
#     print("Task 1 done")
#     return 1
#
#
# async def task2():
#     await asyncio.sleep(1)
#     print("Task 2 done")
#     return 2
#
#
# async def main():
#     for coro in asyncio.as_completed([task1(), task2()]):
#         result = await coro
#         print(result)
#
#
# asyncio.run(main())
#
# (4.25,)
#
# from time import perf_counter
# from typing import NamedTuple
#
# NUMBERS = [
#     9999999967,
#     9999999943,
#     9999999931,
#     9999999907,
#     9999999883,
#     9999999871,
#     9999999857,
#     9999999833,
#     9999999821,
#     9999999797,
# ]
#
#
# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     root = math.isqrt(n)
#     for i in range(3, root + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# class Result(NamedTuple):
#     prime: bool
#     elapsed: float
#
#
# def check(n: int) -> Result:
#     t0 = perf_counter()
#     prime = is_prime(n)
#     return Result(prime, perf_counter() - t0)
#
#
# def main() -> None:
#     print(f"Checking {len(NUMBERS)} numbers sequentially:")
#     t0 = perf_counter()
#     for n in NUMBERS:
#         prime, elapsed = check(n)
#         label = "P" if prime else " "
#         print(f"{n:16} {label} {elapsed:9.6f}s")
#     elapsed = perf_counter() - t0
#     print(f"Total time: {elapsed:.2f}s")
#
#
# if __name__ == "__main__":
#     main()
# import asyncio
#
#
# def blocking_func(x):
#     print(f"Начали работу: {x}")
#     time.sleep(2)
#     print(f"Завершили работу: {x}")
#     return x * 2
#
#
# async def main():
#     loop = asyncio.get_running_loop()
#
#     # Планируем сразу несколько задач
#     tasks = [
#         loop.run_in_executor(None, blocking_func, 1),
#         loop.run_in_executor(None, blocking_func, 2),
#         loop.run_in_executor(None, blocking_func, 3),
#     ]
#
#     # Дождаться всех сразу
#     results = await asyncio.gather(*tasks)
#     print(f"Результаты: {results}")
#
#
# asyncio.run(main())
# from concurrent.futures import ThreadPoolExecutor, as_completed
#
#
# def cpu_task(n):
#     time.sleep(1)
#     return n * 2
#
#
# tasks = [1, 2, 3, 4, 5]
#
# with ThreadPoolExecutor(max_workers=3) as executor:
#     future_to_task = {executor.submit(cpu_task, n): n for n in tasks}
#
#     for future in as_completed(future_to_task):
#         n = future_to_task[future]  # Получаем аргумент n
#         result = future.result()  # Получаем результат
#         print(f"Задача {n} вернула {result}")
#
#
# class Solution:
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         mapping = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }  # I, X, C
#
#         res = 0
#         le = len(s)
#         for i in range(le):
#             curr = mapping[s[i]]
#             next_val = mapping[s[i + 1]] if i + 1 < le else 0
#
#             if curr < next_val:
#                 res -= curr
#             else:
#                 res += curr
#
#         return res
#
#
# s = "LVIII"
# sol = Solution()
# print(sol.romanToInt(s))
# import concurrent.futures
# import os
# from concurrent.futures import as_completed
#
# img_urls = [
#     "https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg",
#     "https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg",
#     "https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg",
#     "https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg",
#     "https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg",
#     "https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg",
# ]
#
#
# def download_image(img_url):
#     # img_bytes = requests.get(img_url).content
#     print(f"[Process ID]:{os.getpid()} Downloading...")
#
#
# if __name__ == "__main__":
#     t1 = time.time()
#     print("Downloading images with Multiprocess")
#     Process()
#     with concurrent.futures.ThreadPoolExecutor(3) as exe:
#         exe.map(download_image, img_urls)
#         # exe.shutdown(wait=False)
#     t2 = time.time()
#     print(f"Multiprocess Code Took:{t2 - t1} seconds")
#
#     print("other")
# import threading
# import time
#
#
# def background_task():
#     time.sleep(5)
#
#     with open("new_file.txt", "a+") as f:
#         f.write("task complite\n ")
#
#     print("Фоновая задача завершена")
#
#
# # daemon=True — поток умрёт, если main завершится
# t = threading.Thread(target=background_task, daemon=True)
# t.start()
#
# print("Главная программа завершена (поток работает в фоне)")
# import time
# from concurrent.futures import ThreadPoolExecutor, as_completed
#
#
# def task(x):
#     time.sleep(2)
#     return x**x
#
#
# executor = ThreadPoolExecutor()
# futures = [executor.submit(task, i) for i in range(3)]
# executor.shutdown(wait=False)  # ✅ теперь действительно не ждёт
#
# print("other")  # ✅ выведется сразу
# print([i.result() for i in futures])
# import asyncio
#
#
# async def f(time):
#     await asyncio.sleep(time)
#     return "finally"
#
#
# async def main():
#     task = asyncio.create_task(f(1))
#     task.add_done_callback(lambda t: print("задача выполнена"))
#     task.set_name("name new")
#     print(task.get_name())
#     await task
#     print(task.result())
#
#
# asyncio.run(main())
# import random
# import time
# from concurrent.futures import ThreadPoolExecutor, as_completed
#
#
# def sl():
#     num = random.randint(1, 2)
#     time.sleep(random.randint(1, 2))
#     return f"task {num} complete"
#
#
# if __name__ == "__main__":
#     with ThreadPoolExecutor(max_workers=6) as executor:
#         futures = []
#
#         # Первая партия задач
#         for _ in [1, 2, 3]:
#             futures.append(executor.submit(sl))
#
#         # Вторая партия задач (добавляется в ту же очередь)
#         for _ in [4, 5, 6]:
#             futures.append(executor.submit(sl))
#
#         # Обработка результатов по мере завершения
#         for future in as_completed(futures):
#             print(future.result())
# import asyncio
# import random
# import time
#
#
# async def background():
#     print("Нечто в фоне запустилось")
#     await asyncio.sleep(random.randint(1, 2))
#     return "result task"
#
#
# async def coroutines_list():
#     return [background() for _ in range(3)]
#
#
# async def task_list():
#     return [asyncio.create_task(background()) for _ in range(3)]
#
#
# async def main():
#     t1 = time.perf_counter()
#     asyncio.create_task(background())
#
#     print("Продолжение")
#     await asyncio.sleep(5)
#     print(time.perf_counter() - t1)
#
#
# async def done_wait():
#     done, pend = await asyncio.wait(await task_list())
#
#
# async def wait_for():
#     print("start wait for")
#     return await asyncio.wait_for(background(), timeout=5)
#
#
# async def main_2():
#     t1 = time.perf_counter()
#     asyncio.create_task(done_wait())
#     print("Продолжение")
#     await asyncio.sleep(5)
#     print(time.perf_counter() - t1)
#
#
# def on_done(fut: asyncio.Task):
#     try:
#         result = fut.result()
#         print("Результат из callback:", result)
#     except Exception as e:
#         print("Ошибка:", e)
#
#
# async def main_3():
#     result_task = asyncio.create_task(wait_for())
#     result_task.add_done_callback(on_done)
#
#     print("нечто")
#     await asyncio.sleep(2)
#
#
# if __name__ == "__main__":
#     asyncio.run(main_3())
#
#
# def sub_gen():
#     yield 1.1
#     yield 1.2
#     return "Done!"
#
#
# def gen():
#     yield 1
#     result = yield from sub_gen()
#     print("<--", result)
#     yield 2
#
#
# # Запуск генератора
# for value in gen():
#     print(value)
#
#
# class MyRange:
#     def __init__(self, iters):
#         self.storage = iters
#         self.len = len(self.storage)
#         self.cur_index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.cur_index < self.len:
#             cur_val = self.storage[self.cur_index]
#             self.cur_index += 1
#             return cur_val
#         raise StopIteration
#
#
# g = MyRange([1, 2, 3, 4, 5])
# for _ in g:
#     print(_)
#
# import asyncio
#
#
# async def cor(x):
#     await asyncio.sleep(1)
#     print(x)
#
#
# async def main():
#     asyncio.create_task(cor(6))
#     await asyncio.sleep(2)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
# import asyncio
# import json
#
# from aiohttp import ClientSession, web
#
#
# async def get_weather(city):
#     async with ClientSession() as session:
#         url = "http://api.openweathermap.org/data/2.5/weather"
#         params = {"q": city, "APPID": "2a4ff86f9aaa70041ec8e82db64abf56"}
#
#         async with session.get(url=url, params=params) as response:
#             weather_json = await response.json()
#             try:
#                 return weather_json["weather"][0]["main"]
#             except KeyError:
#                 return "Нет данных"
#
#
# async def handle(request):
#     city = request.rel_url.query["city"]
#     weather = await get_weather(city)
#     result = {"city": city, "weather": weather}
#
#     return web.Response(text=json.dumps(result, ensure_ascii=False))
#
#
# async def main():
#     app = web.Application()
#     app.add_routes([web.get("/weather", handle)])
#     runner = web.AppRunner(app)
#     await runner.setup()
#     site = web.TCPSite(runner, "localhost", 8080)
#     await site.start()
#
#     while True:
#         await asyncio.sleep(3600)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
# import asyncio
#
#
# async def producer(queue: asyncio.Queue):
#     for i in range(10):
#         print(f"Producer: putting {i}")
#         await queue.put(i)  # кладём задачу в очередь
#         await asyncio.sleep(0.5)  # имитация работы
#     print("Producer: done")
#
#
# async def consumer(queue: asyncio.Queue, name: str):
#     while True:
#         await asyncio.sleep(5)
#         item = await queue.get()  # ждём элемент
#         print(f"Consumer {name}: got {item}")
#         await asyncio.sleep(1)  # имитация обработки
#         queue.task_done()  # помечаем, что элемент обработан
#
#
# async def main():
#     queue = asyncio.Queue(maxsize=3)  # очередь вместимостью 3
#
#     prod = asyncio.create_task(producer(queue))
#     tasks = [asyncio.create_task(consumer(queue, str(i))) for i in range(1)]
#
#     await prod  # ждём завершения производителя
#     await queue.join()  # ждём, пока очередь полностью опустеет
#
#     for task in tasks:
#         task.cancel()
#
#
# asyncio.run(main())
# Получатель (Receiver)
# # Command
# class Light:
#     def turn_on(self):
#         print("Лампочка включена")
#
#     def turn_off(self):
#         print("Лампочка выключена")
#
#
# # Команды
# class TurnOnCommand:
#     def __init__(self, light: Light):
#         self.light = light
#
#     def execute(self):
#         self.light.turn_on()
#
#
# class TurnOffCommand:
#     def __init__(self, light: Light):
#         self.light = light
#
#     def execute(self):
#         self.light.turn_off()
#
#
# # Вызыватель (Invoker)
# class RemoteControl:
#     def __init__(self):
#         self._command = None
#
#     def set_command(self, command):
#         self._command = command
#
#     def press_button(self):
#         if self._command:
#             self._command.execute()
#
#
# # Клиентский код
# if __name__ == "__main__":
#     light = Light()
#     remote = RemoteControl()
#
#     remote.set_command(TurnOnCommand(light))
#     remote.press_button()  # Лампочка включена
#
#     remote.set_command(TurnOffCommand(light))
#     remote.press_button()  # Лампочка выключена
#
# # Factory and Strategy
# # Strategy + Simple Factory: корректный, собеседуемый пример
# from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import Callable, Dict, Type
#
#
# # 1) Strategy — общий интерфейс “как отправлять уведомление”
# class NotifStrategy(ABC):
#     @abstractmethod
#     def send(self, message: str) -> None:
#         """Отправить уведомление"""
#         ...
#
#
# # 2) Конкретные стратегии
# class EmailSend(NotifStrategy):
#     def __init__(self, smtp_host: str = "smtp.example.com", recipient: str = "user@example.com"):
#         self.smtp_host = smtp_host
#         self.recipient = recipient
#
#     def send(self, message: str) -> None:
#         # В проде тут был бы вызов SMTP-клиента; на собесе достаточно показать намерение
#         print(f"[EMAIL → {self.recipient} via {self.smtp_host}] {message}")
#
#
# class ConsoleSend(NotifStrategy):
#     def send(self, message: str) -> None:
#         print(f"[CONSOLE] {message}")
#
#
# # 3) Context — класс, который использует стратегию и может её менять на лету
# class Notifier:
#     def __init__(self, strategy: NotifStrategy) -> None:
#         self._strategy = strategy
#
#     def set_strategy(self, strategy: NotifStrategy) -> None:
#         """Позволяет подменить стратегию во время выполнения (главная фишка Strategy)."""
#         self._strategy = strategy
#
#     def notify(self, message: str) -> None:
#         """Единая точка отправки независимо от выбранной стратегии."""
#         self._strategy.send(message)
#
#
# # 4) Simple Factory — отдельная функция, инкапсулирующая создание стратегий
# #    (Можно сделать и классом с фабричным методом, но для простоты достаточно функции.)
# StrategyCtor = Callable[[], NotifStrategy]
# _registry: Dict[str, StrategyCtor] = {
#     "email": lambda: EmailSend(),     # при желании сюда можно пробросить конфиг
#     "console": lambda: ConsoleSend(),
# }
#
#
# def create_strategy(kind: str) -> NotifStrategy:
#     """Фабрика: по строковому ключу создаёт нужную стратегию."""
#     try:
#         return _registry[kind]()
#     except KeyError:
#         raise ValueError(f"Unknown strategy kind: {kind!r}. Available: {list(_registry)}")
#
#
# # 5) Пример использования (то, что ожидают на собесе)
# def main() -> None:
#     notifier = Notifier(create_strategy("console"))
#     notifier.notify("Сервис поднят")
#
#     notifier.set_strategy(create_strategy("email"))
#     notifier.notify("Критическая ошибка: код=500")
#
#
# if __name__ == "__main__":
#     main()
# class HSpec: ...
# class GSpec: ...
# class TSpec: ...
#
# regs = {}
# for name, obj in globals().items():
#     if isinstance(obj, type) and name.endswith("Spec"):
#         regs[name] = obj  # класс
#         # или если нужны экземпляры:
#         # regs[name] = obj()
# from collections import defaultdict
#
# grades = defaultdict(dict)
#
# students = [
#     ("Alice", "Math", "A"),
#     ("Bob", "Math", "B"),
#     ("Alice", "Science", "A"),
#     ("Bob", "Science", "C"),
# ]
#
# for name, subject, grade in students:
#     grades[name][subject] = grade
#
# print(grades)
# class SingletonMeta(type):
#     _instance = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instance:
#             instance = super().__call__(*args, **kwargs)
#             cls._instance[cls] = instance
#             return cls._instance[cls]
#         return cls._instance[cls]
#
# class UseSingle(metaclass=SingletonMeta):
#     def some_logic(self):
#         return 4
#
# u = UseSingle()
# print(u.some_logic())
# import copy
# from copy import deepcopy
#
#
# class Proto:
#     def __init__(self):
#         self.a = 7
#         self.b = 8
#         self.c = self
#
#     def __deepcopy__(self, memo):
#         if memo is None:
#             memo = {}
#         new = self.__class__()
#         new.__dict__ = copy.deepcopy(self.__dict__, memo)
#         return new
#
# pr1 = Proto()
# pr2 = deepcopy(pr1)
# print(pr1.c)
# print(pr2.c)
# print( id(pr1), id(pr2))
# from abc import ABC, abstractmethod
#
#
# class Light:
#     def on(self):
#         return 'light on'
#
#     def off(self):
#         return 'light off'
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}'
#
# class Command(ABC):
#     @abstractmethod
#     def execute(self): ...
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}(target={self.light})'
#
# class CommandOn(Command):
#     def __init__(self, light: Light):
#         self.light = light
#
#     def execute(self):
#         return self.light.on()
#
#
# class CommandOff(Command):
#     def __init__(self, light: Light):
#         self.light = light
#
#     def execute(self):
#         return self.light.off()
#
#
#
# class RemoteControl:
#     def __init__(self):
#         self.history = []
#
#     def press(self, command):
#         self.history.append(command)
#         return command.execute()
#
#     def get_history(self):
#         return self.history
#
#
# light = Light()
# remote  = RemoteControl()
# print(remote.press(CommandOff(light)))
# print(remote.press(CommandOn(light)))
# print(remote.press(CommandOff(light)))
# print(remote.get_history())
#
## Односвязный список #######################
#
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#     def __str__(self):
#         return str(self.value)
#
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None  # держим tail для O(1) добавления в конец
#
#     def push_front(self, value):
#         # O(1)
#         self.head = Node(value, self.head)
#         if self.tail is None:
#             self.tail = self.head
#
#     def push_back(self, value):
#         # O(1), если tail есть; иначе O(n)
#         node = Node(value)
#         if self.tail is None:
#             self.head = self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#
#     def delete_front(self):
#         value = self.head.value
#         self.head = self.head.next
#         return value
#
#     def delete_back(self):
#         # если первое значение None, список пуст
#         if not self.head:
#             return None
#         # если первый и посдений элемент равны, но в списке один элемент,
#         # ставим все в None и возвращаем значение, что было
#         if self.head == self.tail:
#             val = self.head.value
#             self.head = self.tail = None
#             return val
#
#         # берем список сначала
#         cur = self.head
#         # идем по списку, пока не совпадет не найдем ссылку на последний элемент
#         # записываем ссылку предпоследнего элемента
#         while cur.next != self.tail:
#             cur = cur.next
#         # заменяем последнее значение на то, что нашли в прошлом шаге
#         val = self.tail.value
#         self.tail = cur
#         # ставим пустое значение для последнего элемента, который был предпоследним не давно
#         self.tail.next = None
#         return val
#
#     def find(self, value):
#         # O(n)
#         cur = self.head
#         while cur:
#             if cur.value == value:
#                 return cur
#             cur = cur.next
#         return None
#
#     def print_list(self):
#         cur = self.head
#         while cur:
#             print(cur.value)
#             cur = cur.next
#
#
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# single = SinglyLinkedList()
# single.push_front(1)
# single.push_front(2)
# single.push_back(3)
# single.delete_back()
# single.print_list()
#
##  Двусвязный список
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, value):
#         node = Node(value)
#         # если список пуст, начала является концом
#         if not self.head:
#             self.head = self.tail = node
#         # если список не пуст,
#         else:
#             self.tail.next = node
#             node.prev = self.tail
#             self.tail = node
#
#     def list_(self):
#         current = self.head
#         while current:
#
#             print(current.value)
#             current = current.next
#             if current is None:
#                 break
#
#
# double = DoublyLinkedList()
#
# double.append(1)
# double.append(2)
# double.append(3)
# double.list_()
# def check_brackets(s):
#     maping = {
#         ")": "(",
#         "}": "{",
#         "]": "["
#     }
#     li = []
#     for c in s:
#         if c in maping.values():
#             li.append(c)
#         elif c in maping:
#             if li and li.pop() == maping[c]:
#                 continue
#             else:
#                 return False
#     if len(li) == 0:
#         return True
#     return False
#
# print(check_brackets("()"))          # True
# print(check_brackets("([]{})"))      # True
# print(check_brackets("(]"))          # False
# print(check_brackets("((())"))       # False
# print(check_brackets("{[()]}"))
#
# def evk(r, l):
#     if r == l:
#         return r
#     max_ = max(r,l)
#     min_ = min(r,l)
#     r = max_  - min_
#     return  evk(l, r)
#
# print(evk(400,240))
# import random
# import time
#
#
# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         greater = [i for i in arr[1:] if i > pivot]
#         less = [i for i in arr[1:] if i <= pivot]
#
#         return quick_sort(less) + [pivot] + quick_sort(greater)
#
#
# li = [random.randrange(1, 10_000_000) for _ in range(100_000)]
# base = li[:]  # один и тот же ввод
#
# t = time.perf_counter()
# s1 = sorted(base)
# print("sorted:", time.perf_counter() - t)
#
# arr = base[:]  # копия
# t = time.perf_counter()
# quick_sort(arr)
# print("quicksort_inplace:", time.perf_counter() - t)
#
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quick_sort(left) + middle + quick_sort(right)
#
#
#
#
# print(quick_sort([1, 1, 8, 8, 7, 4, 4, 2]))
#
# def bin_search(arr, target):
#     low = 0
#     height = len(arr) - 1
#
#     while low <= height:
#         middle = (low + height) // 2
#         if arr[middle] == target:
#             return middle
#         elif arr[middle] < target:
#             low = middle + 1
#         elif arr[middle] > target:
#             height = middle - 1
#
#     return -1
#
#
# print(bin_search(quick_sort([1, 1, 8, 8, 7, 4, 4, 2]), 1))
#
# Graphs
# from collections import deque
#
#
# def person_is_seller(name):
#     return name == "tom"
#
#
# graph_people = dict()
# graph_people["you"] = ["alice", "bob", "claire"]
# graph_people["bob"] = ["anuj", "peggy"]
# graph_people["alice"] = ["peggy"]
# graph_people["claire"] = ["tom", "jonny"]
# graph_people["anuj"] = []
# graph_people["tom"] = []
# graph_people["jonny"] = []
# graph_people["peggy"] = []
#
#
# def search_wide(graph_param):
#     search_queue = deque()
#     search_queue += graph_param["you"]
#     searched = set()
#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched:
#             if person_is_seller(person):
#                 print("found seller", person)
#                 return True
#             else:
#                 search_queue += graph_param[person]
#                 searched.add(person)
#     return False
#
#
# print(search_wide(graph_people))
#
# graph_task = {
#     "Проснуться": ["Принять душ", "Почистить зубы"],
#     "Принять душ": [],
#     "Почистить зубы": ["Позавтракать"],
#     "Позавтракать": [],
# }
#
# new_task = {
#     "проснуться": ["сделать зарядку", "почистить зубы", "упаковать обед"],
#     "сделать зарядку": ["принять душ"],
#     "принять душ": ["одеться"],
#     "одеться": [],
#     "почистить зубы": ["позавтракать"],
#     "позавтракать": [],
#     "упаковать обед": [],
#     "уйти": [],
# }
#
#
# def is_valid_order(graph, order):
#     done = set()
#     for step in order:
#         # Все «предки» шага — те вершины, из которых есть ребро в step
#         # Находим их
#         required = [v for v, nxt in graph.items() if step in nxt]
#         if not set(required).issubset(done):
#             return False
#         done.add(step)
#     return True
#
#
# def all_topo_orders(graph):
#     indeg = {v: 0 for v in graph}
#     for u in graph:
#         for v in graph[u]:
#             indeg[v] += 1
#
#     result = []
#
#     def backtrack(path, indeg):
#         if len(path) == len(graph):
#             result.append(path[:])
#             return
#         for node in list(graph):
#             if indeg[node] == 0 and node not in path:
#                 # «выбираем» вершину
#                 for nxt in graph[node]:
#                    indeg[nxt] -= 1
#                 path.append(node)
#                 backtrack(path, indeg)
#                 # откат
#                 path.pop()
#                 for nxt in graph[node]:
#                     indeg[nxt] += 1
#
#     backtrack([], indeg)
#     return result
#
#
# for order in all_topo_orders(graph_task):
#     print(order)
#     print(is_valid_order(graph_task, order))
#
#
# def topo_sort(graph):
#     indegree = {v: 0 for v in graph}
#
#     for u in graph:  # проснуться, сделать зарядку,принять душ ...
#         for v in graph[
#             u
#         ]:  # v = ["сделать зарядку", "почистить зубы", "упаковать обед"], ["принять душ"], ...
#             indegree[v] += 1
#             print(indegree)
#     # находим вершины без зависимостей, где значение - 0
#     queue = deque([v for v, d in indegree.items() if d == 0])
#     order = []
#
#     while queue:
#         # берем вершину из очереди. в нашем случае это одна штука
#         node = queue.popleft()
#         # добавляем в конечный результат
#         order.append(node)
#         # проходим по всем ее потомкам, куда есть стрелки
#         for nxt in graph[node]:
#             # уменьшаем зависимости вершин
#             indegree[nxt] -= 1
#             # когда зависимость будет 0, помещаем в очередь, после чего из этого ключа будет забираться
#             if indegree[nxt] == 0:
#                 queue.append(nxt)
#     return order
#
#
# print(topo_sort(new_task))
# class Solution:
#     def missing_number(self, nums: list[int]) -> int:
#         length = len(nums)
#         for i in range(length + 1):
#             if i not in nums:
#                 return i
#         return -1
#
#
# nums = [3, 0, 1]
# sol = Solution()
# print(sol.missing_number(nums))
# class Sample:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#
#
# a = Sample()
# b = Sample()
# print(a is b)
# print(1000 % 60)
# print((1000 //  60) % 60)
# print((1000 // 3600) % 24)
# class Check:
#     def __set_name__(self, owner, name):
#         self.public_name = name
#         self.private_name = "_" + name
#
#     def __get__(self, instance, owner):
#         value = getattr(instance, self.private_name)
#         return value
#
#     def __set__(self, instance, value):
#         if value > 4:
#             setattr(instance, self.private_name, value)
#         else:
#             raise AttributeError('Значение меньше 4')
#
#
# class A:
#     a = Check()
#     def __init__(self, a, b):
#      self.a = a
#      self.b = b
#
#
#
# a = A(7, 8)
# a.a = 9
# print(a.a)
# print(a.__dict__)

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        acc = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[acc]:
                acc += 1
                nums[acc] = nums[i]
        return acc + 1

s = Solution()
print(s.removeDuplicates([1,1,2]))