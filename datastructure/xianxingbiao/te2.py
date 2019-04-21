class StudentNode:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.next = None

class SLL:
    def __init__(self):
        self.head = StudentNode(None,None)


    # 创建学生链表函数
    def createStudentSLL(self):
        print('*********************')
        print('*请输入数据后按回车键确认，若想结束请输入"#"。*')
        print('*********************')
        cNode = self.head
        element = input('请输入姓名、性别并用空格隔开：')
        while element != '#':
            name = element.split(' ')[0]
            sex = element.split(' ')[1]
            nNode = StudentNode(name, sex)
            cNode.next = nNode
            cNode = cNode.next
            element = input('请输入姓名、性别并用空格隔开：')

    # 拆分单链表函数
    def divideSLL(self, linkedListB, linkedListC):
        aNode = self.head
        bNode = linkedListB.head
        cNode = linkedListC.head
        cPos = 0
        while aNode.next:
            aNode = aNode.next
            cPos += 1
            pNode = aNode
            if cPos % 2 == 1:
                bNode.next = pNode
                bNode = bNode.next
            else:
                cNode.next = pNode
                cNode = cNode.next
        bNode.next = None
        cNode.next = None

    # 遍历单链表函数
    def traverseSLL(self):
        cNode = self.head.next
        while cNode.next:
            print(cNode.name,'->',end=' ')
            cNode = cNode.next
        print(cNode.name)

    def getLength(self):
        cNode = self.head.next
        length = 0
        while cNode:
            length += 1
            cNode = cNode.next
        return length

    # 打印函数
    def printSLL(self):
        cNode = self.head.next
        if cNode.sex == '男':
            print('*******************')
            print('男生小分队包含',self.getLength(),'个人，分别是：')
            self.traverseSLL()
        else:
            print('*******************')
            print('女生小分队包含', self.getLength(), '个人，分别是：')
            self.traverseSLL()
        print('*******************')

if __name__ == '__main__':
    la = SLL()
    lb = SLL()
    lc = SLL()
    la.createStudentSLL()
    la.divideSLL(lb,lc)
    lb.printSLL()
    lc.printSLL()