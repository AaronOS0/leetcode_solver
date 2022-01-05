#!/usr/bin/env python

"""
Linked List: item and next
Two methods:
    1. Insert from the head
    2. Insert after the end
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def print_linked_lst(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


# insert from head
def create_linked_list_from_head(lst):
    head = Node(lst[0])
    for element in lst[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


res = create_linked_list_from_head([1, 2, 3])
print_linked_lst(res)


# insert from after end
def create_linked_list_after_end(lst):
    head = Node(lst[0])
    tail = head
    for element in lst[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


res = create_linked_list_after_end([1, 2, 3])
print_linked_lst(res)
