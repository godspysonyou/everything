# 如何从无序链表中删除重复项
# 方法二：递归法


class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def removeDupRecursion(head):
    if not head.next:
        return head
    pointer = None
    cur = head
    # 对以head.next为首的子链表删除重复的结点
    head.next = removeDupRecursion(head.next)
    pointer = head.next
    # 找出以head.next为首的子链表中与head结点相同的结点并删除
    while pointer:
        if head.data == pointer.data:
            cur.next = pointer.next
            pointer = cur.next
        else:
            pointer = pointer.next
            cur = cur.next
    return head

def removeDup(head):
    if not head:
        return
    head.next = removeDupRecursion(head.next)


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
