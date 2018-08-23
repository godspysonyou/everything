class RadixSort:
    def radixSort(self, A, n):
        # 算位数
        from copy import copy
        import math
        s = max(A)
        tongshu = math.ceil(math.log10(s))
        #print(tongshu)
        tong = [[] for i in range(10)]
        for i in range(int(tongshu)): #从个位开始到最末位
            for yuansu in A:
                # 计算第i位（从右边开始的）
                t = int(yuansu/math.pow(10,i)%10) # 该放入t号桶子
                tong[t].append(yuansu)
            del A[:]
            for tongone in tong:
                A+=tongone
                del tongone[:]
        return A


if __name__ == '__main__':
    import math
    print(math.ceil(math.log10(999)))
    print(int(78/math.pow(10,2)%10))
    r = RadixSort()
    print(r.radixSort([54,35,48,36,27,12,44,44,8,14,26,17,28], 13))