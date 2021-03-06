class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def getIndexOf(s, m):
    if (not s or not m or len(s)<len(m)):
        return -1
    next = getNextArray(m)
    index = 0
    mi = 0
    deng = -1
    while(index<len(s) and mi<len(m)):
        if(s[index]==m[mi]):
            index+=1
            mi+=1
        elif (next[mi]==-1):
            index+=1
        else:
            mi = next[mi]
    if len(m)==mi:
        deng = index-mi
    return deng

# 当一个字符不匹配时，就要观察这个单词前面匹配了x个，这样就可以节省x个再匹配了
# 所以next数组里当前字符位置所存放的值是前一字符所匹配（前缀后缀相等）的值
def getNextArray(ms):
    length = len(ms)
    # 第一个位置一定对应-1,只要i增加就行
    next = [-1 for i in range(length)]
    # 第二个位置一定对应0，因为前一个位置是第一个位置，第一个位置就一个元素，前缀后缀匹配必为0
    next[1] = 0
    pos = 2
    cn =0
    while pos < length:
        if ms[pos-1]==ms[cn]:
            cn+=1
            next[pos] = cn
            pos+=1
        elif (cn>0):
            cn=next[cn]
        else:
            next[pos]=0
            pos+=1
    return next


class IdenticalTree:
    # 树A是否包含树B
    # 先序列化，再用kmp
    def chkIdentical(self, A, B):
        t1Str = self.serialByPre(A)
        t2Str = self.serialByPre(B)
        return getIndexOf(t1Str, t2Str)!= -1

    def serialByPre(self, head):
        if not head:
            return '#!'
        res = str(head.val) + '!'
        res += self.serialByPre(head.left)
        res += self.serialByPre(head.right)
        return res


if __name__ == '__main__':
    print(getNextArray(['a','b','b','a','a','b','b','a','b','b','a']))
    print(getNextArray(['a', 'a', 'b']))




