class Solution:
    def __init__(self):
        self.ret = []
    def DFS(self, candidates, tartget, start, valueslist): # 这个start用来控制返回值不重复
        length = len(candidates)
        if tartget == 0:
            return self.ret.append(valueslist)
        for i in range(start, length):
            if tartget<candidates[i]:
                return
            self.DFS(candidates, tartget-candidates[i], i, valueslist+[candidates[i]])

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.DFS(candidates, target, 0, [])
        return self.ret


if __name__ == '__main__':
    l = [2, 3, 5]
    t = 8
    s = Solution()
    print(s.combinationSum(l, t))
