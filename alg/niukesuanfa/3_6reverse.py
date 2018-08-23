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

class Reverse:
    def reverseSentence(self, A, n):
        l = list(A)
        rotateWord(l)
        return ''.join(l)



if __name__ == '__main__':
    r = Reverse()
    print(r.reverseSentence('pig loves dog', 13))
    # l = ['1','2','3']
    # l[0],l[2] = l[2],l[0]
    # print(l)

