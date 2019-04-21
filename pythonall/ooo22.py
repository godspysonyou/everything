class Classmethod_Demo():
    role = 'dog'

    @classmethod
    def func(cls):
        print(cls.role)


Classmethod_Demo.func()

class Staticmethod_Demo():
    role = 'dog'

    @staticmethod
    def func():
        print('当普通方法用')


Staticmethod_Demo.func()

class Foo:
    def func(self):
        print('in father')


class Son(Foo):
    def func(self):
        print('in son')

s = Son()
s.func()
# 请说出上面一段代码的输出并解释原因？

