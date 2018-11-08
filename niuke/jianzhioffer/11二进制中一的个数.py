'''
二进制中的一的个数
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
负数与上0xffffffff，变成1数目相等的正数
'''

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count+=1
            n = n&(n-1)
        return count

if __name__ == '__main__':
    s = Solution()
    t = s.NumberOf1(-40)
    print(t)