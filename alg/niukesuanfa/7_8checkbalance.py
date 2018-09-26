class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CheckBalance:
    def __init__(self):
        self.res = True
    def check(self, root):
        t = self.getHeight(root, 1)
        return self.res


    def getHeight(self, root, level=1):
        if not root:
            return level
        left = self.getHeight(root.left, level+1)
        right = self.getHeight(root.right, level+1)
        if abs(left-right)>1:
            self.res = False
        return max(left,right)+1
