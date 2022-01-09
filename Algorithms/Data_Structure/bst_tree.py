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

    # if we need to delete the leaf node
    def __remove_node_1(self, node):
        # whether it is root
        if node.parent is None:
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
        else:
            node.parent.rchild = None

    # obj node only have left child
    def __remove_node_21(self, node):
        # whether it is root
        if node.parent is None:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    # obj node only have right child
    def __remove_node_22(self, node):
        # whether it is root
        if node.parent is None:
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:
            node = self.search_loop(val)
            if not node:
                return False
            # leaf node
            if not node.lchild and not node.rchild:
                self.__remove_node_1()
            # only left node
            elif not node.rchild:
                self.__remove_node_21()
            # only right node
            elif not node.lchild:
                self.__remove_node_22()
            # two children: replace the node with the minimum node of right branch
            else:
                min_node = node.rchild
                while not min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # delete min_node
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
print("Preorder:")
tree.pre_order(tree.root)
print("\nInorder:")
tree.in_order(tree.root)
print("\nPostOrder:")
tree.post_order(tree.root)
print("\nSearch 4:")
print(tree.search_loop(4).data)
print("\ndelete 4:")
tree.delete(4)
print("\nSearch 4:")
print(tree.search_loop(4))
