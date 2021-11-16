#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
from collections import Counter

"""
Questions:
453. Minimum Moves to Equal Array Elements
665. Non-decreasing Array
283.
"""


class Solution:
    """
    453. Minimum Moves to Equal Array Elements
    https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

    >>> nums = [1,2,3]
    >>> Solution().minMoves(nums)
    >>> 3
    """
    # Method1: Transform the question to a pure math problem
    # sum(nums) + cnt * (n-1) = n * x
    # n = len(nums)
    # x = min(nums) + cnt
    def minMoves(self, nums: List[int]) -> int:
        cnt = sum(nums) - len(nums) * min(nums)
        return cnt

    # Method2: The recursion version(Have maximum recursion depth issues)
    def __init__(self):
        self.cnt = 0

    def minMoves1(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return self.cnt

        max_value = max(nums)
        max_value_index = nums.index(max_value)

        new_nums = [value + 1 if idx != max_value_index else value for idx, value in enumerate(nums)]

        self.cnt += 1
        return self.minMoves1(new_nums)

    """
    665. Non-decreasing Array
    https://leetcode.com/problems/non-decreasing-array/
    
    >>> nums = [4,2,3]
    >>> Solution().checkPossibility(nums)
    >>> true
    """
    def checkPossibility(self, nums: List[int]) -> bool:
        pass
