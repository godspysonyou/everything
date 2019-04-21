class A:
    def hahaha(self):
        print('A')

class B(A):
    def hahaha(self):
        super().hahaha()
        print('B')

a = A()
b = B()
b.hahaha()
super(B,b).hahaha()