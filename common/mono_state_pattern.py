class People:
    __shared_dict = {
        'name': 'name',
        'list': ['li1', 'li2', 'li3']
    }
    def __init__(self):
        self.__dict__ = self.__shared_dict

p = People()
p2= People()
p.name = '9999'
del p2.list[2]
print(p.name)
print(p2.name)
print(p.list)