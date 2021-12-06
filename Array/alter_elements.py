#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
from collections import Counter

"""
Questions:
453. Minimum Moves to Equal Array Elements
665. Non-decreasing Array
283. Move Zeroes
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

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minMoves(self, nums: List[int]) -> int:
        cnt = sum(nums) - len(nums) * min(nums)
        return cnt

    # Method2: The recursion version(Have maximum recursion depth issues)
    def __init__(self):
        self.cnt = 0

    def minMoves1(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return self.cnt
        # sort the nums by descending order
        nums.sort(reverse=True)
        new_nums = [nums[0]] + [i+1 for i in nums[1:]]

        self.cnt += 1
        return self.minMoves1(new_nums)

    """
    665. Non-decreasing Array
    https://leetcode.com/problems/non-decreasing-array/
    
    >>> nums = [4,2,3]
    >>> Solution().checkPossibility(nums)
    >>> true
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def checkPossibility(self, nums: List[int]) -> bool:
        length_nums = len(nums)
        cnt = 0

        # prevent index exceed range
        nums.extend([float("inf"), float("inf")])

        if length_nums <= 2:
            return True
        # Two situation will be False
        for i in range(1, length_nums):
            if nums[i-1] > nums[i]:
                cnt += 1
            elif nums[i+1] < nums[i-1] and nums[i+2] < nums[i]:
                # (1).2 increase connect by 1 decrease
                return False
        return cnt < 2  # (2).More than 2 decrease

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def checkPossibility1(self, nums: List[int]) -> bool:
        nums_1, nums_2 = nums[:], nums[:]
        # find the wrong order pair, either modify the first one or second one
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums_1[i] = nums[i + 1]
                nums_2[i + 1] = nums[i]
                break
        return nums_1 == sorted(nums_1) or nums_2 == sorted(nums_2)
    """
    283. Move Zeroes
    https://leetcode.com/problems/move-zeroes/

    >>> nums = [0,1,0,3,12]
    >>> Solution().moveZeroes(nums)
    >>> [1,3,12,0,0]
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # Keep swap the no_zero_value with the first_zero (Two pointer)
        zero_1st_idx = 0

        for p in range(len(nums)):
            if nums[p] != 0:
                nums[p], nums[zero_1st_idx] = nums[zero_1st_idx], nums[p]
                zero_1st_idx += 1  # always point to the first zero of the array

        return nums
