'''
1.找零钱问题：假设只有 1 分、 2 分、五分、 1 角、二角、 五角、 1元的硬币。
在超市结账 时，如果 需要找零钱， 收银员希望将最少的硬币数找给顾客。
那么，给定 需要找的零钱数目，如何求得最少的硬币数呢？
'''


# -*- coding:utf-8 -*-


def lingqian():
    d = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]
    d_num = []
    temp = input('请输入每种零钱的个数:')
    d_num0 = temp.split(' ')
    sum = 0
    for index, i in enumerate(d_num0):
        d_num.append(int(i))
        sum += d[index] * int(i)
    lin = float(input('请输入要找的零钱'))
    if lin > sum:
        print('零钱超过总金额')

    iter = len(d) - 1
    while iter >= 0:
        if lin > d[iter]:
            n = int(lin / d[iter])
            if n >= d_num[iter]:
                n = d_num[iter]
            lin -= n * d[iter]
            print('用了%d个%f元硬币' % (n, d[iter]))
        iter -= 1


'''
2.求最大子数组之和问题：给定一个整数数组（数组元素有负有正），求其连续子数组之和的最大值
'''


def max_zi():
    s = [1, -2, 4, -3, 5, -6]
    print('定义的数组为:', s)
    s_max, s_sum = 0, 0
    start = 0
    end = 0
    for i in range(len(s)):
        s_sum += s[i]
        if s_sum >= s_max:
            s_max = s_sum
            end = i
        elif s_sum < 0:
            s_sum = 0
            start = i + 1
    print('最大子数组和为：', s_max)
    print('开始于第%d个' % (start + 1))
    print('结束于第%d个' % (end + 1))


if __name__ == "__main__":
    # lingqian()
    max_zi()
