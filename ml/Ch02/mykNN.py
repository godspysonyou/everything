# -*- coding: utf-8 -*-
import numpy as np
import operator

def deal_text(filename):
    with open('datingTestSet2.txt') as f:
        labels = []
        features = []
        for line in f.readlines():
            line_strip = line.strip().split()
            features.append(line_strip[:3])
            labels.append(line_strip[-1])
        features = np.array(features).astype(np.float32)
        return features, labels


def normalize(features):
    max_values = features.max(0)
    min_values = features.min(0)
    ranges = max_values - min_values
    new_features = (features-min_values) / ranges
    return new_features


def kNearestNeibor(inX, features, lables, k):
    cha = features - inX
    pingfang = cha**2
    he = pingfang.sum(axis=1)
    juli = he**0.5
    juli_index = juli.argsort()
    retMat = {}
    for i in range(k):
        vote_labels = lables[juli_index[i]]
        retMat[vote_labels] = retMat.get(vote_labels, 0) + 1
    sorted_retMat = sorted(retMat.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_retMat[0][0]




if __name__ == '__main__':
    features, labels = deal_text('datingTestSet2.txt')
    #print(features.dtype)
    features = normalize(features)
    print(kNearestNeibor(np.array([0.46,0.36,0.56]), features, labels, 3))
    # x = np.array([[1,2.,3],
    #              [2,3,4],
    #              [3,4,5]])
    # print(x.max(0))
