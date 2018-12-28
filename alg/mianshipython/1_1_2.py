# 如何实现链表的逆序
# 方法二：递归法

class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def RecursiveReverse(head):
    # 如果链表为空或者只为一个元素
    if not head or not head.next:
        return head
    else:
        # 反转后面的结点
        newhead = RecursiveReverse(head.next)
        # 把当前遍历的结点加到后面结点逆序后链表的尾部
        head.next.next = head
        head.next = None
    return newhead

def Reverse(head):
    if not head:
        return
    # 获取链表的第一个结点
    firstNode = head.next
    newhead = RecursiveReverse(firstNode)
    head.next = newhead
    return newhead

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