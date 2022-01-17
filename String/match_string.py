#!/usr/bin/env python
from typing import List
from collections import Counter
from functools import reduce
from math import ceil

"""
Questions:
28. Implement strStr()
686. Repeated String Match
459. Repeated Substring Pattern
"""


class Solution:
    """
    28. Implement strStr()
    https://leetcode.com/problems/implement-strstr/
    >>> haystack = "hello" needle = "ll"
    >>> 2
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def strStr1(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # Method1： KMP
    # ToDo
    # https://www.zhihu.com/question/21923021

    # Method2： Slice
    def strStr2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        else:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    # from the matched position, compare the same length of needle
                    if haystack[i:i+len(needle)] == needle:
                        return i
                    else:
                        continue
            return -1

    """
    686. Repeated String Match
    https://leetcode.com/problems/repeated-string-match/
    >>> a = "abcd", b = "cdabcdab"
    >>> 3
    """
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # only two conditions need to be checked: min_rep and (min_rep + 1)
        min_rep = ceil(len(b) / len(a))
        if b in a * min_rep:
            return min_rep
        elif b in a * (min_rep + 1):
            return min_rep + 1
        else:
            return -1

    """
    459. Repeated Substring Pattern
    https://leetcode.com/problems/repeated-substring-pattern/
    >>> s = "abcabcabcabc"
    >>> true
    """
    # Time Complexity: O()
    # Space Complexity: O()
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
