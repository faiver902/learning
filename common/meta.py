from pprint import pprint


class VerboseMeta(type):
    # 1) Вызывается САМЫМ ПЕРВЫМ, ещё до исполнения тела класса.
    @classmethod
    def __prepare__(mcls, name, bases, **kw):
        print(f"__prepare__: name={name}, bases={bases}, kw={kw}")
        # можно вернуть любой «словарь-подобный» объект; вернём обычный dict
        return {}

    # 2) Создание объекта-класса
    def __new__(mcls, name, bases, ns, **kw):
        print(f"\n__new__: name={name}")
        print("  bases ->", bases)
        print("  extra kw ->", kw)
        print("  namespace:")
        pprint(ns, indent=4, width=50)
        cls = super().__new__(mcls, name, bases, ns)
        return cls

    # 3) Инициализация уже созданного класса
    def __init__(cls, name, bases, ns, **kw):
        print(f"__init__: класс {cls.__name__} готов\n")
        super().__init__(name, bases, ns)

    # 4) Создание экземпляра (вызывает A())
    def __call__(cls, *args, **kwargs):
        print(f"__call__: создаём экземпляр {cls.__name__}")
        print("  args ->", args)
        print("  kwargs ->", kwargs)
        return super().__call__(*args, **kwargs)


# ----------------------------------------------
#      объявляем класс с метаклассом
# ----------------------------------------------
class A(metaclass=VerboseMeta, flag=True):
    x = 10
    y = "hello"

    def __init__(self, a, option):
        self.a = a
        self.option = option

    def foo(self):
        return "bar"


# ----------------------------------------------
#      создаём экземпляр
# ----------------------------------------------
a = A(42, option="yes")
print(dir())

# __prepare__: name=A, bases=(), kw={'flag': True}
#
# __new__: name=A
#   bases -> ()
#   extra kw -> {'flag': True}
#   namespace:
# {   '__init__': <function A.__init__ at 0x0000020B0A42B740>,
#     '__module__': '__main__',
#     '__qualname__': 'A',
#     'foo': <function A.foo at 0x0000020B0A42B7E0>,
#     'x': 10,
#     'y': 'hello'}
# __init__: класс A готов
#
# __call__: создаём экземпляр A
#   args -> (42,)
#   kwargs -> {'option': 'yes'}
# ['A', 'VerboseMeta', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'pprint']
