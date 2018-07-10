'''
ID3的做法是每次选取当前最佳的特征来分割数据，并按照该特征的所有可能取值来切分。也就是说，如果一个特征有4中取值，那么数据将会
被切成4分。一旦安某特征切分后，该特征在之后的算法执行过程中将不会再起作用，所以有观点认为这种切分方式过于迅速。另外一种方法是
二元切分法，即每次把数据集切分成两份。如果数据的某特征值等于切分所要求的值，那么这些数据就进入树的左子树，反之则进入树的右子树。

除了切分过于迅速外，ID3还存在另一个问题，他不能直接处理连续型特征，只有实现将连续型特征转换成离散型，才能在ID3算法中使用。但
这种转换过程会破坏连续型变量的内在性质。而使用二分切分法则易于对树构建过程进行调整以处理连续型特征。
具体的处理方法是：
    如果特征值大于给定值就走左子树，否则就走右子树。另外，二元切分法也节省了树的构建时间（但这点意义也不是特别大，因为这些树构建一般
    是离线完成，时间并非需要重点关注的因素）
'''

import numpy as np
class treeNode():
    def __init__(self, feat, val, right, left):
        featureTopSpliton = feat
        valueOfSplit = val
        rightBranch = right
        leftBranch = left

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat

def binSplitDataSet(dataSet, feature, value):
    mat0 = dataSet[np.nonzero(dataSet[:,feature] > value)[0],:][0]
    mat1 = dataSet[np.nonzero(dataSet[:,feature] <= value)[0],:][0]
    return mat0, mat1

def createTree(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):
    feat, val = chooseBestSplit(dataSet, feat, val)
    retTree['SpInd'] = feat
