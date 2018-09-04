# 用递归和栈进行栈的反转
class StackReverse:
    def reverseStack(self, A, n):
        if not A:
            return
        i = self.get(A)
        self.reverseStack(A, n)
        A.append(i)
        return A

    def get(self, A):
        result = A.pop(-1)
        if (not A):
            return result
        else:
            last = self.get(A)
            A.append(result)
            return last

if __name__ == '__main__':
    s = StackReverse()
    A = [230, 272, 224, 399, 126]
    s.reverseStack(A,5)
    print(A)

