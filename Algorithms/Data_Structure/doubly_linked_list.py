#!/usr/bin/env python

"""
Doubly linked list:
 item
 next
 prior
"""


class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prior = None


node = Node(2)
node.next = Node(3)
node.prior = Node(1)

print(node.prior.item)
