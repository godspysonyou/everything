class InsertionSort:
    def InsertionSort(self, A, n):
        for i in range(1, n):
            j = i - 1
            temp = A[i]
            while j>=0 and temp<A[j]:
                A[j+1] = A[j]
                j-=1
            A[j+1] = temp
        return A

if __name__ == '__main__':
    b = InsertionSort()
    s = b.InsertionSort([54,35,48,36,27,12],6)
    print(s)