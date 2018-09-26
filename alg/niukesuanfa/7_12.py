class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LongestDistance:
    def findLongest(self, root):
        if not root:
            return 0
        zuo = self.findLongest(root.left)
        you = self.findLongest(root.right)
        zhong = self.last(root.left)+self.last(root.right)+1
        return max(zuo,zhong,you)

    def last(self, root):
        if not root:
            return 0
        left = self.last(root.left)
        right = self.last(root.right)
        return max(left,right)+1

