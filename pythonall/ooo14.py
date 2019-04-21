import abc

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass

class People(Animal):
    def talk(self):
        print('say hello')


class Dog(Animal):
    def talk(self):
        print('say wangwang')


class Pig(Animal):
    def talk(self):
        print('say aoao')


class File(metaclass=abc.ABCMeta): #同一类事物:文件
    @abc.abstractmethod
    def click(self):
        pass

class Text(File): #文件的形态之一:文本文件
    def click(self):
        print('open file')

class ExeFile(File): #文件的形态之二:可执行文件
    def click(self):
        print('execute file')


peo=People()
dog=Dog()
pig=Pig()

#peo、dog、pig都是动物,只要是动物肯定有talk方法
#于是我们可以不用考虑它们三者的具体是什么类型,而直接使用
peo.talk()
dog.talk()
pig.talk()

#更进一步,我们可以定义一个统一的接口来使用
def func(obj):
    obj.talk()


#二者都像鸭子,二者看起来都像文件,因而就可以当文件一样去用
class TxtFile:
    def read(self):
        pass

    def write(self):
        pass

class DiskFile:
    def read(self):
        pass
    def write(self):
        pass

