class SelectionSort:
    def selectionSort(self, A, n):
        for i in range(n):
            s = min(A[i:])
            t = A[i:].index(s)
            A[i], A[i+t] = A[i+t], A[i]
        return A

if __name__ == '__main__':
    b = SelectionSort()
    s = b.selectionSort([1,2,5,3,4,4],5)
    print(s)