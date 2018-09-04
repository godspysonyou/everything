class Parenthesis:
    def chkParenthesis(self, A, n):
        strs = list(A)
        num=0
        for i in range(n):
            if strs[i]=='(':
                num+=1
            if strs[i]==')':
                num-=1
            if num<0:
                return False
        if num!=0:
            return False
        return True

if __name__ == '__main__':
    p = Parenthesis()
    print(p.chkParentesis('(()())',6))