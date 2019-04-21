######
#表示法：双亲表示法
#类名称：TreeNodeP
#类说明：定义树的一个结点
#类释义：分别有数据data和双亲结点的位置parent
######

class TreeNodeP(object):
    def __init__(self):
        self.data='#'
        self.parent='-1'

######
#表示法：孩子表示法
#类名称：TreeNodeC
#类说明：定义树的根结点
#类释义：分别有结点data和该结点的第一个孩子结点FirstChild
######

class TreeNodeC(object):
    def __init__(self):
        self.data = '#'
        self.FirstChild = None

######
#类名称：ChildNode
#类说明：定义一个孩子结点
#类释义：包括该结点在数组中的下标index及其某一个兄弟结点NextSibling

class ChildNode(object):
    def __init__(self):
        self.index = -1
        self.nextSibling = None


######
#表示法：孩子兄弟表示法
#类名称：TreeNodeCS
#类说明：定义树的一个结点
#类释义：分别有结点值data,第一个孩子结点pFirstChild和下一个兄弟结点pNextSibling

class TreeNodeCS(object):
    def __init__(self):
        self.data = '#'
        self.pFirstChild = None
        self.pNextSibling = None


