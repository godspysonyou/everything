# class A:
#     def fa(self):
#         print('from A')
#
#     def test(self):
#         self.fa()
#
#
# class B(A):
#     def fa(self):
#         print('from B')
#
#
# b = B()
# b.test()


class A:
    def __fa(self):
        print('from A')

    def test(self):
        self.__fa()


class B(A):
    def __fa(self):
        print('from B')

b = B()
b.test()
print(B.__dict__)
print(A.__dict__)
