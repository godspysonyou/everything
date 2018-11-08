'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        length = len(s)
        kongge = 0
        for e in s:
            if e == ' ':
                kongge += 1
        newLength = length + kongge * 2
        strs = list(s)
        strs += [' ' for i in range(kongge*2)]
        newLength -= 1
        for i in range(length)[::-1]:
            if strs[i] != ' ':
                strs[newLength] = strs[i]
                newLength -= 1
            else:
                strs[newLength-2:newLength+1] = ['%', '2', '0']
                newLength -= 3
        return ''.join(strs)

if __name__ == '__main__':
    s = Solution()
    s.replaceSpace('Hello World')