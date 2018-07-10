'''
我们称利用svd的方法为 隐性语义索引（Latent Semantic Indexing,LSI）或(Latent Semantic Analysis,LSA)

简单版本的推荐系统能够计算项或者人之间的相似度。更先进的方法则先利用SVD从数据中构建一个主题空间，然后在该空间下计算
其相似度。
'''

import numpy as np

U, Sigma, VT = np.linalg.svd([[1,1],[7,7]])
print(U)

'''
计算距离的方法，皮尔逊相关系数（Pearson correlation）
余弦相似度
    cos theta = A*B/(|A|_2*|B|_2)
欧氏距离
'''
def ecludSim(inA, inB):
    return 1.0/(1.0+np.linalg.norm(inA-inB))

def pearsSim(inA, inB):
    if len(inA) < 3:
        return 1.0
    return 0.5 + 0.5*np.corrcoef(inA, inB, rowvar=0)[0][1]

def cosSim(inA, inB):
    num = float(inA.T*inB)
    denom = np.linalg.norm(inA)*np.linalg.norm(inB)
    return 0.5+0.5*(num/denom)


def loadExData():
    return[[0, 0, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1],
           [1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 1, 0, 0]]

myMat = np.mat(loadExData())
from sklearn.model_selection import cross_val_score

