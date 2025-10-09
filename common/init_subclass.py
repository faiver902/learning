class Base:
    def __init_subclass__(cls, **kwargs):
        super(Base, cls).__init_subclass__()
        print(f"Создан подкласс {cls.__name__}")


class A(Base, flag=True):
    """
    str
    """

    pass


class B(Base, flag=True):
    pass


class PluginBase:
    registry: dict[str, type] = {}

    def __init_subclass__(cls, name: str | None = None, **kw):
        super().__init_subclass__(**kw)
        key = name or cls.__name__.lower()
        PluginBase.registry[key] = cls


class CsvPlugin(PluginBase, name="csv"):
    pass


class JsonPlugin(PluginBase):
    pass


print(PluginBase.registry)

print(JsonPlugin.__mro__)
print("PluginBase", PluginBase().registry)


class ServiceBase:
    required_methods = {"execute", "rollback"}

    def __init_subclass__(cls, **kw):
        super().__init_subclass__(**kw)
        missing = ServiceBase.required_methods - cls.__dict__.keys()
        if missing:
            raise TypeError(f"{cls.__name__}: нет методов {missing}")


class GoodService(ServiceBase):
    def execute(self): ...

    def rollback(self): ...


class Bad(ServiceBase):
    def execute(self): ...


# TypeError: Bad: нет методов {'rollback'}
