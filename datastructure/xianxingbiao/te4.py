# 双链表的使用，来自数据结构python语言描述
# 页码翻页小程序
from datastructure.xianxingbiao.t2 import DoubelLinkedNode, DoubleLinkedList

class DLL(DoubleLinkedList):
    def pageTurning(self):
        cNode = self.head.next
        print('您当前所在的页码为：',cNode.data)
        print('*****************')
        print('*N:向后翻页')
        print('*P:向前翻页')
        print('*Q:退出程序')
        print('*****************')
        order = input('请输入：')
        while order != 'Q':
            if order == 'N':
                if not cNode.next:
                    print('您当前位于最后一页，无法向后翻页！')
                else:
                    cNode = cNode.next
                    print('您当前所在页码为：',cNode.data)
                order = input('请输入：')
            elif order == 'P':
                if cNode.prev == self.head:
                    print('您当前位于第一页，无法向前翻页！')
                else:
                    cNode = cNode.prev
                    print('您当前所在页码为：',cNode.data)
                order = input('请输入：')
            else:
                print('您的输入有误，请重新输入！')
                order = input('请输入：')
if __name__ == '__main__':
    d2l = DLL()
    d2l.createDoubleLinkedList()
    d2l.pageTurning()

if __name__ == '__main__':
    pass