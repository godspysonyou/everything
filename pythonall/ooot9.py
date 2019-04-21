class Foo:
    def __init__(self):
        self.__t = 1
        self.a = 1
        self.b = 2

    def __call__(self, *args, **kwargs):
        print('__call__')

    def __len__(self):
        return len(self.__dict__)

    def __hash__(self):
        return hash(str(self.a) + str(self.b))

    def __eq__(self, other):
        if self.a == obj.a and self.b == obj.b:
            return True






obj = Foo()
obj()
print(len(obj))
print(hash(obj))
obj2 = Foo()
print(obj == obj2)
