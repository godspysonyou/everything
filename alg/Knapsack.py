# n是物品的数量，c是书包的容量，w是每个物品的重量w=[2,2,6,5,4],v是每个物品的价值v=[6,3,5,4,6]

def Knapsack(n, c, w, v):
    res = [[-1 for j in range(c+1)] for i in range(n+1)]
    for i in range(c+1):
        res[0][i] = 0
    for j in range(n+1):
        res[j][0] = 0
    for i in range(1,n+1):
        for j in range(1,c+1):
            if j < w[i-1]:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = max(res[i-1][j], res[i-1][j-w[i-1]]+v[i-1])
    return res

def show(n,c,w,res):
    print('最大价值为：',res[n][c])
    j = c
    x = [0 for i in range(n)]
    while n>0:
        if res[n][j]>res[n-1][j]:
            x[n-1] = 1
            j-=w[n-1]
        n-=1
    print(x)

if __name__ == '__main__':
    # n = 5
    # c = 10
    # w = [2, 2, 6, 5, 4]
    # v = [6, 3, 5, 4, 6]

    n = 4
    c = 8
    w = [2,3,4,5]
    v = [3,4,5,6]
    res = Knapsack(n, c, w, v)
    show(n, c, w, res)
