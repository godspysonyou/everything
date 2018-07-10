import numpy as np


def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


def standRegres(xArr, yArr):
    xMat = np.mat(xArr);
    yMat = np.mat(yArr).T
    xTx = xMat.T * xMat
    if np.linalg.det(xTx) == 0.0:
        print('this matrix is singlar, cannot do inverse')
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws


xArr, yArr = loadDataSet('ex0.txt')


# print(xArr)

# print(standRegres(xArr, yArr))

def plot1():
    ws = standRegres(xArr, yArr)
    xMat = np.mat(xArr)
    yMat = np.mat(yArr)
    yHat = xMat * ws
    print(np.corrcoef(yHat.T, yMat))
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy * ws
    ax.plot(xCopy[:, 1], yHat)
    plt.show()


# plot1()
def lwlr(testPoint, xArr, yArr, k=1.0):
    '''
    局部加权线性回归有点像kNN，必须携带数据集
    :param testPoint:
    :param xArr:
    :param yArr:
    :param k:
    :return:
    '''
    xMat = np.mat(xArr);
    yMat = np.mat(yArr).T
    m = np.shape(xMat)[0]
    weights = np.mat(np.eye((m)))
    for j in range(m):  # next 2 lines create weights matrix
        diffMat = testPoint - xMat[j, :]  #
        weights[j, j] = np.exp(diffMat * diffMat.T / (-2.0 * k ** 2))
    xTx = xMat.T * (weights * xMat)
    if np.linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws


def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = np.shape(testArr)[0]
    yHat = np.zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat


def plot2():
    xArr, yArr = loadDataSet('ex0.txt')
    # print(yArr[0])
    # print(lwlr(xArr[0],xArr,yArr,1.0))
    # print(lwlr(xArr[0],xArr,yArr,0.001))

    yHat = lwlrTest(xArr, xArr, yArr, 0.003)
    xMat = np.mat(xArr)
    strInd = xMat[:, 1].argsort(0)
    xSort = xMat[strInd][:, 0, :]
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xSort[:, 1], yHat[strInd])
    ax.scatter(xMat[:, 1].flatten().A[0], np.mat(yArr).T.flatten().A[0], s=2, c='red')
    plt.show()

def rssError(yArr,yHatArr):
    return ((yArr-yHatArr)**2).sum()

def test1():
    abX, abY = loadDataSet('abalone.txt')
    yHat01 = lwlrTest(abX[0:99],abX[0:99],abY[0:99],0.1) # 较小的核容易造成过拟合，训练集误差小，测试机误差大
    yHat1 = lwlrTest(abX[0:99],abX[0:99],abY[0:99],1)
    yHat10 = lwlrTest(abX[0:99],abX[0:99],abY[0:99],10)

    print(rssError(abY[0:99],yHat01.T))
    print(rssError(abY[0:99],yHat1.T))
    print(rssError(abY[0:99],yHat10.T))

    yHat01 = lwlrTest(abX[100:199],abX[0:99],abY[0:99],0.1) # 较小的核容易造成过拟合
    yHat1 = lwlrTest(abX[100:199],abX[0:99],abY[0:99],1)
    yHat10 = lwlrTest(abX[100:199],abX[0:99],abY[0:99],10)

    print(rssError(abY[100:199],yHat01.T))
    print(rssError(abY[100:199],yHat1.T))
    print(rssError(abY[100:199],yHat10.T))

    ws = standRegres(abX[0:99], abY[0:99])
    yHat = np.mat(abX[100:199])*ws

    print(rssError(abY[100:199], yHat.T.A))

'''
缩减系数来理解数据
如果数据的特征比样本点还多应该怎么办。那么不能使用线性回归了
因为在计算（XTX）^-1时会出错
如果特征比样本点还多，也就是说输入数据的矩阵X不是满秩矩阵
非满秩矩阵在求逆时会出现问题
为了解决这个问题，统计学家引入了岭回归（ridge regression）
'''

