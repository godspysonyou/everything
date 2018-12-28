# 如何从无序链表中移除重复项
# 方法一：顺序删除 双重循环

class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None


def removeDup(head):
    if not head or not head.next:
        return
    outerCur = head.next # 用于外循环，指向链表的第一个节点
    innerCur = None # 用于内层循环，来遍历outerCur后面的结点
    innerPre = None # innerCur的前驱结点
    while outerCur:
        innerCur = outerCur.next
        innerPre = outerCur
        while innerCur:
            # 找到重复结点并删除
            if outerCur.data == innerCur.data:
                innerPre.next = innerCur.next
                innerCur = innerCur.next
            else:
                innerPre = innerCur
                innerCur = innerCur.next
        outerCur = outerCur.next

if __name__ == '__main__':
    i = 1
    head = LNode(None)
    head.next = None
    tmp = None
    cur = head
    while i < 7:
        tmp = LNode(None)
        if i % 2 == 0:
            tmp.data = i + 1
        elif i % 3 == 0:
            tmp.data = i - 2
        else:
            tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print("删前：")
    cur = head.next
    while cur:
        print(cur.data)
        cur = cur.next
    removeDup(head)
    print("删后：")
    cur = head.next
    while cur:
        print(cur.data)
        cur = cur.next