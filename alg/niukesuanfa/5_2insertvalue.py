class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class InsertValue:
    def insert(self, A, nxt, val):
        if not A:
            return val
        head = ListNode(A[0])
        p = head
        for i in range(1,len(A)):
            temp = ListNode(A[i])
            p.next = temp
            p = p.next
        #p.next = head
        pre = head
        cur = head.next
        temp = ListNode(val)
        while cur!=None:
            if pre.val<=val<cur.val:
                # 插入
                pre.next=temp
                temp.next=cur
                return head
            else:
                pre = pre.next
                cur = cur.next
        pre.next = temp
        if temp.val<=head.val:
            temp.next = head
            head = temp
            pre.next = None
        return head

if __name__ == '__main__':
    i = InsertValue()
    print(i.insert([1,3,4,5,7],[1,2,3,4,0],0).val)


