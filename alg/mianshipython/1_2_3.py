# 如何从无序链表中删除重复项
# 方法三：空间换时间 hashSet

class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None


def removeDup(head):
    if not head or not head.next:
        return head
    hashSet = set()
    cur = head.next
    pre = head
    while cur:
        if cur.data in hashSet:
            pre.next = cur.next
            cur = pre.next
            pass
        else:
            hashSet.add(cur.data)
            cur = cur.next
            pre = pre.next
    return head


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

'''
引申：
如何从有序链表中移除重复项
    用cur指向链表第一个结点，此时需要分为以下两种情况：
    1）如果cur.data == cur.next.data,那么删除cur.next结点
    2）如果cur.data != cur.next.data,那么继续遍历其余结点
'''