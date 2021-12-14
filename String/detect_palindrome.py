#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Questions:
125. Valid Palindrome
680. Valid Palindrome II
"""


class Solution:
    """
    125. Valid Palindrome
    https://leetcode.com/problems/valid-palindrome/

    >>> s = "A man, a plan, a canal: Panama"
    >>> true
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isPalindrome(self, s: str) -> bool:
        pure_s = list(filter(lambda x: x.isalnum(), s.lower()))
        return pure_s == pure_s[::-1]

    """
    680. Valid Palindrome II
    https://leetcode.com/problems/valid-palindrome-ii/

    >>> s = "A man, a plan, a canal: Panama"
    >>> true
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # delete left or right, then test whether the remaining str is Palindrome
                return s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]
            left += 1
            right -= 1

        return True

