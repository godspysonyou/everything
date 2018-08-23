class Solution:
    def __init__(self):
        self.ret = []
    def DFS(self, k, n, start, valuesList):
        if k==0 and n==0:
            return self.ret.append(valuesList)
        for i in range(start,10):
            if n<i:
                return
            if i in valuesList:
                continue
            self.DFS(k-1,n-i,i,valuesList+[i])


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.DFS(k,n,1,[])
        return self.ret

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3,9))