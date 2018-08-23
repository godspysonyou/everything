class Solution:
    def __init__(self):
        self.ret=[]

    def DFS(self, candidates, target, start, valueslist):
        length = len(candidates)
        if target==0:
            return self.ret.append(valueslist)
        before = -1 # 设置before是为了避免这一层中有相同的初始， 如 1 1，将会产生,用 if i in list会更好
        for i in range(start,length):
            if target<candidates[i]:
                return
            if candidates[i]==before:
                continue
            before = candidates[i]
            cantemp = candidates.copy()
            cantemp.remove(candidates[i])
            self.DFS(cantemp,target-candidates[i],i,valueslist+[candidates[i]])



    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.DFS(candidates, target, 0, [])
        return self.ret


if __name__ == '__main__':
    l = [1]
    t = 1
    s = Solution()
    print(s.combinationSum2(l, t))