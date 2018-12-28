# -*- coding: utf-8 -*-

import heapq

__author__ = u'ckm'


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @property
    def is_leaf(self):
        return (not self.data) or \
               (all(not bool(c) for c, p in self.children))

    def preorder(self):
       if not self:
           return

       yield self

       if self.left:
           for x in self.left.preorder():
               yield x

       if self.right:
           for x in self.right.preorder():
               yield x

    def inorder(self):
        if not self:
            return
        if self.left:
            for x in self.left.inorder():
                yield x

        yield self

        if self.right:
            for x in self.right.inorder():
                yield x

    def postorder(self):
        if not self:
            return

        if self.left:
            for x in self.left.postorder():
                yield x

        if self.right:
            for x in self.right.postorder():
                yield x

        yield self

    @property
    def children(self):
        if self.left and self.left.data is not None:
            yield self.left, 0
        if self.right and self.right.data is not None:
            yield self.right, 1


    def set_child(self, index, child):
        if index == 0:
            self.left = child
        else:
            self.right = child

    def height(self):
        min_height = int(bool(self))
        return max
