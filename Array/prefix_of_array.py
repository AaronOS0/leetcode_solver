#!/usr/bin/env python
from typing import List
from collections import Counter

"""
Questions:
303. Range Sum Query - Immutable
304.
238.
"""


class NumArray:
    """
    303. Range Sum Query - Immutable
    https://leetcode.com/problems/range-sum-query-immutable/

    >>> [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    >>> [null, 1, -1, -3]
    """
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def __init__(self, nums: List[int]):
        self.numArray = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.numArray[left:right + 1])

    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(left,right)
