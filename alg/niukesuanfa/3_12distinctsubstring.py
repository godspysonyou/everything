class DistinctSubstring:
    def longestSubstring(self, A, n):
        if n < 0:
            return 0
        if n == 1:
            return 1
        strs = list(map(ord, list(A)))
        maps = [-1 for j in range(256)]
        len = 0
        pre = -1 # 保存上一个位置
        cur = 0
        for i in range(n):
            pre = max(pre,maps[strs[i]])
            cur = i-pre
            len = max(len, cur)
            maps[strs[i]] = i # 存map

        return len


if __name__ == '__main__':
    d = DistinctSubstring()
    print(d.longestSubstring('aabcb',5))