def ridgeRegres(xMat, yMat, lam=0.2):
    xTx = xMat.T*xMat
    denom = xTx + np.eye(np.shape(xMat)[1])*lam
    if np.linalg.det(denom) == 0.0:
        print('This matrix is singular, cannot do inverse')
        return
    ws = denom.I*(xMat.T*yMat)
    return ws

def ridgeTest(xArr, yArr):
    xMat = np.mat(xArr)
    yMat = np.mat(yArr).T
    yMean = np.mean(yMat,0)
    yMat = yMat - yMean
    xMeans = np.mean(xMat,0)
    xVar = np.var(xMat,0)
    xMat = (xMat-xMeans)/xVar
    numTestPts = 30
    wMat = np.zeros((numTestPts,np.shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat, yMat, np.exp(i-10))
        wMat[i,:] = ws.T
    return wMat

def plot3():
    abX, abY = loadDataSet('abalone.txt')
    ridgeWeights = ridgeTest(abX, abY)
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ridgeWeights)
    plt.show()

'''
普通的最小二乘法回归会得到与岭回归一样的公式：
sigma wk方<=l
另一个缩减法lasso：
    sigma |wk|<=l
使用了绝对值代替平方和，虽然约束形式只是稍作变化，但结果却大相径庭：
在l足够小的时候，一些系数会因此被迫缩减到0，这个特性可以帮助我们
更好的理解数据。（为了在这个新的约束条件下解出回归系数，需要使用二次规划）
下面介绍一个简单的方法来得到结相似的结果--前向逐步回归
他是一种贪心算法，即每一步都尽可能减少误差，一开始，所有的权重都设为1，然后
每一步所做的决策是对某个权重增加或减少一个很小的值
'''

'''
算法
数据标准化，使其满足0均值和单位方差
在每轮迭代过程中：
    设置当前最小误差lowestError为正无穷
    对每个特征：
        增大或缩小：
            改变一个系数得到一个新的W
            计算新W下的误差
            如果误差Error小于当前最小误差lowestError：设置Wbest等于当前的W
        将W设置为新的Wbest
'''

def regularize(xMat):#regularize by columns
    inMat = xMat.copy()
    inMeans = np.mean(inMat,0)   #calc mean then subtract it off
    inVar = np.var(inMat,0)      #calc variance of Xi then divide by it
    inMat = (inMat - inMeans)/inVar
    return inMat

def stageWise(xArr,yArr,eps=0.01,numIt=100):
    xMat = np.mat(xArr); yMat=np.mat(yArr).T
    yMean = np.mean(yMat,0)
    yMat = yMat - yMean     #can also regularize ys but will get smaller coef
    xMat = regularize(xMat)
    m,n=np.shape(xMat)
    returnMat = np.zeros((numIt,n)) #testing code remove
    ws = np.zeros((n,1)); wsTest = ws.copy(); wsMax = ws.copy()
    for i in range(numIt):
        print(ws.T)
        lowestError = np.inf;
        for j in range(n):
            for sign in [-1,1]:
                wsTest = ws.copy()
                wsTest[j] += eps*sign
                yTest = xMat*wsTest
                rssE = rssError(yMat.A,yTest.A)
                if rssE < lowestError:
                    lowestError = rssE
                    wsMax = wsTest
        ws = wsMax.copy()
        returnMat[i,:]=ws.T
    return returnMat

def test2():
    xArr, yArr = loadDataSet('abalone.txt')
    # print(stageWise(xArr, yArr, 0.01, 200))
    # print(stageWise(xArr, yArr, 0.001, 5000))

    xMat = np.mat(xArr)
    yMat = np.mat(yArr).T
    xMat = regularize(xMat)
    yM = np.mean(yMat, 0)
    yMat = yMat - yM
    weights = standRegres(xMat, yMat.T)
    print(weights.T)

