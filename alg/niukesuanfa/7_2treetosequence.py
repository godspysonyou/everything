class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeToSequence:
    def __init__(self):
        self.left_list = []
        self.mid_list = []
        self.right_list = []
        self.result = []
    def convert(self, root):
        self.left(root)
        self.mid(root)
        self.right(root)
        self.result.append(self.left_list)
        self.result.append(self.mid_list)
        self.result.append(self.right_list)
        return self.result

    def left(self, root):
        if not root:
            return
        self.left_list.append(root.val)
        self.left(root.left)
        self.left(root.right)

    def mid(self, root):
        if not root:
            return
        self.mid(root.left)
        self.mid_list.append(root.val)
        self.mid(root.right)

    def right(self, root):
        if not root:
            return
        self.right(root.left)
        self.right(root.right)
        self.right_list.append(root.val)

