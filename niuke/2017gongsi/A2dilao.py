'''
题目描述
给定一个 n 行 m 列的地牢，其中 '.' 表示可以通行的位置，'X' 表示不可通行的障碍，
牛牛从 (x0 , y0 ) 位置出发，遍历这个地牢，和一般的游戏所不同的是，
他每一步只能按照一些指定的步长遍历地牢，要求每一步都不可以超过地牢的边界，也不能到达障碍上。
地牢的出口可能在任意某个可以通行的位置上。牛牛想知道最坏情况下，他需要多少步才可以离开这个地牢。

输入描述:
每个输入包含 1 个测试用例。每个测试用例的第一行包含两个整数 n 和 m（1 <= n, m <= 50），
表示地牢的长和宽。接下来的 n 行，每行 m 个字符，描述地牢，地牢将至少包含两个 '.'。
接下来的一行，包含两个整数 x0, y0，表示牛牛的出发位置（0 <= x0 < n, 0 <= y0 < m，左上角的坐标为 （0, 0），
出发位置一定是 '.'）。之后的一行包含一个整数 k（0 < k <= 50）表示牛牛合法的步长数，接下来的 k 行，
每行两个整数 dx, dy 表示每次可选择移动的行和列步长（-50 <= dx, dy <= 50）

输出描述:
输出一行一个数字表示最坏情况下需要多少次移动可以离开地牢，如果永远无法离开，输出 -1。
以下测试用例中，牛牛可以上下左右移动，在所有可通行的位置.上，地牢出口如果被设置在右下角，
牛牛想离开需要移动的次数最多，为3次。

'''
N, M = map(int, input().split())
dilao = [input() for i in range(N)]
x0, y0 = map(int, input().split())
assert (0 <= x0 < N and 0 <= y0 < M)
k = map(int, input())
move = [[int(x) for x in input().split()] for i in range(k)]
num = 0
visit = [[0]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        if dilao[i][j] == '.':
            visit[i][j] = 1
            num+=1

def layer():
    res = 1
    count = 1
    tmp = []
    visit[x0][y0] = 0
    que = [[x0,y0]]
    while que:
        for x,y in que:
            for dx,dy in move:
                nx, ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<M and dilao[nx][ny]=='.' and visit[nx][ny]==1:
                    visit[nx][ny]=0
                    count+=1
                    tmp.append([nx,ny])
                if count == num:
                    return res
        que = tmp
        res+=1
    return -1

print(layer())


