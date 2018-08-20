class ShellSort:
    def shellSort(self, A, n):
        step = 2
        group = int(n/2)
        while group > 0:
            for i in range(group):
                for j in range(i+group,n,group):
                    k = j-group
                    temp = A[j]
                    while k>=0 and temp<A[k]:
                        A[k+group] = A[k]
                        k-=group
                    A[k+group] = temp
            group = int(group/step)
        return A

if __name__ == '__main__':
    b = ShellSort()
    s = b.shellSort([54, 35, 48, 36, 27, 27, 12, 100, 46, 100], 10)
    print(s)

