#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
Questions:
434. Number of Segments in a String
58. Length of Last Word
"""


class Solution:
    """
    434. Number of Segments in a String
    https://leetcode.com/problems/number-of-segments-in-a-string/

    >>> s = "Hello, my name is John"
    >>> 5
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def countSegments(self, s: str) -> int:
        return len(s.split())

    """
    58. Length of Last Word
    https://leetcode.com/problems/length-of-last-word/

    >>> s = "   fly me   to   the moon  "
    >>> 4
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.split()
        return len(new_s[-1]) if new_s else 0
