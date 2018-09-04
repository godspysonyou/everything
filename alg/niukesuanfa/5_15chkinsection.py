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
        if(not node1 and node2)or(node1 and not node2):
            return False
        elif(not node1 and not node2):
            return self.chkinternoloop(head1,head2)
        else:
            return self.chkinterloop(head1,head2)

    def chkinterloop(self, head1, head2):
        node1 = self.chkLoop(head1)
        node2 = self.chkLoop(head2)
        if (node1 == node2):
            return True
        cur = node1.next
        while (cur != node1):
            if (cur == node2):
                return True
            cur = cur.next
        return False

    def chkinternoloop(self, headA, headB):
        p = headA
        q = headB
        lenA = 0
        lenB = 0
        while p:
            lenA += 1
            p = p.next
        while q:
            lenB += 1
            q = q.next
        # 先让 A 走50步
        p = headA
        q = headB
        if lenA > lenB:
            lenC = lenA - lenB
            while lenC > 0:
                p = p.next
                lenC -= 1

            while p and q:
                if p == q:
                    return True
                p = p.next
                q = q.next
            return False
        else:
            lenC = lenB - lenA
            while lenC > 0:
                q = q.next
                lenC -= 1
            while p and q:
                if p == q:
                    return True
                p = p.next
                q = q.next
            return False