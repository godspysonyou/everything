import math
def heapAdjust(A,i,size):
    # 对所有的父亲节点
    if i<size/2:
        left = 2*i+1
        right = 2*i+2
        max = i
        if left<size and A[max]<A[left]:
            max = left
        if right<size and A[max]<A[right]:
            max = right
        if max!=i:
            A[max],A[i] = A[i], A[max]
            heapAdjust(A,max,size)
    return A

def treeBuild(A, size):
    n = len(A)
    lastp = int((n-1)/2)
    for i in range(lastp,-1,-1):
        A = heapAdjust(A, i, size)
    return A

class HeapSort:
    def heapSort(self, A, n):
        A = treeBuild(A,n)
        for i in range(n-1,-1,-1):
            A[0], A[i] = A[i], A[0]
            A = heapAdjust(A,0,i)
        return A

if __name__ == '__main__':
    b = HeapSort()
    s = b.heapSort([54, 35, 48, 36, 27, 27, 12, 100, 46, 100], 10)
    print(s)

