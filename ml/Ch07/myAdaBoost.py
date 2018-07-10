'''
AdaBoost 组合相似的分类器来提高分类性能
bagging:
    bootstrap aggregating，从原始数据集选择S次后得到S个新数据集，意味着可以多次选择同一样本
    ，这一性质就允许新数据集中可以有重复的值，而原始数据集的某些值在新集合中则不再出现。
    S个数据集建立完成后，将某个学习算法分别作用于每个数据集就得到了S个分类器。当我们要对新数据进行
    分类时，就可以应用着S个分类器进行分类。选择分类器投票结果中最多的类别作为最后的分类结果。

boosting:
    使用的分类器类型一致。boosting是通过集中关注被已有分类器错分的那些数据来获得新的分类器。

AdaBoost:
    e = 为正确分类的样本数目/所有样本数目
    a = 1/2 ln((1-e)/e) # 分类器权重阿尔法值

计算出alpha值之后，可以对权重向量D进行更新，以使那些正确分类的样本的权重降低而错分样本的权重升高。
如果某个样本被正确分类，那么该样本的权重更改为：
    Di(t+1) = (Di(t)e^-a) / sum(D)
如果某个样本被错误分类，那么该样本的权重更改为：
    Di（t+1）= (Di(t)e^a) / sum(D)

'''
import numpy as np
def loadSimpData():
    datMat = np.matrix([[1., 2.1],
                        [2.,1.1],
                        [1.3,1.],
                        [1.,1.],
                        [2.,1.]])

    classLabels = [1.0,1.0,-1.0,-1.0,1.0]
    return datMat, classLabels

datMat, classLabels = loadSimpData()
'''
将最小错误率minError设为+00
对数据集中的每一个特征（第一层循环）:
    对每一个步长（第二层循环）:
        对每一个不等号（第三层循环）:
            建立一棵单层决策树并利用加权数据集对它进行测试
            如果错误率低于minError,则将当前单层决策树设为最佳单层决策树。
返回最佳单层决策树
'''
def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    retArray = np.ones((np.shape(dataMatrix)[0],1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:,dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:,dimen] > threshVal] = -1.0
    return retArray

def buildStump(dataArr,classLabels,D):
    dataMatrix = np.mat(dataArr); labelMat = np.mat(classLabels).T
    m,n = np.shape(dataMatrix)
    numSteps = 10.0; bestStump = {}; bestClasEst = np.mat(np.zeros((m,1)))
    minError = np.inf #init error sum, to +infinity
    for i in range(n):#loop over all dimensions
        rangeMin = dataMatrix[:,i].min(); rangeMax = dataMatrix[:,i].max();
        stepSize = (rangeMax-rangeMin)/numSteps
        for j in range(-1,int(numSteps)+1):#loop over all range in current dimension
            for inequal in ['lt', 'gt']: #go over less than and greater than
                threshVal = (rangeMin + float(j) * stepSize)
                predictedVals = stumpClassify(dataMatrix,i,threshVal,inequal)#call stump classify with i, j, lessThan
                errArr = np.mat(np.ones((m,1)))
                errArr[predictedVals == labelMat] = 0
                weightedError = D.T*errArr  #calc total error multiplied by D
                print("split: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (i, threshVal, inequal, weightedError))
                if weightedError < minError:
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump,minError,bestClasEst

D = np.mat(np.ones((5,1))/5)
#buildStump(datMat, classLabels, D)

'''
对每次迭代：
    利用buildStump()函数找到最佳的单层决策树
    将最佳单层决策树加入到单层决策树数组
    计算alpha
    计算新的权重向量D
    更新累计类别估计值
    如果错误率等于0.0，则退出循环
'''

def adaBoostTrainDS(dataArr,classLabels,numIt=40):
    weakClassArr = []
    m = np.shape(dataArr)[0]
    D = np.mat(np.ones((m,1))/m)   #init D to all equal
    aggClassEst = np.mat(np.zeros((m,1)))
    for i in range(numIt):
        bestStump,error,classEst = buildStump(dataArr,classLabels,D)#build Stump
        #print "D:",D.T
        alpha = float(0.5*np.log((1.0-error)/max(error,1e-16)))#calc alpha, throw in max(error,eps) to account for error=0
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)                  #store Stump Params in Array
        #print "classEst: ",classEst.T
        expon = np.multiply(-1*alpha*np.mat(classLabels).T,classEst) #exponent for D calc, getting messy
        D = np.multiply(D,np.exp(expon))                              #Calc New D for next iteration
        D = D/D.sum()
        #calc training error of all classifiers, if this is 0 quit for loop early (use break)
        aggClassEst += alpha*classEst
        #print "aggClassEst: ",aggClassEst.T
        aggErrors = np.multiply(np.sign(aggClassEst) != np.mat(classLabels).T,np.ones((m,1)))
        errorRate = aggErrors.sum()/m
        print("total error: ",errorRate)
        if errorRate == 0.0: break
    return weakClassArr,aggClassEst

adaBoostTrainDS(datMat, classLabels,9)