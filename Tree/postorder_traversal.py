#!/usr/bin/env python

from typing import List, Optional
from collections import Counter, deque

"""
Questions:
145. Binary Tree Postorder Traversal
590. N-ary Tree Postorder Traversal
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    """
    145. Binary Tree Postorder Traversal
    Given the root of a binary tree, return the postorder traversal of its nodes' values.
    https://leetcode.com/problems/binary-tree-postorder-traversal/

    >>> root = [1,null,2,3]
    >>> [3,2,1]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                res.append(node.val)
        return res[::-1]

    """
    590. N-ary Tree Postorder Traversal
    Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
    
    >>> [1,null,3,2,4,null,5,6]
    >>> [5,6,3,2,4,1]
    """
    def postorder(self, root: 'Node') -> List[int]:
        pass


