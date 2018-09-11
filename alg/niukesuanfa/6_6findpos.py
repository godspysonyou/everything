# -*- coding:utf-8 -*-

class Find:
    def findPos(self, arr, n):
        # write code here
        if n == 0:
            return -1
        left = 0
        right = n - 1
        res = -1
        while (left<=right):
            if (arr[left]>left) or arr[right]<right:
                break
            mid = left + (right-left)/2
            if(arr[mid]>mid):
                right=mid-1
            elif (arr[mid]<mid):
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        return res