class CLNode:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.next = None

class CSLL:
    def __init__(self):
        self.head = CLNode(None,None,None)

    def createCSLL(self):
        print('*********************')
        print('请输入数据后按回车键确认，若想结束请输入"#"。*')
        print('*********************')
        cNode = self.head
        element = input('请输入姓名，性别，年龄并用空格隔开：')
        while element != '#':
            name = element.split(' ')[0]
            sex = element.split(' ')[1]
            age = int(element.split(' ')[2])
            nNode = CLNode(name, sex, age)
            cNode.next = nNode
            nNode.next = self.head
            cNode = cNode.next
            element = input('请输入姓名，性别，年龄并用空格隔开：')

    def visitElement(self, tNode):
        if tNode:
            print(tNode.name,tNode.sex,tNode.age,'->',end=' ')
        else:
            print('None')
    def traverseCSLL(self):
        cNode = self.head
        if cNode.next == self.head:
            print('当前循环单链表为空')
            return
        print('您当前的循环单链表为：')
        cNode = cNode.next
        while cNode.next != self.head:
            self.visitElement(cNode)
            cNode = cNode.next
        self.visitElement(cNode)

    def getLength(self):
        cNode = self.head
        length = 0
        while cNode.next != self.head:
            length += 1
            cNode = cNode.next
        return length

    def lottery(self):
        pNode = self.head
        cNode = self.head.next
        count = self.getLength()
        total = self.getLength()
        while count != 1:
            import random
            randomNum = random.randint(0, 100)
            print('****************************')
            print('第',(total-count)+1,'轮抽取得随机数为：',randomNum)
            tansNum = randomNum % count
            while tansNum != 0:
                pNode = pNode.next
                cNode = cNode.next
                tansNum -= 1
                if cNode == self.head:
                    cNode = cNode.next
                    pNode = pNode.next
            print('被淘汰的会员为：', cNode.name)
            pNode.next = cNode.next
            del cNode
            cNode = pNode.next
            count = self.getLength()
        cNode = self.head.next
        print('$$$$$$$$$$$$$$$$$')
        print('最终赢得大奖的是：',cNode.name)

if __name__ == '__main__':
    csll = CSLL()
    csll.createCSLL()
    csll.traverseCSLL()
    csll.lottery()

