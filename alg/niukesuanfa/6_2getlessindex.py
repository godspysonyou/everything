class Solution:
    def getLessIndex(self, arr):
        # 数组中所有数不同
        length = len(arr)
        if not arr:
            return -1
        if length==1:
            return arr[0]
        if arr[0]<arr[1]:
            return arr[0]
        if arr[-1]<arr[-2]:
            return arr[-1]

        # 以上都不满足，说明局部极小值在mid
        # 二分
        left = 0
        right = length-1
        while left<right:
            mid = int(left+ (right-left)/2)
            if arr[mid]>arr[mid-1]:
                # 说明局部最小在左边
                right=mid-1
                pass
            elif arr[mid]>arr[mid+1]:
                left=mid+1
                pass
            else:
                return mid

if __name__ == '__main__':
    s = Solution()
    print(s.getLessIndex([10,9,8,7,15,16,17]))
