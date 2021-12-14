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
                return strs[0][:cnt] if cnt >= 0 else ""

        # if the first str have already traversed but not return
        return strs[0][:cnt] if cnt >= 0 else ""
