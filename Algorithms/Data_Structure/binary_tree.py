#!/usr/bin/env python
from collections import deque
"""
Binary Tree: Each node has at most two children.
        E
    A       G
      C       F
    B   D

Tree Traversals:
1. Preorder
2. Inorder
3. Postorder
4. Levelorder
"""


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e


def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)


print("Preorder:")
pre_order(root)


def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)


print("\nInorder:")
in_order(root)


def post_order(root):
    if root:
        post_order(root.lchild)
        print(root.data, end=',')
        post_order(root.rchild)


print("\nPostorder:")
post_order(root)


def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=',')

        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


print("\nLevelorder:")
level_order(root)
