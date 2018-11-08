class BubbleSort:
    def bubbleSort(self, A, n):
        for i in range(n-1):
            for j in range(n-1-i):
                if A[j]>A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
        return A

if __name__ == '__main__':
    b = BubbleSort()
    s = b.bubbleSort([2,1,5,3,4],5)
    print(s)