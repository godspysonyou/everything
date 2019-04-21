class QueueNode:
    def __init__(self):
        self.data = None
        self.next = None


class LinkQueue:
    def __init__(self):
        tQueueNode = QueueNode()
        self.front = tQueueNode
        self.rear = tQueueNode

    # 判断链式队列是否为空的函数
    def isEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    # 进队
    def enQueue(self, da):
        tQueueNode = QueueNode()
        tQueueNode.data = da
        self.rear.next = tQueueNode
        self.rear = tQueueNode
        print('当前进队的元素为：',da)

    # 出队列
    def deQueue(self):
        if self.isEmptyQueue():
            print('队列为空')
            return
        else:
            tQueueNode = self.front.next
            self.front.next = tQueueNode.next
            if self.rear == tQueueNode:
                self.rear = self.front
            return tQueueNode.data

    def getQueueLength(self):
        length = 0
        flag = self.front.next
        while flag:
            length += 1
            flag = flag.next
        return length

    # 获取对头元素的函数
    def getHead(self):
        if self.isEmptyQueue():
            print('队列为空')
            return
        else:
            return self.front.next.data

    def queueTraverse(self):
        if self.isEmptyQueue():
            print('队列为空')
            return
        else:
            flag = self.front.next
            while flag:
                print(flag.data, end=" ")
                flag = flag.next

    # 通过用户输入的方式创建一个队列
    def createQueueByInput(self):
        data = input('请输入元素（继续输入请按回车键，结束请输入"#"）:')
        while data != '#':
            self.enQueue(data)
            data = input('请输入元素：')


class CircleLinkQueue:
    def __init__(self):
        tQueueNode = QueueNode()
        self.rear =tQueueNode
        self.rear.next = tQueueNode

    def enQueue(self, da):
        tQueueNode = QueueNode()
        tQueueNode.data = da
        tQueueNode.next = self.rear.next
        self.rear.next = tQueueNode
        self.rear = tQueueNode

    def isQueueEmpty(self):
        if self.rear == self.rear.next:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    def deQueue(self):
        if self.isQueueEmpty():
            print('队列为空')
            return
        else:
            front = self.rear.next
            d0 = front.next
            front.next = d0.next
            d0.next = None



if __name__ == '__main__':
    lq = LinkQueue()
    lq.createQueueByInput()
