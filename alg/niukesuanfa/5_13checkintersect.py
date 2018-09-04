class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class CheckIntersect:
    def chkIntersect(self, headA, headB):
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
                lenC-=1

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
                lenC-=1
            while p and q:
                if p == q:
                    return True
                p = p.next
                q = q.next
            return False



