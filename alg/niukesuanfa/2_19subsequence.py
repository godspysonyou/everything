class Subsequence:
    def shortestSubsequence(self, A, n):
        # 第一遍
        leftToRight = []
        rightToLeft = []
        max = -1
        min = 100000
        for i in range(n):
            if A[i]>max:
                max = A[i]
            if max>A[i]:
                leftToRight.append(i)
        for j in range(1,n)[::-1]:
            if A[j]<min:
                min = A[j]
            if min<A[j]:
                rightToLeft.append(j)
        if not leftToRight:
            return 0
        l = leftToRight[-1]
        r = rightToLeft[-1]
        return l-r+1

if __name__ == '__main__':
    s = Subsequence()
    print(s.shortestSubsequence([1,5,4,3,2,6,7],7))
    l = [1,2,3,3,8,9]
    l = [1,2,10,1,8,9]
    print(s.shortestSubsequence(l, 6))