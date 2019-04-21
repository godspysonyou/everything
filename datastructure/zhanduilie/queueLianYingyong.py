from datastructure.zhanduilie.queueLian import LinkQueue
from datastructure.zhanduilie.myqueue import CircularSequenceQueue

class Josephus:
    def josephus(self, n, k):
        qu = LinkQueue()
        i = 1
        while i <= n:
            qu.enQueue(i)
            i = i + 1
        print("队内的编号顺序为：",end=' ')
        qu.queueTraverse()
        print('\n出队列顺序为：')
        count = 0
        while qu.getQueueLength() != 1:
            iNum = 1
            while iNum != k:
                tData = qu.deQueue()
                qu.enQueue(tData)
                iNum += 1
            print(qu.deQueue(), end=" ")
            count = count + 1
            if count % 10 == 0:
                print()
        print("\n最后剩下的一个编号为：",end=" ")
        qu.queueTraverse()

    def testJosephus(self):
        peopleNum = int(input('请输入总人数：'))
        gap = int(input('请输入要出列的编号：'))
        if peopleNum > 0 and gap > 0 and gap <= peopleNum:
            self.josephus(peopleNum, gap)
        else:
            print('输入不符合要求')

    def MatchAB(self):
        quA = CircularSequenceQueue(20)
        quB = CircularSequenceQueue(20)
        print('请输入选手的编号，男生：M****，女生：F****，并以-1结尾')
        while True:
            num = input('请输入选手编号：')
            if num == '-1':
                break
            else:
                if len(num) == 5:
                    if num[0] == 'M':
                        quA.enQueue(num)
                    elif num[0] == 'F':
                        quB.enQueue(num)
                    else:
                        print('输入格式错误')
                else:
                    print('输入格式错误')
        print('A队列的元素有：',end= " ")
        quA.queueTraverse()
        print()
        print('组合的过程如下')
        count = 0
        while True:
            if quA.isEmptyQueue() and quB.isEmptyQueue():
                print('两队都为空，组合结束')
                break
            elif quA.isEmptyQueue():
                print('A队为空，组合结束')
                print('B队剩余的元素为：', end=" ")
                quB.queueTraverse()
                break
            elif quB.isEmptyQueue():
                print('B队为空，组合结束')
                print('A队剩余的元素为：', end=" ")
                quA.queueTraverse()
                break
            else:
                print(quA.deQueue(), end=" ")
                print('组合', end=" ")
                print(quB.deQueue(), end=" ")
                count = count + 1
                print()
        print('\n共有',count,'个组合')



if __name__ == '__main__':
    # j = Josephus()
    # j.testJosephus()
    j = Josephus()
    j.MatchAB()