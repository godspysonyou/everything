import operator

import numpy as np


def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


group, labels = createDataSet()
print(group)
print(labels)
print('*********')


def classify0(inX, dataSet, labels, k):
    '''

    :param inX: 待比较的数据
    :param dataSet: 只包含特征的数据集
    :param labels: 标签
    :param k: k个邻居
    :return:
    '''
    dataSetSize = dataSet.shape[0]
    diffMat = inX - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)  # 列相加
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()  # 得到下标
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    sortedClassCount = sorted(classCount.items(), key=lambda x: x[1], reverse=True)
    return sortedClassCount[0][0]


print(classify0([0, 0], group, labels, 3))
print('*********')


def file2matrix(filename):
    with open(filename) as fr:
        arrayOlines = fr.readlines()
        numberOfLines = len(arrayOlines)
        returnMat = np.zeros((numberOfLines, 3))
        classLabelVector = []
        index = 0
        for line in arrayOlines:
            line = line.strip()
            listFromLine = line.split('\t')
            returnMat[index, :] = listFromLine[0:3]
            classLabelVector.append(int(listFromLine[-1]))
            index += 1
    return returnMat, classLabelVector


datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
print(datingDataMat)
print('*********')


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


normMat, ranges, minVals = autoNorm(datingDataMat)
print(normMat)
print('*********')


def datingClassTest():
    hoRatio = 0.1
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print('the classifier came back with: %d, the real answer is: %d' % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print('the total error rate is: %f' % (errorCount / float(numTestVecs)))


datingClassTest()
print('**********')


def classifyPerson():
    resultList = ['not at all', 'in small', 'in large']
    percentTats = float(input('percentage of time spent playing video games?'))
    ffMiles = float(input('frequent flier miles earned per year?'))
    iceCream = float(input('liters of ice cream consumed per year?'))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = np.array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print('you will probably like this person: ', resultList[classifierResult - 1])


# classifyPerson()

def img2vector(filename):
    returnVect = np.zeros((1, 1024))
    with open(filename) as fr:
        for i in range(32):
            lineStr = fr.readline()
            for j in range(32):
                returnVect[0, 32 * i + j] = int(lineStr[j])
        return returnVect


testVector = img2vector('./digits/testDigits/0_13.txt')
print(testVector[0, 0:31])
print('*********')


def handwritingClassTest():
    import os
    hwLables = []
    trainingfileList = os.listdir('./digits/trainingDigits')
    m = len(trainingfileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingfileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLables.append(classNumStr)
        trainingMat[i, :] = img2vector('./digits/trainingDigits/%s' % fileNameStr)
    testFileList = os.listdir('./digits/testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('./digits/testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLables, 3)
        print('the classifier came back with: %d, the real answer is: %d' % (classifierResult, classNumStr))
        if (classifierResult != classNumStr):
            errorCount += 1.0
    print('\nthe total number of errors is: %d' % errorCount)
    print('\nthe total error rate is: %f' % (errorCount / float(mTest)))

handwritingClassTest()
print('***********')
