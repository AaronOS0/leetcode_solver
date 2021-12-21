#!/usr/bin/env python
from typing import List
from collections import Counter
from functools import reduce
from math import ceil

"""
Questions:
5. Longest Palindromic Substring
647. Palindromic Substrings
"""


class Solution:
    """
    5. Longest Palindromic Substring
    https://leetcode.com/problems/longest-palindromic-substring/
    >>> s = "babad"
    >>> "bab"
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""
        longest_len = 0

        # centre: n(single) + n-1(dual)
        for i in range(2*n - 1):
            # define left and right
            l = int(i / 2)
            r = l + i % 2
            # from centre expand the Palindrome
            while l >= 0 and r < n and s[r] == s[l]:
                temp = s[l:r+1]
                temp_len = len(temp)
                if temp_len > longest_len:
                    longest = temp
                    longest_len = temp_len

                l -= 1
                r += 1
        return longest

    """
    647. Palindromic Substrings
    https://leetcode.com/problems/palindromic-substrings/
    >>> s = "abc"
    >>> 3
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def countSubstrings(self, s: str) -> str:
        n = len(s)
        cnt = 0

        # centre: n(single) + n-1(dual)
        for i in range(2*n - 1):
            # define left and right
            l = int(i / 2)
            r = l + i % 2
            # from centre expand the Palindrome
            while l >= 0 and r < n and s[r] == s[l]:

                cnt += 1
                l -= 1
                r += 1

        return cnt
