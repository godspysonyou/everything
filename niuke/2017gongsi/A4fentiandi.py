'''
题目描述
牛牛和 15 个朋友来玩打土豪分田地的游戏，牛牛决定让你来分田地，
地主的田地可以看成是一个矩形，每个位置有一个价值。分割田地的方法是横竖各切三刀，
分成 16 份，作为领导干部，牛牛总是会选择其中总价值最小的一份田地，
作为牛牛最好的朋友，你希望牛牛取得的田地的价值和尽可能大，你知道这个值最大可以是多少吗？
输入描述:
每个输入包含 1 个测试用例。每个测试用例的第一行包含两个整数 n 和 m（1 <= n, m <= 75），
表示田地的大小，接下来的 n 行，每行包含 m 个 0-9 之间的数字，表示每块位置的价值。
输出描述:
输出一行表示牛牛所能取得的最大的价值。
'''
N, M = map(int, input().split())
mat = [[int(c) for c in input().strip()] for i in range(N)]
left = min([min(m) for m in mat])
right = sum([sum(sum) for m in mat]) // 16 + 1
# sum grid from (x0,y0) to (x1, y1)
sums_ = [[0]*(M+1) for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        sums_[i][j] = sums_[i-1][j]+sums_[i-1][j-1]+mat[i-1][j-1]

