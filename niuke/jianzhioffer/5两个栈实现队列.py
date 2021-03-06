'''
两个栈实现队列
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
时间复杂度push O（1）
pop O(n)
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    s.push(4)
    print(s.pop())