'''
从大规模数据中寻找物品间的隐含关系成为"关联分析"
一个项集的支持度被定义为数据集中包含该项集的记录所占的比例
可信度或置信度（cofidence）针对一条诸如{尿布}->{葡萄酒}的关联规则来定义的。两个支持度相除。

Aprior原理可以帮我们减少可能感兴趣的项集。Apriori原理说如果某个项集是频繁的，那么它的所有子集也是频繁的。
这个原理在直观上并没有什么帮助，但是反过来就很有用。也就是说：如果一个项集是非频繁项集，那么它的所有超集也是
非频繁的。



'''
def loadDataSet():
    return [[1,3,4],
            [2,3,5],
            [1,2,3,5],
            [2,5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can):
                    ssCnt[can]=1
                else:
                    ssCnt[can]+=1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support>= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

'''
当集合中的项的个数大于零时：
    构建一个k个项组成的候选项集的列表
    检查数据以确认每个项集都是频繁的
    保留频繁项集并构建k+1项组成的候选项集的列表
'''