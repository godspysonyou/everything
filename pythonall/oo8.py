class ParentClass1:
    pass

class ParentClass2:
    pass

class SubClass1(ParentClass1):
    pass

class Subclass2(ParentClass1, ParentClass2):
    pass

print(SubClass1.__bases__)

print(Subclass2.__bases__)



# class Cat:
#
#     def eat(self):
#         pass
#
#     def drink(self):
#         pass
#
#     def climbing(self):
#         pass
#
# class Dog:
#
#     def eat(self):
#         pass
#
#     def drink(self):
#         pass
#
#     def look_home(self):
#         pass
#
#


class Animal:

    def eat(self):
        print("%s 吃 " %self.name)

    def drink(self):
        print ("%s 喝 " %self.name)

class Cat(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = '猫'

    def climb(self):
        print('爬树')

class Dog(Animal):

    def __init__(self, name):
        self.name = name
        self.breed='狗'

    def look_after_house(self):
        print('汪汪叫')


# ######### 执行 #########

c1 = Cat('小白家的小黑猫')
c1.eat()

c2 = Cat('小黑的小白猫')
c2.drink()

d1 = Dog('胖子家的小瘦狗')
d1.eat()

