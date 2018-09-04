class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回RandomListNode
    def Clone1(self, pHead):
        # write code here
        if not pHead:
            return pHead
        p = pHead
        while p:
            cloneOne = RandomListNode(p.label)
            cloneOne.next = p.next
            p.next = cloneOne
            p = p.next.next
        q1 = pHead
        q2 = pHead.next
        while True:
            q2.random = q1.random.next
            q1 = q1.next.next
            if not q1:
                break
            q2 = q2.next.next
            # 分流
        new = pHead
        result = pHead.next
        r = result
        while True:
            new.next = r.next
            new = new.next
            if not new:
                break
            r.next = new.next
            r = r.next
        return result

    def Clone(self, pHead):
        if (not pHead):
            return pHead
        cur = pHead
        next = None
        while cur:
            next = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = next
            cur = next
        cur = pHead
        curCopy = None
        while cur:
            next = cur.next.next
            curCopy = cur.next
            if cur.random: # cur.random 有可能指向None
                curCopy.random = cur.random.next
            else:
                curCopy.random = None
            cur = next
        res = pHead.next
        cur = pHead
        while cur:
            # split
            while cur:
                next = cur.next.next
                curCopy = cur.next
                cur.next = next
                if next:
                    curCopy.next = next.next
                else:
                    curCopy.next = None
                cur = next
        return res

if __name__ == '__main__':
    r1 = RandomListNode(1)
    r2 = RandomListNode(2)
    r3 = RandomListNode(3)
    r1.next = r2
    r2.next = r3
    r1.random = r3
    r2.random = r1
    r3.random = r2
    t = Solution()
    print(t.Clone(r1).random.label)
