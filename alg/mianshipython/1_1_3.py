# 如何实现链表的逆序
# 方法三：插入法

class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def Reverse(head):
    # 判断链表是否为空
    if not head or not head.next:
        return
    cur = head.next.next
    head.next.next = None
    while cur:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next

if __name__ == "__main__":
    i = 1
    head = LNode(None)
    head.next = None
    tmp = None
    cur = head
    # 构造单链表
    while i < 8:
        tmp = LNode(i)
        #tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print("逆序前：")
    cur = head.next
    while cur:
        print(cur.data)
        cur = cur.next

    print("\n逆序后：")
    Reverse(head)
    cur = head.next
    while cur:
        print(cur.data)
        cur = cur.next


'''
引申：
1）不带头结点，用方法2中的RecursiveReverse，或者用插入法
2）从尾到头输出链表
    1.就地逆序+顺序输出 这样改变了原链表的结构
    2.栈
    3.递归输出
        def ReversePrint(firstNode):
            if not firstNode:
                return
            ReversePrint(firstNode.next)
            print(firstNode.data)
'''