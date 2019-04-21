class SequenceList:
    def __init__(self):
        self.seqList = []

    # 创建顺序表
    def createSeqenceList(self):
        print("********************")
        print("*请输入数据后按回车键确认，若想结束请输入'#'。*")
        print("********************")
        element = input("请输入元素：")
        while element != '#':
            self.seqList.append(int(element))
            element = input("请输入元素：")

    # 查找元素，时间复杂度O（n）
    def findElement(self):
        key = int(input('请输入想要查找的元素：'))
        if key in self.seqList:
            ipos = self.seqList.index(key) # 调用了index方法
            print('查找成功！值为',self.seqList[ipos],'的元素，位于当前顺序表第',ipos+1,"个位置。")
        else:
            print('查找失败！当前顺序表中不存在值为',key,'的元素')

    # 指定位置插入元素函数，元素平均移动n/2次
    def insertElement(self):
        ipos = int(input('请输入待插入元素的位置：'))
        element = int(input('请输入待插入的元素值：'))
        self.seqList.insert(ipos, element)
        print('插入元素后，当前顺序表为： \n',self.seqList)

    # 指定位置删除，元素平均移动(n-1)/2次
    def deleteElement(self):
        dpos = int(input('请输入待删除元素的位置：'))
        print('正在删除元素',self.seqList[dpos],'...')
        self.seqList.remove(self.seqList[dpos])
        print('删除后顺序表为：\n',self.seqList)

    # 遍历顺序表
    def traverseElement(self):
        seqListLen = len(self.seqList)
        print('*****遍历顺序表中元素*****')
        for i in range(seqListLen):
            print('第',i+1,"个元素的值为",self.seqList[i])


    # 求顺序表最值
    def getExtremum(self):
        while True:
            print('********************')
            print('*1:查询最大值')
            print('*2:查询最小值')
            print('*3:查询最大值和最小值')
            print('*0:退出程序')
            print('********************')
            i = int(input('请输入：'))
            if i == 1:
                print('顺序表中最大值为：',max(self.seqList))
            elif i == 2:
                print('顺序表中最小值为：',min(self.seqList))
            elif i == 3:
                print('顺序表中最大值为：', max(self.seqList))
                print('顺序表中最小值为：', min(self.seqList))
            elif i==0:
                break

if __name__ == '__main__':
    L = SequenceList()
    L.createSeqenceList()
    L.getExtremum()
