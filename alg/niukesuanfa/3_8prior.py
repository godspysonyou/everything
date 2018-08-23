def heapAdjust(A,i,size):
    # 对所有的父亲节点
    if i<size/2:
        left = 2*i+1
        right = 2*i+2
        max = i
        if left<size and compare(A[left], A[max]):
            max = left
        if right<size and compare(A[right], A[max]):
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

def compare(str1, str2):
    if str1+str2>str2+str1:
        return True
    return False
class Prior:
    def findSmallest(self, strs, n):
        treeBuild(strs, n)
        for i in range(0,n)[::-1]:
            strs[0],strs[i] = strs[i], strs[0]
            heapAdjust(strs, 0, i)
        return ''.join(strs)

if __name__ == '__main__':
    p = Prior()
    strs = ['abc','de']
    print(p.findSmallest(strs,2))
