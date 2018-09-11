# -*- coding:utf-8 -*-

class MinValue:
    def getMin(self, arr, n):
        # write code here
        if n == 0:
            return
        if n == 1:
            return arr[0]
        l = 0
        r = n - 1
        m = int(l + (r - l) / 2)
        res = 0
        while l < r:
            if arr[l] < arr[r]:
                return arr[l]
            elif arr[l]<arr[m]:
                l = m
            elif arr[m]<arr[r]:
                r = m
            else:
                return min(arr[l:r+1])
        return min([arr[l],arr[r]])



if __name__ == '__main__':
    pass
