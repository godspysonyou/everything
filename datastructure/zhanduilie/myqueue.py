class SequenceQueue:
    def __init__(self, maxSize):
        self.maxQueueSize = maxSize
        self.s = [None for x in range(self.maxQueueSize)]
        self.front = 0
        self.rear = 0

    # 判断队列是否为空
    def isEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    # 元素进队列
    def enQueue(self, x):
        if (self.rear < self.maxQueueSize - 1):
            self.rear = self.rear + 1
            self.s[self.rear] = x
            print('当前进队元素为：', x)
        else:
            print('队列已满，无法进队')
            return

    # 元素出队列
    def deQueue(self):
        if self.isEmptyQueue():
            print('队列为空，无法出队列')
            return
        else:
            self.front = self.front + 1
            return self.s[self.front]

    # 获取队头元素
    def getHead(self):
        if self.isEmptyQueue():
            print('队列为空，无法输出队头元素')
            return
        else:
            return self.s[self.front+1]


    # 通过用户输入的方式创建队列
    def createQueueByInput(self):
        data = input('请输入元素（继续输入请按回车键，结束请输入"#"）：')
        while data != '#':
            self.enQueue(data)
            data = input('请输入元素：')

# 0 1 2 3 4 5 6
# k k k k k f r
# k代表空，f代表front，r代表rear
# 当这种情况下，有新元素要进队时会提示队列已满

# 循环队列队空条件front==rear
# 队列满条件 front = (rear+1)%maxQueueSize
# 队列中元素个数 (rear-front+maxQueueSize)%maxQueueSize
class CircularSequenceQueue:
    def __init__(self, maxSize):
        self.maxQueueSize = maxSize
        self.s = [None for x in range(self.maxQueueSize)]
        self.front = 0
        self.rear = 0

    # 遍历元素
    def queueTraverse(self):
        if self.isEmptyQueue():
            print('队列为空，无法输出')
            return
        else:
            flag = self.front
            while flag != self.rear:
                print(self.s[flag+1], end=" ")
                flag = (flag + 1) % self.maxQueueSize



    def getQueueLength(self):
        return (self.rear - self.front+self.maxQueueSize)%self.maxQueueSize

    def getHead(self):
        if self.isEmptyQueue():
            print('队列为空，无法输出队头元素')
            return
        else:
            return self.s[(self.front+1)%self.maxQueueSize] # ？

    def isEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    # 进队列
    def enQueue(self, x):
        if (self.rear+1)%self.maxQueueSize!=self.front:
            self.rear=(self.rear+1)%self.maxQueueSize
            self.s[self.rear] = x
            print('当前进队元素为：', x)
        else:
            print('队列已满，无法进队')
            return
    # 出队列
    def deQueue(self):
        if self.isEmptyQueue():
            print('队列为空，无法出队')
            return
        else:
            self.front = (self.front+1)%self.maxQueueSize
            return self.s[self.front]

    # 将用户输入的元素进队的函数
    def createQueueByInput(self):
        data = input('请输入元素（继续输入请按回车键，结束请输入"#"）：')
        while data != '#':
            self.enQueue(data)
            data = input('请输入元素：')





if __name__ == '__main__':
    # sq = SequenceQueue(10)
    # sq.createQueueByInput()
    csq = CircularSequenceQueue(10)
    csq.createQueueByInput()