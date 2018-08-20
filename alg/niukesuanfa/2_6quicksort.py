def partition(l, start, end):
    pri = l[start]
    while start<end:
        while start<end and l[end]>pri:
            end-=1
        l[start] = l[end]
        while start<end and l[start]<=pri:
            start+=1
        l[end]=l[start]
    l[start]=pri
    return start
def myqucik(l, left, right):
    if len(l)<2:
        return l
    if left<right:
        m = partition(l,left,right)
        myqucik(l,left, m-1)
        myqucik(l,m+1,right)
    return l


class QuickSort:
    def quickSort(self, A, n):
        left = 0
        right = n-1
        return myqucik(A,left,right)

if __name__ == '__main__':
    b = QuickSort()
    s = b.quickSort([54, 35, 48, 36, 27, 27, 12, 100, 46, 100], 10)
    print(s)

