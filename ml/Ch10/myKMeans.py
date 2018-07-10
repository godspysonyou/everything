'''
K-均值是发现给定数据集中的k个簇的算法。簇个数k是用户给定的，每一个簇通过其质心，即簇中所有点的中心来描述
k-均值算法的工作流程是这样的：
    首先，随机确定k个初始点作为质心。然后将数据集中的每个点分配到一个簇中，具体来讲，为每个点找距其最近的质心，
    并将其分配给该质心所对应的簇。这一步完成之后，每个簇质心更新为该簇所有点的平均值。

伪代码：
    创建k个点作为起始质心（经常是随机选择的）
    当任意一个点的簇分配结果发生改变时
        对数据集中的每个数据点
            对每个质心
                计算质心与数据点之间的距离
            将数据点分配到距其最近的簇
        对每一个簇，计算簇中所有点的均值并将均值作为质心
'''
import numpy as np

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = np.array(list(map(float, curLine)))
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return np.sqrt(np.sum(np.power(vecA-vecB, 2)))

def randCent(dataSet, k):
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k,n)))#create centroid mat
    for j in range(n):#create random cluster centers, within bounds of each dimension
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = np.mat(minJ + rangeJ * np.random.rand(k,1))
    return centroids

def test1():
    datMat = np.mat(loadDataSet('testSet.txt'))
    min1 = min(datMat[:, 0])
    min2 = min(datMat[:, 1])
    max1 = max(datMat[:, 0])
    max2 = max(datMat[:, 1])
    print(min1, min2, max1, max2)
    print(randCent(datMat, 2))
    print(distEclud(datMat[0], datMat[1]))

def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))#create mat to assign data points
                                      #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = np.inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        print(centroids)
        for cent in range(k):#recalculate centroids
            ptsInClust = dataSet[np.nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,:] = np.mean(ptsInClust, axis=0) #assign centroid to mean
    return centroids, clusterAssment

# datMat = np.mat(loadDataSet('testSet.txt'))
# myCentroids, clustAssing = kMeans(datMat,4)

'''
如何确定k的值呢
度量聚类效果的指标SEE(Sum of Squared Error 误差平方和)

二分k-均值算法
伪代码：
    将所有点看成一个簇
    当簇数目小于k时
        对于每一个簇
            计算总误差
            在给定的簇上面进行K-均值聚类（k=2）
            计算将该簇一分为二之后的总误差
        选择使得误差最小的那个簇进行划分操作
'''
def biKmeans(dataSet, k, distMeas=distEclud):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroid0 = np.mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j,1] = distMeas(np.mat(centroid0), dataSet[j,:])**2
    while (len(centList) < k):
        lowestSSE = np.inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataSet[np.nonzero(clusterAssment[:,0].A==i)[0],:]
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
            sseSplit = np.sum(splitClustAss[:,1])
            sseNotSplit = np.sum(clusterAssment[np.nonzero(clusterAssment[:,0].A!=i)[0],1])
            print('sseSplit, and notSplit: ', sseSplit,sseNotSplit)
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestclustAss = splitClustAss.copy()


