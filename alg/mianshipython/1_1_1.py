# 如何实现链表的逆序
# 方法一：就地逆序

class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None


def Reverse(head):
    # 判断列表是否为空
    if not head or not head.next:
        return
    cur = head.next
    next = cur.next
    pre = cur
    cur = next
    pre.next = None
    while cur.next:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    # 最后一个结点指向原来链表的尾节点
    cur.next = pre
    head.next = cur

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
