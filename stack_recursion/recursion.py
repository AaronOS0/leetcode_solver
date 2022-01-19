#!/usr/bin/env python
from typing import List
from collections import Counter
from functools import reduce
from math import ceil
import operator
import re

"""
Questions:
385. Mini Parser
341. Flatten Nested List Iterator
394. Decode String
"""


class Solution:
    """
    385. Mini Parser
    https://leetcode.com/problems/mini-parser/
    >>> s = "[123,[456,[789]]]"
    >>> [123,[456,[789]]]
    """
    # Time Complexity: O()
    # Space Complexity: O()

    """
    341. Flatten Nested List Iterator
    https://leetcode.com/problems/flatten-nested-list-iterator/
    >>> nestedList = [[1,1],2,[1,1]]
    >>> [1,1,2,1,1]
    """
    # Time Complexity: O()
    # Space Complexity: O()

    """
    394. Decode String
    https://leetcode.com/problems/decode-string/
    >>> s = "3[a]2[bc]"
    >>> "aaabcbc"
    """
    # Method 1: Stack
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def decodeString(self, s:str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            # if c is alphabet
            else:
                res += c
        return res

    # Method 2: Recursion
    # Time Complexity: O()
    # Space Complexity: O()

