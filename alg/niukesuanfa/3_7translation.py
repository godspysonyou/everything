def reverse(l, start, end):
    while (start < end):
        #print(l[start])
        l[start], l[end] = l[end], l[start]
        start+=1
        end-=1

def rotateWord(l):
    length = len(l)
    start=0
    end= length-1
    reverse(l, start, end)
    # 用来记录单词的开始 结束
    left = 0
    right = 0
    for i in range(length):
        # 确定每个单词的位置
        if l[i]!= ' ':
            right+=1
        else:
            right-=1
            reverse(l, left, right)
            left = i+1
            right=i+1
    reverse(l,left,right-1)
    return l

class Translation:
    def stringTranslation(self, A, n, len):
        l = list(A)
        reverse(l, 0, len-1)
        reverse(l, len, n-1)
        reverse(l,0, n-1)
        return ''.join(l)

if __name__ == "__main__":
    t = Translation()
    print(t.stringTranslation('RJXJYA',6,1))