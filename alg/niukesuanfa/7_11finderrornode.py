class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindErrorNode:
    def findError(self, root):
        ret = []
        #res = []
        self.mid(root, ret)
        jiedian_count = 0
        max1=-1
        max2=-1
        min1=-1
        min2=-1
        for i in range(1, len(ret)):
            if ret[i]<ret[i-1]:
                jiedian_count+=1
                if jiedian_count==1:
                    max1=ret[i-1]
                    min1=ret[i]
                elif jiedian_count==2:
                    max2=ret[i-1]
                    min2=ret[i]

        if jiedian_count==2:
            return min2,max1
        else:
            return min1,max1

        pass

    def mid(self, root, ret):
        if not root:
            return
        self.mid(root.left, ret)
        ret.append(root.val)
        self.mid(root.right, ret)