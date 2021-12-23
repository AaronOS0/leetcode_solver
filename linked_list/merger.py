#!/usr/bin/env python
from typing import Optional

"""
Questions:
21. Merge Two Sorted Lists
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    21. Merge Two Sorted Lists
    https://leetcode.com/problems/merge-two-sorted-lists/
    >>> list1 = [1,2,4] list2 = [1,3,4]
    >>> [1,1,2,3,4,4]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Method1: Iteratively choose the next ListNode
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr = dummy_head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        return dummy_head.next

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Method2: Recursively choose the next ListNode
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists1(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists1(list1, list2.next)
            return list2



