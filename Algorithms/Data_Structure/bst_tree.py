#!/usr/bin/env python

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    def __init__(self, lst=None):
        self.root = None
        if lst:
            for val in lst:
                self.insert_loop(val)

    def insert_rec(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert_rec(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert_rec(node.rchild, val)
            node.rchild.parent = node
        else:
            pass
        return node

    def insert_loop(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return

        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def search_rec(self, node, val):
        if not node:
            return None

        if val < node.data:
            return self.search_rec(node.lchild, val)
        elif val > node.data:
            return self.search_rec(node.rchild, val)
        else:
            return node

    def search_loop(self, val):
        p = self.root
        while p:
            if val > p.data:
                p = p.rchild
            elif val < p.data:
                p = p.lchild
            else:
                return p
        return None

    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # in_order traversal will return an ordered sequence
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')


tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
tree.pre_order(tree.root)
print(" ")
tree.in_order(tree.root)
print(" ")
tree.post_order(tree.root)
print(" ")
print(tree.search_loop(4).data)
