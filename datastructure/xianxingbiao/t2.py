class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    # 初始化头结点
    def __init__(self):
        self.head = Node(None)

    def isEmpty(self):
        return not self.head.next

    # 创建单链表
    def createSingleLinkedList(self):
        print('********************')
        print("*请输入数据后按回车键确认，若想结束请输入'#'。*")
        cNode = self.head
        element = input('请输入当前节点的值：')
        while element != '#':
            nNode = Node(int(element))
            cNode.next = nNode
            cNode = cNode.next
            element = int(input('请输入当前节点的值：'))

    # 尾端插入元素，时间复杂度O（n）
    def insertElementInTail(self):
        element = int(input('请输入待插入节点的值：'))
        if element == '#':
            return
        cNode = self.head
        nNode = Node(int(element))
        while cNode.next:
            cNode = cNode.next
        cNode.next = nNode

    # 首端插入元素，时间复杂度O（1）
    def insertElementInHead(self):
        element = input('请输入待插入结点的值：')
        if element == '#':
            return
        cNode = self.head
        nNode = Node(int(element))
        nNode.next = cNode.next
        cNode.next = nNode

    # 查找指定元素并返回其位置
    def findElement(self):
        pos = 0
        cNode = self.head
        key = input('请输入想要查找的元素值：')
        if self.isEmpty():
            print('当前单链表为空！')
            return
        while(cNode.next and cNode.data != key):
            cNode = cNode.next
            pos += 1
        if cNode.data == key:
            print('查找成功，值为',key,'的结点位于单链表的第',pos,'个位置')
        else:
            print('查找失败！当前单链表不存在值为',key,'的元素')

    # 删除元素
    def deleteElement(self):
        dElement = int(input('请输入待删除结点的值：'))
        cNode = self.head
        pNode = self.head
        if self.isEmpty():
            print('当前单链表为空！')
            return
        while cNode.next and cNode.data!=dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            pNode.next = cNode.next
            del cNode
            print('成功删除含有元素', dElement, '的结点')
        else:
            print('删除失败！当前单链表中不存在含有元素',dElement,'的结点')


    # 遍历单链表
    def traverseElement(self):
        cNode = self.head
        if not cNode.next:
            print('当前单链表为空')
            return
        print('您当前的单链表为：')
        while cNode:
            cNode = cNode.next
            self.visitElement(cNode)

    # 输出单链表某一元素
    def visitElement(self, tNode):
        if tNode:
            print(tNode.data,'->',end=' ')
        else:
            print('None')


class CircularSingleLinkedList:
    def __init__(self):
        self.head = Node(None)

    # 创建循环单链表
    def createCircularSingleLinkedList(self):
        print('*******************')
        print("*请输入数据后按回车键确认，若想结束请输入'#'。*")
        print('*******************')
        data = input('请输入结点的值：')
        cNode = self.head
        while data != '#':
            nNode = Node(int(data))
            cNode.next = nNode
            nNode.next = self.head
            cNode = cNode.next
            data = input('请输入结点的值：')

    # 尾端插入
    def insertElementInTail(self):
        element = input('请输入待插入结点的值：')
        if element == '#':
            return
        cNode = self.head
        nNode = Node(int(element))
        while cNode.next != self.head:
            cNode = cNode.next
        cNode.next = nNode
        nNode.next = self.head

    # 首端插入元素
    def insertElementInHead(self):
        element = input('请输入待插入结点的值：')
        if element == '#':
            return
        cNode = self.head
        nNode = Node(int(element))
        nNode.next = cNode.next
        cNode.next = nNode

    def isEmpty(self):
        return self.head.next == self.head

    # 删除元素
    def deleteElement(self):
        dElement = int(input('请输入待删除结点的值：'))
        cNode = self.head
        pNode = self.head
        if self.isEmpty():
            print('当前循环单链表为空！')
            return
        while cNode.next != self.head and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            pNode.next = cNode.next
            del cNode
            print('成功删除含有元素',dElement,'的结点')
        else:
            print('删除失败，循环链表中不存在含有元素',dElement,'的结点\n')

class DoubelLinkedNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = DoubelLinkedNode(None)

    def isEmpty(self):
        return not self.head.next

    # 创建双链表
    def createDoubleLinkedList(self):
        print('*****************')
        print("*请输入数据后按回车键确认，若想结束请输入'#'。*")
        print('*****************')
        data = input('请输入元素：')
        cNode = self.head
        while data != '#':
            nNode = DoubelLinkedNode(int(data))
            cNode.next = nNode
            nNode.prev = cNode
            cNode = cNode.next
            data = input('请输入元素：')

    # 尾端插入
    def insertElementInTail(self):
        element = input('请输入待插入结点的值：')
        if element != '#':
            return
        nNode = DoubelLinkedNode(int(element))
        cNode = self.head
        while cNode.next:
            cNode = cNode.next
        cNode.next = nNode
        nNode.pre = cNode

    # 首端插入元素
    def insertElementInHead(self):
        element = input('请输入待插入结点的值：')
        if element != '#':
            return
        cNode = self.head.next
        pNode = self.head
        nNode = DoubelLinkedNode(int(element))
        nNode.prev = pNode
        pNode.next = nNode
        nNode.next = cNode
        cNode.prev = nNode

    # 删除元素
    def deleteElement(self):
        dElement = int(input('请输入待删除结点的值：'))
        cNode = self.head
        pNode = self.head
        if self.isEmpty():
            print('当前双链表为空！')
            return
        while cNode.next and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            if cNode.next == None:
                pNode.next = None
                del cNode
                print('成功删除含有元素',dElement,'的结点！\n')
            else:
                qNode = cNode.next
                pNode.next = qNode
                qNode.prev = pNode
                del cNode
                print('成功删除含有元素',dElement,'的结点！\n')
        else:
            print('删除失败！双链表中不存在含有元素',dElement,'的结点\n')

    # 遍历双链表
    def traversDoubleLinkedList(self):
        cNode = self.head
        print('按next域遍历带头结点的双链表：')
        if self.isEmpty():
            print('当前双链表为空！')
            return
        while cNode.next:
            cNode = cNode.next
            self.visitElementByNext(cNode)
        print('None')

    # 按next域输出某一元素
    def visitElementByNext(self, tNode):
        if tNode:
            print(tNode.data,'->',end=' ')

class CircularDoubleLinkedList:
    def __init__(self):
        self.head = DoubelLinkedNode(None)
    def isEmpty(self):
        if self.head.next == self.head:
            return True
        return False

    # 创建循环双链表
    def createCircularDoubleLinkedList(self):
        print('******************')
        print('*请输入数据后按回车键确认，若想结束请输入"#"。*')
        print('******************')
        data = input('请输入元素：')
        cNode = self.head
        while data != '#':
            nNode = DoubelLinkedNode(int(data))
            cNode.next = nNode
            nNode.prev = cNode
            nNode.next = self.head
            self.head.prev = nNode
            cNode = cNode.next
            data = input('请输入元素：')

    # 尾端插入
    def insertElementInTail(self):
        element = input('请输入待插入结点的值：')
        if element == '#':
            return
        nNode = DoubelLinkedNode(int(element))
        cNode = self.head
        while cNode.next != self.head:
            cNode = cNode.next
        cNode.next = nNode
        nNode.pre = cNode
        nNode.next = self.head
        self.head.prev = nNode

    # 首端插入
    def insertElementInHead(self):
        element = input('请输入待插入结点的值：')
        if element == '#':
            return
        cNode = self.head.next
        pNode = self.head
        nNode = DoubelLinkedNode(int(element))
        nNode.prev = pNode
        pNode.next = nNode
        nNode.next = cNode
        cNode.prev = nNode

    # 删除元素
    def deleteElement(self):
        dElement = int(input('请输入待删除的结点：'))
        cNode = self.head
        pNode = self.head
        if self.isEmpty():
            print('当前循环双链表为空！')
            return
        while cNode.next != self.head and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            qNode = cNode.next
            pNode.next = qNode
            qNode.prev = pNode
            del cNode
            print('成功删除含有元素',dElement,'的结点')
        else:
            print('删除失败！循环双链表中不存在含有元素',dElement,'的结点\n')

    def traversCircleDoubleLinkedList(self):
        cNode = self.head
        print('按next域遍历带头结点的双链表：')
        if self.isEmpty():
            print('当前双链表为空！')
            return
        while cNode.next:
            cNode = cNode.next
            self.visitElementByNext(cNode)
        print('None')

    # 按next域输出某一元素
    def visitElementByNext(self, tNode):
        if tNode:
            print(tNode.data,'->',end=' ')


