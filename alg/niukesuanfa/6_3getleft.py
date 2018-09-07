class LeftMostAppearance:
    def findPos(self, arr, n, num):
        if n==0:
            return -1
        if n==1:
            if arr[0]==num:
                return 0
            else:
                return -1

        left = 0
        right = n-1
        res = -1
        while left<=right:
            mid = int(left+(right-left)/2)
            if arr[mid]>num:
                right=mid-1
            elif arr[mid]<num:
                left=mid+1
            else:
                res=mid
                right=mid-1
        return res

if __name__ == '__main__':
    s = [0,1,3,3,3,4,5]
    l = LeftMostAppearance()
    print(l.findPos(s,7,3))

