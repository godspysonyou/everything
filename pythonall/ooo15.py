#其实这仅仅这是一种变形操作
#类中所有双下划线开头的名称如__x都会自动变形成：_类名__x的形式：

class A:
    __N=0 #类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A__N
    def __init__(self):
        self.__X=10 #变形为self._A__X
    def __foo(self): #变形为_A__foo
        print('from A')
    def bar(self):
        self.__foo() #只有在类内部才可以通过__foo的形式访问到.

#A._A__N是可以访问到的，即这种操作并不是严格意义上的限制外部访问，仅仅只是一种语法意义上的变形

#print(A.__N)
print(A._A__N)

a = A()
print(a.__dict__)
print(A.__dict__)
a.__Y = 1
print(a.__dict__)