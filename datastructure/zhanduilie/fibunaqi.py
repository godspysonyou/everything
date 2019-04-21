

from datastructure.zhanduilie.myqueue import CircularSequenceQueue

class Fibunaqi:
    def fibonacci(self, n):
        qu = CircularSequenceQueue(20)
        if n == 0:
            print('起始小兔的总对数为：', 1)
            return
        elif n==1:
            print('起始小兔的总对数为：', 2)
            return
        else:
            qu.enQueue(1)
            qu.enQueue(2)
            iMonth = 1
            while iMonth < n:
                numHead = qu.deQueue()
                numRear = qu.getHead()
                totalNumber = numHead + numRear
                qu.enQueue(totalNumber)
                iMonth = iMonth + 1
            while qu.getQueueLength() != 1:
                qu.deQueue()
        print('第',n,'个月小兔的总对数为：',qu.deQueue())

    def testFibonacci(self):
        n = int(input('请输入要求那个月的小兔总对数：'))
        while n < 0:
            n = int(input('请重新输入需要求哪个月的小兔总对数：'))
        self.fibonacci(n)

if __name__ == '__main__':
    t = Fibunaqi()
    t.testFibonacci()