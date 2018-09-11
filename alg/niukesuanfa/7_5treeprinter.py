class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def notEmpty(queue):
    if len(queue) != 0:
        return True
    return False
class TreePrinter:
    def printTree(self, root):
        if not root:
            return root
        vecList = [] # 返回结果

        last = root # 保存当前行的最后一个
        nlast = None # 保存下一行的最后一个
        queue = [] # 一个队列
        queue.append(root)
        while(notEmpty(queue)):
            vec = []  # 保存一行结果
            while queue[0]!=last: # 直到当前层的queue[0]使我们的last指针
                # 都要进行打印（存vec）并将它们的孩子节点放入队列（如果不为None）
                cur = queue.pop(0)
                vec.append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            # 之后把最后一个也进行 打印（存vec）和放孩子节点到队列
            cur = queue.pop(0)
            vec.append(cur.val)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
            if notEmpty(queue):
                # 下一行的nlast就是队列的最后一个元素
                nlast = queue[-1] # 这里-1可能会有一个越界问题，就是万一队列为空了，就没有最后一个元素了
                # 将last指向nlast，以便继续遍历
                last = nlast
            vecList.append(vec)
        return vecList




