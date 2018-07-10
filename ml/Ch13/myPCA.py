'''
在pca中，数据从原来的坐标系转换到了新的坐标系，新坐标系的选择是由数据本身决定的。第一个新坐标轴选择的是原始数据中
方差最大的方向，第二个新坐标轴的选择和第一个坐标轴正交且具有最大方差的方向。该过程一直重复，重复次数为原始数据中特征
的数目。我们会发现大部分方差都包含在最前面的几个新坐标轴中，因此，我们可以忽略余下的坐标轴，即对数据进行了降维处理。

降维主要是降低数据的复杂度，识别最重要的多个特征

PCA伪代码：
    去除平均值
    计算协方差矩阵
    计算协方差矩阵的特征值和特征向量
    将特征值从大到小排序
    保留最上面的N个特征向量
    将数据转换到上述N个特征向量构建的新空间中
'''
import numpy as np
def loadDataSet(fileName, dellim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(dellim) for line in fr.readlines()]
    datArr = [list(map(float, line)) for line in stringArr]
    return np.mat(datArr)

def pca(dataMat, topNfeat=9999999):
    '''
    沿数据最大方差方向旋转坐标轴来实现
    :param dataMat:
    :param topNfeat:
    :return:
    '''
    meanVals = np.mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals # 减去平均值
    covMat = np.cov(meanRemoved, rowvar=0) # 得到协方差矩阵
    eigVals, eigVects = np.linalg.eig(np.mat(covMat)) # 计算协方差矩阵的特征值和特征向量
    eigValInd = np.argsort(eigVals) # 将特征值从大到小排序
    eigValInd = eigValInd[:-(topNfeat+1):-1]
    redEigVects = eigVects[:,eigValInd]
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat

dataMat = loadDataSet('testSet.txt')
lowDMat, reconMat = pca(dataMat, 1)
print(np.shape(lowDMat))

