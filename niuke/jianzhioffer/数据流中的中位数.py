'''
如何得到一个数据流中的中位数？如果从数据流中读出
奇数个数值，那么中位数就是所有数值排序之后位于中间
的数值。如果从数据流中读出偶数个数值，那么中位数
就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，
使用GetMedian()方法获取当前读取数据的中位数。
'''

class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        self.data.append(num)
        self.data.sort()
    def GetMedian(self, data):
        l = len(self.data)
        if l%2==0:
            res = (self.data[l//2]+self.data[l//2-1]) / 2.0
        else:
            res = self.data[(l//2)]
        return res