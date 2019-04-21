# 广义表，表尾是出第一个元素以外剩余元素组成的表，因此广义表的表尾一定是一个广义表

class GLNode:
    def __init__(self):
        self.tag = 1
        self.union = None
        self.next = None


class GList:
    # 创建广义表的函数
    def createGList(self, Table):
        tTable = None
        if len(Table) > 0:
           tTable = Table.pop(0)
           tGLNode = GLNode()
           if tTable=="(":
               tGLNode.tag=1
               tGLNode.union = self.createGList(Table)
           elif tTable==')' or tTable=='#':
               tGLNode = None
           else:
               tGLNode.tag=0
               tGLNode.union = tTable
        else:
            tGLNode = None
        if len(Table) > 0:
            tTable=Table.pop(0)
        if tGLNode!=None:
            if tTable==',':
                tGLNode.next = self.createGList(Table)
            else:
                tGLNode.next = None
        return tGLNode

    # 获取广义表表头
    def getGListHead(self, GList):
        import copy
        if GList!=None and GList.union!=None:
            head = copy.deepcopy(GList.union)
            head.next = None
            return head
        else:
            print('无法获取表头！')

    # 获取广义表表尾
    def getListTail(self, GList):
        import copy
        if GList!=None and GList.union!=None:
            tail = copy.deepcopy(GList.union.next)
            return tail
        else:
            print('无法获取表尾')

    # 遍历广义表的函数
    def traverseGList(self, GList):
        if GList!=None:
            if GList.tag == 0:
                print(GList.union, end=" ")
            else:
                print('(',end='')
                if GList.union==None:
                    print('#',end=' ')
                else:
                    self.traverseGList(GList.union)
                print(')',end=' ')
            if GList.next!=None:
                print(',',end=' ')
                self.traverseGList(GList.next)
