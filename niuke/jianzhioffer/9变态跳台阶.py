'''
变态跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
可以用右移来表示平方
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        else:
            return 1<<(number-1)

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(3))