from datastructure.xianxingbiao.t2 import CircularDoubleLinkedList, DoubelLinkedNode

class CDL(CircularDoubleLinkedList):
    def find(self):
        import operator
        pos = 0
        cNode = self.head
        name = input('请主持人指定玫瑰当前的持有者：')
        cmpResult = False
        while cNode.next != self.head and cmpResult == False:
            cNode = cNode.next
            pos = pos + 1
            cmpResult = operator.eq(int(cNode.data), int(name))
        if cmpResult == True:
            return cNode
        else:
            print('输入有误，不存在该参与者！')

    def judgeWinner(self, count, tNode):
        if count == 1:
            print('此轮比赛的季军是：', tNode.data)
        elif count == 2:
            print('此轮比赛的亚军是：', tNode.data)
        elif count == 3:
            print('此轮比赛的冠军是：', tNode.data)
        else:
            print('输入有误')

    def getLength(self):
        cNode = self.head
        length = 0
        while cNode.next != self.head:
            length += 1
            cNode = cNode.next
        return length

    def transRule(self, sign, transNum, count ,tNode):
        cNode = tNode
        pNode = cNode.prev
        if sign == '右':
            while transNum != 0:
                cNode = cNode.next
                pNode = pNode.next
                transNum -= 1
                if cNode == self.head:
                    cNode = cNode.next
                    pNode = pNode.next
        elif sign == '左':
            while transNum != 0:
                cNode = cNode.prev
                pNode = pNode.prev
                transNum -= 1
                if cNode == self.head:
                    cNode = cNode.prev
                    pNode = pNode.prev
        else:
            print('输入有误！')
        self.judgeWinner(count, cNode)
        qNode = cNode.next
        pNode.next = qNode
        qNode.prev = pNode
        del cNode
        cNode = pNode.next

    def traversCircleDoubleLinkedList(self):
        cNode = self.head
        print('按next域遍历带头结点的双链表：')
        if self.isEmpty():
            print('当前双链表为空！')
            return
        while cNode.next != self.head:
            cNode = cNode.next
            self.visitElementByNext(cNode)
        print('None')

    # 按next域输出某一元素
    def visitElementByNext(self, tNode):
        if tNode:
            print(tNode.data,'->',end=' ')

    def roseGame(self):
        import random
        total = self.getLength()
        count = 1
        while count < 4:
            print('***********************')
            self.traversCircleDoubleLinkedList()
            cNode = self.find()
            pNode = cNode.prev
            print('请',cNode.data,'决定传递方向为（左/右）:',end=' ')
            sign = input()
            randomNum = random.randint(0, 100)
            print('主持人第',count,'轮，随机抽取一个数为（1到100）:',randomNum)
            tansNum = randomNum % total
            print('传递次数为：',tansNum)
            self.transRule(sign, tansNum, count, cNode)
            count = count + 1
            total = self.getLength()

        print('****************************')
        print('比赛结束')

if __name__ == '__main__':
    cdl = CDL()
    cdl.createCircularDoubleLinkedList()
    cdl.roseGame()