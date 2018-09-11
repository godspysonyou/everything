# -*- coding:utf-8 -*-
import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getDepth(root):
    depth = 0
    while (root):
        depth+=1
        root=root.left
    return depth


class CountNodes:
    def count(self, root):
        # write code here
        res = 0
        if (not root):
            return 0
        leftDepth = getDepth(root.left)
        rightDepth = getDepth(root.right)
        if (leftDepth == rightDepth):
            res+=2**leftDepth
            res += self.count(root.right)
        elif leftDepth>rightDepth:
            res+=2**rightDepth
            res+=self.count(root.left)
        return res