class StackNode:
    def __init__(self):
        self.data = None
        self.next = None

class LinkStack:
    def __init__(self):
        self.top = StackNode()

    # 判断链栈是否为空
    def isEmptyStack(self):
        if self.top.next == None:
            iTop = True
        else:
            iTop = False
        return iTop

    # 进栈
    def pushStack(self, da):
        tStackNode = StackNode()
        tStackNode.data = da
        tStackNode.next = self.top.next
        self.top.next = tStackNode
        print('当前进栈元素为： ',da)

    # 出栈
    def popStack(self):
        if self.isEmptyStack():
            print('栈为空')
            return
        else:
            tStackNode = self.top.next
            self.top.next = tStackNode.next
            return tStackNode.data

    # 获取栈顶元素
    def getTopStack(self):
        if self.isEmptyStack():
            print('栈为空')
            return
        else:
            return self.top.next.data

    # 通过用户输入创建一个栈
    def createStackByInput(self):
        data = input('请输入元素（继续输入请按回车键，结束请输入"#"）：')
        while data != '#':
            self.pushStack(data)
            data = input('请输入元素：')

    # 遍历栈
    def reverseStackTraverse(self): # 我这里用的不是反转
        if self.isEmptyStack():
            print('栈为空')
            return
        else:
            cNode = self.top.next
            while cNode:
                print(cNode.data,'->',end=' ')
                cNode = cNode.next

    # 检查括号是否匹配
    def bracketMatch(self, strone):
        ls = LinkStack()
        i = 0
        while i < len(strone):
            if strone[i] == '{':
                ls.pushStack(strone[i])
                i = i + 1
            elif strone[i] == '}':
                if ls.getTopStack() ==  '{':
                    ls.popStack()
                    i = i + 1
                else:
                    ls.pushStack(strone[i])
                    i = i + 1
            else:
                i = i + 1
        if ls.isEmptyStack():
            print('括号匹配成功！')
        else:
            print('括号匹配不成功!')
            print('未匹配的括号为：', end=' ')
            ls.reverseStackTraverse()

    def readFile(self, strFileName):
        with open(strFileName) as f:
            strone = f.read()
            print('要判断括号匹配的文件如下：')
            print(strone)
            return strone


if __name__ == '__main__':
    # ls = LinkStack()
    # ls.createStackByInput()
    ls = LinkStack()
    ls.bracketMatch(ls.readFile('1.txt'))
