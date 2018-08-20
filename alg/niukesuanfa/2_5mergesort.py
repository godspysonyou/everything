def merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i<len(left):
        res.extend(left[i:])
    if j <len(right):
        res.extend(right[j:])
    return res
class MergeSort:
    def mergesort(self, A, n):
        if n==1:
            return A
        m = int((n)/2)
        left = self.mergesort(A[0:m], len(A[0:m]))
        right = self.mergesort(A[m:n], len(A[m:n]))
        return merge(left,right)

if __name__ == '__main__':
    b = MergeSort()
    s = b.mergesort([54, 35, 48, 36, 27, 12], 6)
    print(s)
