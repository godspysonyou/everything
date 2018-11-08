'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        col = len(array[0])
        startRow = 0
        startCol = col - 1

        while (startRow < row and startCol >= 0):
            cur = array[startRow][startCol]
            if cur == target:
                return True
            elif cur > target:
                startCol -= 1
            else:
                startRow += 1
        return False


if __name__ == '__main__':
    array = [[1, 2, 3],
             [2, 3, 4],
             [3, 4, 5]]
    s = Solution()
    f = s.Find(2, array)
    print(f)