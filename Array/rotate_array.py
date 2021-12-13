#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
Questions:
189. Rotate Array
396. Rotate Function
"""


class Solution:
    """
    189. Rotate Array
    https://leetcode.com/problems/rotate-array/
    >>> nums = [1,2,3,4,5,6,7]
    >>> k = 3
    >>> [5,6,7,1,2,3,4]
    """
    # Time Complexity: O(n*k)
    # Space Complexity: O(1)
    # Time Limit Exceeded
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            for j in range(len(nums) - 1, 0, -1):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            i += 1

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        # 3 times reverse to get the answer
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    """
    396. Rotate Function
    https://leetcode.com/problems/rotate-function/
    >>> nums = [4,3,2,6]
    >>> 26
    
    F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
    """
    # F(1) = F(0) - (3 * 6) + sum([4,3,2]) = F(0) - (4 * 6) + sum([4,3,2,6])
    # F(2) = F(1) - (4 * 2) + sum([4,3,2,6])
    # F(3) = F(2) - (4 * 3) + sum([4,3,2,6])
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxRotateFunction(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        total = sum(i * j for i, j in enumerate(nums))
        i = 1
        n = len(nums)

        res = total
        while i < n:
            total += (nums_sum - nums[-i] * n)
            res = max(res, total)
            i += 1
        return res
