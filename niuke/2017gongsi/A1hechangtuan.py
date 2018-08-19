'''
题目描述
有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，
要求相邻两个学生的位置编号的差不超过 d，使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？

输入描述:
每个输入包含 1 个测试用例。每个测试数据的第一行包含一个整数 n (1 <= n <= 50)，
表示学生的个数，接下来的一行，包含 n 个整数，按顺序表示每个学生的能力值 ai（-50 <= ai <= 50）。
接下来的一行包含两个整数，k 和 d (1 <= k <= 10, 1 <= d <= 50)。

36

7 -15 31 49 -44 35 44 -47 -23 15 -11 10 -21 10 -13 0 -20 -36 22 -13 -39 -39 -31 -13 -27 -43 -6 40 5 -47 35 -8 24 -31 -24 -1
3 31

108241

输出描述:
输出一行表示最大的乘积。
'''

n = int(input())
aList = list(map(int, input().split()))
k, d = list(map(int, input().split()))

# 能力有正有负，维护两个数组
fm = [[0] * n for i in range(k)]
fn = [[0] * n for j in range(k)]

res = 0

for i in range(n):
    fm[0][i] = aList[i]

for j in range(n):
    fn[0][j] = aList[j]

for i in range(1, k):
    for j in range(n):
        for z in range(j - 1, max(0, j - d)-1, -1):
            fm[i][j] = max(fm[i][j], max(fm[i - 1][z] * aList[j], fn[i - 1][z] * aList[j]))
            fn[i][j] = min(fn[i][j], min(fn[i - 1][z] * aList[j], fm[i - 1][z] * aList[j]))
res = max(fm[k-1])
print(res)
