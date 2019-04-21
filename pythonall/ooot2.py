class Foo(object):

    staticField = 'old boy'

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'

    @staticmethod
    def bar():
        return 'bar'

print(getattr(Foo, 'staticField'))
print(getattr(Foo, 'func'))
print(getattr(Foo, 'bar'))
