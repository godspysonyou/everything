from datastructure.xianxingbiao.t2 import CircularSingleLinkedList, Node

class YueSeFu(CircularSingleLinkedList):
    def getLength(self):
        cNode = self.head
        length = 0
        while cNode.next != self.head:
            length += 1
            cNode = cNode.next
        return length

    def yuesefuProblem(self, k, m):
        length = self.getLength()
        if length < 1:
            print('还没有人参与')
            return
        if k > length:
            print('k大于现在人数')
            return
        cNode = self.head.next
        pNode = self.head
        pos = 0
        while pos < k:
            pNode = cNode
            cNode = cNode.next
            pos += 1
        while length > 0:
            tansNum = m % length
            pos2 = 0
            while pos2 < tansNum:
                pos2 += 1
                pNode = cNode
                cNode = cNode.next
                # 头结点跳过
                if cNode == self.head:
                    pNode = cNode
                    cNode = cNode.next
            pNode.next = cNode.next
            print(cNode.data,'走了')
            del cNode
            length -= 1
            cNode = pNode.next
            #头结点跳过
            if cNode == self.head:
                pNode = cNode
                cNode = cNode.next
        print('结束')

if __name__ == '__main__':
    ysf = YueSeFu()
    ysf.createCircularSingleLinkedList()
    ysf.yuesefuProblem(4,20)


