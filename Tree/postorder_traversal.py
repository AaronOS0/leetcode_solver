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
    # Time Complexity: O()
    # Space Complexity: O()
    # Recursion version
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        def recursion(root, res):
            if root:
                recursion(root.left, res)
                recursion(root.right, res)
                res.append(root.val)

        recursion(root, res)
        return res

    # Iteration version
    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
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
    # Recursion version
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        # Empty tree
        if not root:
            return res

        def recursion(root, res):
            for child in root.children:
                recursion(child, res)
            res.append(root.val)

        recursion(root, res)
        return res

    # Iteration version
    def postorder1(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)

        return res[::-1]



