class Foo:

    def __del__(self):
        print('执行我')

f1 = Foo()
del f1
print('------->')

