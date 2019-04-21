class A:
    def __init__(self):
        self.x = 1
        print('in init function')

    def __new__(cls, *args, **kwargs):
        print('in new function')
        return object.__new__(A, *args, **kwargs)

a = A()
print(a.x)

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

one = Singleton()
two = Singleton()

two.a = 3
print(one.a)

print(id(one) == id(two))

