#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
from collections import Counter

"""
Questions:
645. Set Mismatch
697. Degree of an Array
448. Find All Numbers Disappeared in an Array
442. Find All Duplicates in an Array
41. First Missing Positive
274. H-Index
"""


class Solution:
    """
    645. Set Mismatch
    https://leetcode.com/problems/set-mismatch/

    >>> nums = [1,2,2,4]
    >>> Solution().findErrorNums(nums)
    >>> [2,3]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing_value = list(set(range(1, len(nums)+1)) - set(nums))[0]
        duplicate_value = Counter(nums).most_common(1)[0][0]

        return [duplicate_value, missing_value]

    """
    697. Degree of an Array
    https://leetcode.com/problems/degree-of-an-array/

    >>> nums = [1,2,2,3,1,4,2]
    >>> Solution().findShortestSubArray(nums)
    >>> 6
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = Counter(nums).most_common()
        degree = counts[0][1]
        common_num = [i[0] for i in counts if i[1] == degree]

        res = float('inf')
        for key in common_num:
            index_lst = [i[0] for i in enumerate(nums) if i[1] == key]
            min_distance = abs(index_lst[0] - index_lst[-1])

            if min_distance < res:
                res = min_distance

        return res + 1

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findShortestSubArray1(self, nums: List[int]) -> int:
        count_dic, left_dic, right_dic = {}, {}, {}

        for idx, num in enumerate(nums):
            if num not in left_dic.keys():
                left_dic[num] = idx

            right_dic[num] = idx
            count_dic[num] = count_dic.get(num, 0) + 1

        degree = max(count_dic.values())
        short_dis = len(nums)

        for num, counts in count_dic.items():
            if counts == degree:
                dis = right_dic[num] - left_dic[num] + 1
                if dis < short_dis:
                    short_dis = dis

        return short_dis

    """
    448. Find All Numbers Disappeared in an Array
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

    >>> nums = [4,3,2,7,8,2,3,1]
    >>> Solution().findDisappearedNumbers(nums)
    >>> [5,6]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing_sets = set(range(1, len(nums)+1)) - set(nums)
        return list(missing_sets)

    """
    442. Find All Duplicates in an Array
    https://leetcode.com/problems/find-all-duplicates-in-an-array/

    >>> nums = [4,3,2,7,8,2,3,1]
    >>> Solution().findDuplicates(nums)
    >>> [2,3]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [num for num, counts in Counter(nums).items() if counts == 2]

    """
    41. First Missing Positive
    https://leetcode.com/problems/first-missing-positive/

    >>> nums = [3,4,-1,1]
    >>> Solution().firstMissingPositive(nums)
    >>> 2
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        continuous_lst = range(1, len(nums)+1)
        missing = set(continuous_lst) - set(nums)

        if missing:
            return min(missing)
        else:
            return continuous_lst[-1] + 1

    """
    274. H-Index
    https://leetcode.com/problems/h-index/

    >>> nums = [3,0,6,1,5]
    >>> Solution().hIndex(nums)
    >>> 3
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def hIndex(self, citations: List[int]) -> int:

        return sum([i < j for i, j in enumerate(sorted(citations, reverse=True))])