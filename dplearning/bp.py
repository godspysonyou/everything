import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets



class bpNN:
    def __init__(self, numH, numO, learning_rate, n_iteration):
        self.numH = numH
        self.numO = numO
        self.learning_rate = learning_rate
        self.n_iteration = n_iteration

        self.weight_H = 0
        self.b_H = 0
        self.weight_O = 0
        self.b_O = 0

    def __ini_weight_b(self, x): #初始化权重和偏置
        w1 = np.random.random([self.numH, x.shape[0]]) * 0.01
        b1 = np.zeros([self.numH, 1])
        w2 = np.random.random([self.numO, self.numH]) * 0.01
        b2 = np.zeros([self.numO, 1])
        return w1, b1, w2, b2

    def sigmoid(self, value): #sigmoid函数
        y = 1.0 / (1 + np.exp(-value))
        return y

    def z_a(self, x): #计算隐层z1 = w1x + b1, a1 = sigmoid(z1), 输出层z2 = w2a1 + b2, a2 = sigmoid(z2)
        z1 = np.dot(self.weight_H, x) + self.b_H.repeat(x.shape[1]).reshape(self.numH, x.shape[1])
        a1 = self.sigmoid(z1)
        z2 = np.dot(self.weight_O, a1) + self.b_O.repeat(x.shape[1]).reshape(self.numO, x.shape[1])
        a2 = self.sigmoid(z2)
        return z1, a1, z2, a2

    def fit(self, x, y): #训练函数, BP误差传递主体
        self.weight_H, self.b_H, self.weight_O, self.b_O = self.__ini_weight_b(x)
        for i in range(self.n_iteration):
            z1, a1, z2, a2 = self.z_a(x)
            dz2 = (a2 - y)
            dw2 = np.dot(dz2, a1.T)
            db2 = dz2.sum(axis=1).reshape(self.numO,1)
            da1 = np.dot(self.weight_O.T, dz2)
            dz1 = da1 * (a1 - a1**2)
            dw1 = np.dot(dz1, x.T)
            db1 = dz1.sum(axis=1).reshape(self.numH,1)
            self.weight_H = self.weight_H - self.learning_rate * dw1
            self.b_H = self.b_H - self.learning_rate * db1
            self.weight_O = self.weight_O - self.learning_rate * dw2
            self.b_O = self.b_O - self.learning_rate * db2

    def predict(self, x): #预测函数
        z1, a1, z2, a2 = self.z_a(x)
        return a2;

X, y = datasets.make_moons(200, noise=0.2) #产生训练集
plt.figure(1) #训练集图像
plt.scatter(X[:, 0], X[:, 1], s=40, c=y, cmap=plt.cm.Spectral)


train_X = np.array(X).T
bpNN = bpNN(8, 1, 0.01, 50000)
bpNN.fit(train_X, y)
predict_y = np.floor(bpNN.predict(train_X) * 1.99999)
plt.figure(2) #用训练集预测图像
plt.scatter(X[:, 0], X[:, 1], s=40, c=predict_y, cmap=plt.cm.Spectral)


x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
h = 0.01
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = np.floor(bpNN.predict(np.c_[xx.ravel(), yy.ravel()].T) * 1.99999)
Z = Z.reshape(xx.shape)
plt.figure(3) #预测分界图像
plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)

plt.show()