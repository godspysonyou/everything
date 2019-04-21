from mathwork import log


def calcShannonEnt(dataSet):  # 信息熵，另一种是基尼不纯度
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
        # labelCounts[labelCounts] = labelCounts.get(currentLabel,0) + 1
    shannonEnt = 0.0
    # H = -sigmma p*logp
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


myDat, labels = createDataSet()
print(myDat)
print('**********')
print(calcShannonEnt(myDat))
print('**********')

myDat[0][-1] = 'maybe'
print(myDat)
print('**********')
print(calcShannonEnt(myDat))
print('**********')


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


myDat, labels = createDataSet()
print(myDat)
print('*********')
print(splitDataSet(myDat, 0, 1))
print('*********')


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0;
    bestFeature = -1;
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


myDat, labels = createDataSet()
print('最好的划分特征是 %d' % chooseBestFeatureToSplit(myDat))
print('*********')


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        classCount[vote] = classCount.get(vote, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=lambda x: x[1], reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):  # 这里的label可不是标签，而是特征的名字
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):  # 类别完全相同则停止
        return classList[0]

    if len(dataSet[0]) == 1:
        return majorityCnt(classList)  # 遍历完所有特征时返回出现次数最多的
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


myDat, labels = createDataSet()
myTree = createTree(myDat, labels)
print(myTree)
print('**********')

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree,fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)

def lenses_use():
    with open('lenses.txt') as fr:
        lenses = [inst.strip().split('\t') for inst in fr.readlines()]
        lensesLabels = ['age', 'prescript','astigmatic','tearRate']
        lensesTree = createTree(lenses, lensesLabels)
        print(lensesTree)

lenses_use()
print('**********')