class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeToString:
    def __init__(self):
        self.res = []

    def toString(self, root):
        self.first(root)
        return self.res

    def first(self, root):
        if not root:
            self.res.append('#!')
        self.res.append(str(root.val)+"!")
        self.first(root.left)
        self.first(root.right)

def t(l):
    l.append(1)
if __name__ == "__main__":
    s = (1,2)
    t(s)
    t(s)
    print(s)

