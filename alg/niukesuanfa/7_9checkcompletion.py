class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CheckCompletion:
    def chk(self, root):
        if not root:
            return False
        flag = False
        que = []
        que.append(root)
        while(que):
            top = que.pop(0)
            if (top.left):
                que.append(top.left)
            if (top.right):
                que.append(top.right)
            if (not top.left and top.right):
                return False
            if (top.left and not top.right):
                if(flag):
                    if(top.left or top.right):
                        return False
                flag = True
                continue
            if(flag):
                if (top.left or top.right):
                    return False
        return True


if __name__ == '__main__':
    s = [1,2,3,4,5]
    s.remove(0)
    print(s)