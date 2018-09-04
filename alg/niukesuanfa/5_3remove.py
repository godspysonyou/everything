class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Remove:
    def removeNode(self, pHead, delVal):
        if not pHead:
            return None
        if pHead.val==delVal:
            pHead = pHead.next
            return pHead
        pre = pHead
        cur = pHead.next
        while cur.val!=delVal:
            pre = pre.next
            cur = cur.next
        pre.next = cur.next
        return pHead

