#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
Questions:
485. Max Consecutive Ones
495. Teemo Attacking
414. Third Maximum Number
628. Maximum Product of Three Numbers
"""


class Solution:

    """
    485. Max Consecutive Ones
    https://leetcode.com/problems/max-consecutive-ones/

    Given a binary array nums, return the maximum number of consecutive 1's in the array.
    >>> nums = [1,1,0,1,1,1]
    >>> Solution().findMaxConsecutiveOnes(nums)
    >>> 3
    """
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        num = 0

        for i in nums:
            if i == 1:
                num += 1

            else:
                max_num = max(num, max_num)
                num = 0

        return max(num, max_num)

    """
    Method1: Also can use regular expression to solve it.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def findMaxConsecutiveOnes1(self, nums: List[int]) -> int:
        import re
        # Transform the list to string
        nums_str = "".join(map(lambda x: str(x), nums))
        # Form the regular expression
        pattern = re.compile(r'1+')
        # Get all matched sub str
        matched_sub_str = re.findall(pattern, nums_str)
        if matched_sub_str:
            return max(map(lambda x: len(x), matched_sub_str))
        else:
            return 0

    """
    495. Teemo Attacking
    https://leetcode.com/problems/teemo-attacking/
    
    >>> timeSeries = [1,4]
    >>> duration = 2
    >>> Solution().findPoisonedDuration(timeSeries, duration)
    >>> 4
    """
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        length = len(timeSeries)
        cnt = 0

        while cnt < length - 1:
            res += min(timeSeries[cnt+1] - timeSeries[cnt], duration)
            cnt += 1

        return res + duration

    """
    414. Third Maximum Number
    https://leetcode.com/problems/third-maximum-number/
    
    Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
    >>> nums = [2,2,3,1]
    >>> Solution().thirdMax(nums)
    >>> 1
    
    """
    def thirdMax(self, nums: List[int]) -> int:
        sorted_set = sorted(list(set(nums)), reverse=True)
        return sorted_set[2] if len(sorted_set) >= 3 else sorted_set[0]

    """
    628. Maximum Product of Three Numbers
    Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
    
    >>> nums = [1,2,3,4]
    >>> Solution().maximumProduct(nums)
    >>> 24
    """
    def maximumProduct(self, nums: List[int]) -> int:
        lst = sorted(nums, reverse=False)
        res1 = lst[-1] * lst[-2] * lst[-3]  # all Positive
        res2 = lst[0] * lst[1] * lst[2]  # all negative
        res3 = lst[0] * lst[1] * lst[-1]  # Mix

        return max([res1, res2, res3])