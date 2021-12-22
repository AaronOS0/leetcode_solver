#!/usr/bin/env python
from typing import List, Optional

"""
Questions:
203. Remove Linked List Elements
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    203. Remove Linked List Elements
    https://leetcode.com/problems/remove-linked-list-elements/
    >>> head = [1,2,6,3,4,5,6] val = 6
    >>> [1,2,3,4,5]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        prev = dummy_head
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head

            head = head.next
        return dummy_head.next

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Method1: Recursion
    def removeElements1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        head.next = self.removeElements1(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head