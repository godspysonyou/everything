# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ChkIntersection:

    def chkLoop(self, head):
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
        return fast

    def chkInter(self, head1, head2, adjust0, adjust1):
        # write code here
        node1 = self.chkLoop(head1)
        node2 = self.chkLoop(head2)
        if (node1==node2):
            return True
        cur = node1.next
        while(cur!=node1):
            if (cur==node2):
                return True
            cur = cur.next
        return False