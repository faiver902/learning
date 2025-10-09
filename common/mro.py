class A:
    def ping(self):
        print("A")


class C(A):
    def ping(self):
        print("C")
        super().ping()


class B(A):
    def ping(self):
        print("B")
        super().ping()


class D(C, B):
    def ping(self):
        print("D")
        super().ping()


d = D()
d.ping()
print(D.__mro__)


class X:
    pass


class Y:
    pass


class Z(Y, X):
    pass


class Bad(X, Y):
    pass  # меняем порядок


class Boom(Z, Bad):  # ← конфликт
    pass


print(Boom.__mro__)
