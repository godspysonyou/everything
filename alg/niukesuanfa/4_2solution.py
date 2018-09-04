# 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数
class Solution:
    def __init__(self):
        self.stackdata = []
        self.stackmin = []
    def push(self, node):
        self.stackdata.append(node)
        if (not self.stackmin) or self.stackmin[-1]>node:
            self.stackmin.append(node)
        else:
            self.stackmin.append(self.stackmin[-1])
    def pop(self):
        self.stackdata.pop(-1)
        self.stackmin.pop(-1)
    def top(self):
        return self.stackdata[-1]
    def min(self):
        return self.stackmin[-1]


if __name__ == '__main__':
    pass