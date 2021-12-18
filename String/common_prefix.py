#!/usr/bin/env python
from typing import List

"""
Questions:
14. Longest Common Prefix
"""


class Solution:
    """
    14. Longest Common Prefix
    https://leetcode.com/problems/longest-common-prefix/

    >>> strs = ["flower","flow","flight"]
    >>> "fl"
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        cnt = 0

        if n == 1:
            return strs[0]

        # let the shortest str at the first place
        strs.sort(key=len)
        # if the shortest str == ""
        if strs[0] == "":
            return ""

        # compare each character of the first str with all the other strs' each character by order
        for idx, character in enumerate(strs[0]):
            # if all the character match
            if len(list(filter(lambda x: x[idx] == character, strs[1:]))) == n-1:
                cnt += 1
            else:
                return strs[0][:cnt]

        # if the first str have already traversed but not return
        return strs[0][:cnt]

    # Approach 1: Horizontal scanning
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        n = len(strs)
        prefix = strs[0]

        for i in range(1, n):
            prefix = self.lcp(prefix, strs[i])  # always compare two neighbors by order
            if len(prefix) == 0:
                return ""
        return prefix

    def lcp(self, str1, str2):
        length, idx = min(len(str1), len(str2)), 0
        while idx < length and str1[idx] == str2[idx]:
            idx += 1
        return str1[:idx]

    # Approach 2: Vertical scanning
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ""

        n, cnt = len(strs[0]), len(strs)

        for i in range(n):
            character = strs[0][i]
            if any((len(strs[j]) == i) or (strs[j][i] != character) for j in range(1, cnt)):
                return strs[0][:i]
        return strs[0]

    # Approach 3: Divide and Conquer
    # Time Complexity: O(n)
    # Space Complexity: O(mlog(n))
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        if not strs:
            return ""
        else:
            return self.divide_conquer(strs, 0, len(strs) - 1)

    def divide_conquer(self, strs, left, right):
        if left == right:
            return strs[left]
        else:
            mid = (left + right) // 2
            lcp_left = self.divide_conquer(strs, left, mid)
            lcp_right = self.divide_conquer(strs, mid + 1, right)
            return self.lcp(lcp_left, lcp_right)

    def lcp(self, str1, str2):
        length, idx = min(len(str1), len(str2)), 0
        while idx < length and str1[idx] == str2[idx]:
            idx += 1
        return str1[:idx]

    # Approach 4: Binary Search
    # Time Complexity: O()
    # Space Complexity: O()
    # ToDo