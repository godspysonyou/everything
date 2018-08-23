def heapadjust(A, i, size):
    left = 2*i+1
    right = 2*i+2
    min = i
    if i < size/2:
        if left<size and A[min]>A[left]:
            min = left
        if right<size and A[min]>A[right]:
            min = right
        if min!=i:
            A[i],A[min] = A[min],A[i]
            heapadjust(A,min,size)
def buildheap(A, size):
    for i in range(int(size/2))[::-1]:
        heapadjust(A,i,size)
    return A


class ScaleSort:
    def sortElement(self, A, n, k):
        heap = buildheap(A[:k],k)
        for i in range(k,n):
            A[i-k] = heap[0]
            heap[0] = A[i]
            heapadjust(heap,0,k)
        for i in range(n-k,n):
            A[i] = heap[0]
            heap[0],heap[k-1] = heap[k-1],heap[0]
            k-=1
            heapadjust(heap,0,k)
        return A


if __name__ == '__main__':
    # r = ScaleSort()
    # print(r.sortElement([1,2,4,3,5,6,7,8,9,10,11,12,13,14,15,16], 13,4))
    c = ScaleSort()
    print(c.sortElement([2,1,3,5,4,6,8,7,9,10,12,11,13,15,14],15,3))


