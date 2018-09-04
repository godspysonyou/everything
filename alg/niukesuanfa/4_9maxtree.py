class MaxTree:
    def buildMaxTree(self, A, n):
        res = ['*' for i in range(n)]
        stack = []
        for i in range(n):
            while(stack and A[stack[-1]]<A[i]):
                stack.pop()

            if (not stack):
                res[i] = -1
            else:
                res[i] = stack[-1]
            stack.append(i)
        while stack:
            stack.pop()
        for i in range(n)[::-1]:
            while(stack and A[stack[-1]<A[i]]):
                stack.pop()
            if (stack and (res[i]==-1 or A[stack[-1]<A[res[i]]])):
                res[i] = stack[-1]
            stack.append(i)
        return res

if __name__ == '__main__':
    m = MaxTree()
    print(m.buildMaxTree([36,1173,934,436],4))