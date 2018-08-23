class CountSort:
    def countingSort(self, A, n):
        res = []
        maxv = max(A)
        minv = min(A)
        tong = [[] for i in range(minv, maxv-minv+2)] # 最大数减去最小数个桶
        #print(tong)
        for i in A:
            #print(tong[i])
            tong[i-minv].append(i)
        for j in tong:
            for t in j:
                res.append(t)
        return res

if __name__ == '__main__':
    c = CountSort()
    print(c.countingSort([1,2,3,5,2,3],6))
