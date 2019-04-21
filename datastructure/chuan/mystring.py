class StringList:
    def __init__(self):
        self.maxStringSize = 256
        self.chars = ""
        self.length = 0

    # 获取字符串长度
    def getStringLength(self):
        return self.length

    # 获取字符串序列
    def getString(self):
        return self.chars


    # 判断string是否为空
    def isEmptyString(self):
        if self.length == 0:
            isEmpty = True
        else:
            isEmpty = False
        return isEmpty

    # 创建一个串的函数
    def createString(self):
        stringSH = input('请输入字符串，按回车键结束输入：')
        if len(stringSH) > self.maxStringSize:
            print('输入的字符序列超过分配的存储空间，超过的部分无法存入当前串中。')
            self.chars = stringSH[:self.maxStringSize]
        else:
            self.chars = stringSH
        self.length = len(self.chars)

    # 串连接
    def stringConcat(self, strSrc):
        lengthSrc = strSrc.length
        stringSrc = strSrc.chars
        if lengthSrc + len(self.chars) <= self.maxStringSize:
            self.chars = self.chars + stringSrc
        else:
            print('两个字符串连接后的长度超过分配的内存，超过的部分无法显示。')
            size = self.maxStringSize - len(self.chars)
            self.chars = self.chars + stringSrc[0:size]
        print('连接后的字符串为：',self.chars)

    # 从指定位置开始获取指定长度子串
    def subString(self, iPos, length):
        if iPos > len(self.chars) - 1 or iPos < 0 or length < 1 or (length+iPos>len(self.chars)):
            print('无法获取字串')
        else:
            substr = self.chars[iPos:iPos+length]
            print('获取的字串为：',substr)

    # 遍历串
    def stringTraverse(self):
        for c in self.chars:
            print(c,end=' ')

    # BF算法
    def indexBF(self, pos, T):
        length = T.getStringLength()
        if len(self.chars)<length:
            print('字串的长度大于主串的长度，无法进行字符串的模式匹配')
        else:
            tag = False
            i = pos
            string = T.getString()
            while (i < len(self.chars) - length):
                iT = i
                j = 0
                tag = False
                while j < length:
                    if self.chars[i] == string[j]:
                        i = i+1
                        j=j+1
                    else:
                        break
                if j == length:
                    print('匹配成功！模式串在主串中首次出现的位置为',iT)
                    tag = True
                    break
                else:
                    i = iT+1
            if tag == False:
                print('匹配失败！')

    # KMP算法
    def indexKMP(self, pos, T, ListNextValue):
        i = pos
        j = 0
        length = T.getStringLength()
        string = T.getString()
        while i <len(self.chars) and j <length:
            if j == -1 or self.chars[i]==string[j]:
                i = i+1
                j = j+1
            else:
                j = ListNextValue[j] # 从next数组中查找
        if j==length:
            print('匹配成功！模式串在主串中首次出现的位置为',i-length)
        else:
            print('匹配失败！')

    # 获取模式串的listNext值的函数
    def getListNext(self):
        listNext = [None for x in range(100)]
        listNext[0] = -1
        k = -1
        j = 0
        while j < len(self.chars):
            if k==-1 or self.chars[j]==self.chars[k]:
                k=k+1
                j=j+1
                listNext[j] = k
            else:
                k = listNext[k]
        return listNext

    # 获取模式串的listNextValue的值
    def getListNextValue(self):
        listNextValue = [None for x in range(100)]
        listNextValue[0] = -1
        k = -1
        j = 0
        while j < len(self.chars) - 1:
            if k == -1 or self.chars[j] == self.chars[k]:
                k = k + 1
                j = j + 1
                if self.chars[j] != self.chars[k]:
                    listNextValue[j] = k
                else:
                    listNextValue[j] = listNextValue[k]
            else:
                k = listNextValue[k]
        return listNextValue

class TestIndex:
    def testIndexBF(self):
        s = StringList()
        s.createString()
        print('主串为：',end=' ')
        s.stringTraverse()
        t = StringList()
        t.createString()
        print('模式为：',end=' ')
        t.stringTraverse()
        pos = int(input('请输入从主串的哪一位纸开始串的模式匹配：'))
        print('匹配结果',end=' ')
        s.indexBF(pos, t)

    def testIndexKMP(self):
        s = StringList()
        s.createString()
        print('主串为：',end=' ')
        s.stringTraverse()
        print()
        t = StringList()
        t.createString()
        print('模式串为：',end=' ')
        t.stringTraverse()
        pos = int(input('\n请输入从主串的哪一位开始串的模式匹配：'))
        print('\n借助listNext值的匹配结果：')
        s.indexKMP(pos, t, t.getListNext())
        print('\n借助listNextValue值的匹配结果：')
        s.indexKMP(pos, t, t.getListNextValue())


if __name__ == '__main__':
    # test = TestIndex()
    # test.testIndexBF()
    # test = TestIndex()
    # test.testIndexKMP()
    s = StringList()
    s.createString()
    print(s.getListNextValue())




