'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        stack = []
        p = listNode
        while p:
            stack.insert(0,p.val)
            p = p.next
        return stack

    def printListFromTailToHead1(self, listNode):
        if not listNode:
            return []
        if not listNode.next:
            return [listNode.val]
        res =[]
        p = listNode
        head = p
        #q = listNode.next
        while(p.next):
            q = p.next
            p.next = p.next.next
            q.next = head
            head = q

        p = head
        while(p):
            res.append(p.val)
            p = p.next
        return res

if __name__ == '__main__':
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode3 = ListNode(3)
    ListNode1.next = ListNode2
    ListNode2.next = ListNode3

    s = Solution()
    stack = s.printListFromTailToHead1(ListNode1)
    print(stack)