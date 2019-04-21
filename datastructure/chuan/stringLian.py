# 串的存储密度=串所在的存储位/实际分配的存储位

class StringNode:
    def __init__(self):
        self.data = None
        self.next = None

class StringLink:
    def __init__(self):
        self.head = StringNode()
        self.tail = self.head
        self.length = 0

    # 创建一个链串的函数
    def createString(self):
        stringSH = input('\n请输入字符串，按回车键结束输入：')
        while self.length < len(stringSH):
            tString = StringNode()
            tString.data = stringSH[self.length]
            self.tail = tString
            self.length = self.length + 1

    # 复制串的函数实现
    def stringCopy(self, strSrc):
        self.head = strSrc.head
        self.tail = strSrc.tail
        self.length = strSrc.length

    # 串连接
    def StringConcat(self, strSrc):
        self.tail.next = strSrc.head.next
        self.tail = strSrc.tail
        self.length = self.length + strSrc.length