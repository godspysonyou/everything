class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ChkLoop:
    def chkLoop1(self, head, adjust):
        if not head or not head.next:
            return -1
        quick = head #
        slow = head #
        while quick!=slow:
            if ((not quick) or (not quick.next)):
                return -1
            quick = quick.next.next
            slow = slow.next
        quick = head
        while quick!=slow:
            quick = quick.next
            slow = slow.next
        return slow.val

    def chkLoop(self, head, adjust):
        if not head:
            return -1
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                break
        if (not fast) or (not fast.next):
            return -1
        fast = head
        while fast!=slow:
            fast = fast.next
            slow = slow.next
        return fast.val

if __name__ == '__main__':
    s = ListNode(3)
    g = ListNode(3)
    p=s
    q=s
    print(s==g)