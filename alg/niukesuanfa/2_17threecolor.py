def swap(A, index1, index2):
    A[index1], A[index2] = A[index2], A[index1]
class ThreeColor:
    def sortTreeColor(self, A, n):
        left = -1 # 空窗
        right = n
        index = 0
        while (index < right):
            if (A[index]==0):
                left+=1
                swap(A, left, index)
                index+=1
            elif (A[index]==2):
                right-=1
                swap(A, index, right)
            else:
                index+=1
        return A

if __name__ == '__main__':
    t = ThreeColor()
    print(t.sortTreeColor([1,0,1],3))

