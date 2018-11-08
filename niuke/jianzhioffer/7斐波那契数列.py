'''
斐波那契数列，动态规划
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
时间复杂度O（n），空间复杂度O（n）
'''

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        else:
            s=[]
            s.append(1)
            s.append(1)
            for i in range(2,n):
                s.append(s[i-1]+s[i-2])
            return s[n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(4))