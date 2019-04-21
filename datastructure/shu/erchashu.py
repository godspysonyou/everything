#######
#类名称：SequenceBinaryTree
#类说明：定义一颗顺序存储的二叉树
#类释义：包含存储二叉树每一个结点的数组
#######

class SequenceBinaryTree(object):
    def __init__(self):
        self.sequenceBinaryTree=[]


#######
#类名称：LinkedBinaryTreeNode
#类说明：定义二叉树的一个结点
#类释义：分别有结点值data，该结点的左孩子LeftChild和该结点的右孩子RightChild
#######

class LinkedBinaryTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.leftChild = None
        self.rightChild = None

class TreeState(object):
    def __init__(self, binaryTreeNode, visitedFlag):
        self.binaryTreeNode = binaryTreeNode
        self.visitedFlag = visitedFlag


class ErChaShu(object):
    def __init__(self):
        pass

    #访问二叉树一个结点函数
    def visitBinaryTreeNode(self, binaryTreeNode):
        if binaryTreeNode.data is not '#':
            print(binaryTreeNode.data)

    #先序遍历二叉树的函数，递归
    def preOrder(self, root):
        if root:
            self.visitBinaryTreeNode(root)
            self.preOrder(root.leftChild)
            self.preOrder(root.rightChild)

    #先序遍历二叉树，非递归
    def preOrderNonRecursive(self, root):
        stackTreeNode = []
        tTreeNode = root
        while len(stackTreeNode) or tTreeNode:
            while tTreeNode:
                self.visitBinaryTreeNode(tTreeNode)
                stackTreeNode.append(tTreeNode)
                tTreeNode=tTreeNode.leftChild
            if len(stackTreeNode)>0:
                tTreeNode = stackTreeNode.pop()
                tTreeNode = tTreeNode.rightChild

    #中序遍历二叉树，递归
    def inOrder(self, root):
        if root:
            self.inOrder(root.leftChild)
            self.visitBinaryTreeNode(root)
            self.inOrder(root.rightChild)

    #中序遍历二叉树，非递归
    def inOrderNonRecursive(self, root):
        stackTreeNode = []
        tTreeNode = root
        while len(stackTreeNode) or tTreeNode:
            while tTreeNode:
                stackTreeNode.append(tTreeNode)
                tTreeNode = tTreeNode.leftChild
            if len(stackTreeNode)>0:
                tTreeNode = stackTreeNode.pop()
                self.visitBinaryTreeNode(tTreeNode)
                tTreeNode = tTreeNode.rightChild

    #后序遍历二叉树，递归
    def postOrder(self, root):
        if root:
            self.postOrder(root.leftChild)
            self.postOrder(root.rightChild)
            self.visitBinaryTreeNode(root)

    #后序遍历二叉树，非递归版
    def postOrderNonRecursive(self, root):
        stackTreeNode = []
        tBinaryTreeNode = root
        tTree = None
        while tBinaryTreeNode:
            tTree = TreeState(tBinaryTreeNode, 0)
            stackTreeNode.append(tTree)
            tBinaryTreeNode = tBinaryTreeNode.leftChild
        while len(stackTreeNode)>0:
            tTree = stackTreeNode.pop()
            if not tTree.binaryTreeNode.rightChild or tTree.visitedFlag==1:
                self.visitBinaryTreeNode(tTree.binaryTreeNode)
            else:
                stackTreeNode.append(tTree)
                tTree.visitedFlag=1
                tBinaryTreeNode = tTree.binaryTreeNode.rightChild
                while tBinaryTreeNode:
                    tTree = TreeState(tBinaryTreeNode, 0)
                    stackTreeNode.append(tTree)
                    tBinaryTreeNode = tBinaryTreeNode.leftChild
