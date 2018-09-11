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
        stack = []
        cur = None
        stack.append(root)
        while (stack):
            cur = stack.pop(-1)
            self.left_list.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    def mid(self, root):
        if not root:
            return
        stack = []
        cur = root
        while(stack or cur):
            if(cur):
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                self.mid_list.append(cur.val)
                cur = cur.right

    def right(self, root):
        if not root:
            return
        cur = None
        stack1 = []
        stack2 = []
        stack1.append(root)
        while(stack1):
            cur = stack1.pop(-1)
            stack2.append(cur)
            if (cur.left):
                stack1.append(cur.left)
            if (cur.right):
                stack1.append(cur.right)
        while(stack2):
            cur = stack2.pop(-1)
            self.right_list.append(cur.val)
