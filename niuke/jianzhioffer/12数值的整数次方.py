'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

# -*- coding:utf-8 -*-
class Solution:
    def Power1(self, base, exponent):
        # write code here
        start = base
        if exponent == 0:
            return 1
        if exponent<0:
            for i in range(-exponent-1):
                base=base*start
            return 1.0/base
        else:
            for i in range(exponent-1):
                base=base*start
            return base

    def Power(self, base, exponent):
        if exponent<=0:
            return 0.0
        absexponent = exponent
        if exponent < 0:
            absexponent = -exponent
        res = self.getPower(base, absexponent)
        if (exponent<0):
            res = 1.0/res
        return res

    def getPower(self, b, e):
        if (e==0):
            return 1.0
        if (e==1):
            return b
        result = self.getPower(b, e>>1)
        result *= result
        if (e&1)==1:
            result*b
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.Power(2,3))
