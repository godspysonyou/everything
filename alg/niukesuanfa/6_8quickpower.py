# -*- coding:utf-8 -*-

class QuickPower:
    def getPower(self, k, N):
        # write code here
        MOD = 1000000007
        temp = k
        res = 1
        if N == 0:
            return 1
        while(N!=0):
            if(N & 1)!=0:
                res = res*temp%MOD
            temp = temp*temp%MOD
            N = N>>1
        return res