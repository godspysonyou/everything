class SequenceStack:
    def __init__(self, maxl):
        self.maxStackSize = maxl
        self.s = [None for x in range(self.maxStackSize)]
        self.top = -1

    # 判断栈是否为空
    def isEmptyStack(self):
        if self.top == -1:
            iTop = True
        else:
            iTop = False
        return iTop

    # 进栈
    def pushStack(self, x):
        if self.top < self.maxStackSize-1:
            self.top = self.top + 1
            self.s[self.top] = x
        else:
            print('栈满')
            return

    # 出栈
    def popStack(self):
        if self.isEmptyStack():
            print('栈为空')
            return
        else:
            iTop = self.top
            self.top = self.top - 1
            return self.s[iTop]

    # 获取栈顶元素
    def getTopStack(self):
        if self.isEmptyStack():
            print('栈为空')
            return
        else:
            return self.s[self.top]

    # 遍历栈中元素
    def stackTraverse(self):
        if self.isEmptyStack():
            print('栈为空')
            return
        else:
            for i in range(self.top+1):
                print(self.s[i], end=' ')

    # 通过用户输入的方式创建一个栈
    def createStackByInput(self):
        data = input('请输入元素（继续输入请按回车键，结束请输入"#"）：')
        while data != '#':
            self.pushStack(data)
            data = input('请输入元素：')

# 判断是否为回文单词
def plalindrome(strone):
    ss1 = SequenceStack(20)
    ss2 = SequenceStack(20)
    i = 0
    while i < len(strone):
        ss1.pushStack(strone[i])
        i = i+1
    print('栈ss1内的元素依次为：', end=' ')
    ss1.stackTraverse()
    i = i - 1
    while i < len(strone) and i >= 0:
        ss2.pushStack(strone[i])
        i = i - 1
    print('栈ss2内的元素依次为：', end=' ')
    ss2.stackTraverse()
    while ss1.isEmptyStack() != True:
        if ss1.popStack() != ss2.popStack():
            print('\n当前栈ss1和ss2的元素不相等，所以',strone,'不是回文单词')
            return
    print('\n栈为空，说明ss1和ss2的元素完全一致，所以',strone,'是回文单词')

# 用户测试输入单词是否为回文单词
def testPlalindrome():
    strone = input('请输入一个英文单词：')
    i = 0
    while i < len(strone):
        if (strone[i]>='a' and strone[i]<='z') or (strone[i]>='A' and strone[i]<='Z'):
            i = i + 1
        else:
            break
    if i == len(strone):
        plalindrome(strone)
    else:
        print('输入错误！')



if __name__ == '__main__':
    # ss = SequenceStack(10)
    # ss.createStackByInput()
    # print('栈内元素为：',end=" ")
    # ss.stackTraverse()
    testPlalindrome()