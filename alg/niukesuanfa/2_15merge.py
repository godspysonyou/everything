def compare(a,b):
    if a>b:
        return True
    return False
class Merge:
    def mergeAB(self, A, B, n, m):
        zhiB = m-1
        zhiA = n-1
        zhiE = m+n-1
        while zhiA>=0 and zhiB>=0:
            if compare(A[zhiA],B[zhiB]):
                A[zhiE] = A[zhiA]
                zhiE-=1
                zhiA-=1
            else:
                A[zhiE] = B[zhiB]
                zhiE-=1
                zhiB-=1
        while zhiA>=0:
            A[zhiE] = A[zhiA]
            zhiE -= 1
            zhiA -= 1
        while zhiB>=0:
            A[zhiE] = B[zhiB]
            zhiE -= 1
            zhiB -= 1
        return A

if __name__ == '__main__':
    m = Merge()
    A = [1,2,0,0]
    B = [3,4]
    print(m.mergeAB(A,B,2,2))