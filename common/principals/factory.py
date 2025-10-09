class ShapeFactory:
    _registry = {}

    @classmethod
    def register_shape(cls, shape_type, shape_class):
        cls._registry[shape_type] = shape_class

    @classmethod
    def create_shape(cls, shape_type):
        shape_class = cls._registry.get(shape_type)
        if not shape_class:
            raise ValueError(f"Unknown shape type: {shape_type}")
        return shape_class()


# Пример фигур
class Circle:
    def draw(self):
        print("Drawing Circle")


class Square:
    def draw(self):
        print("Drawing Square")


# Регистрируем
ShapeFactory.register_shape("circle", Circle)
ShapeFactory.register_shape("square", Square)

# Используем
shape = ShapeFactory.create_shape("circle")
shape.draw()
