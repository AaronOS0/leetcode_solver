#!/usr/bin/env python
from typing import List
from collections import Counter
from functools import reduce

"""
Questions:
482. License Key Formatting
6. Zigzag Conversion
68.
"""


class Solution:
    """
    482. License Key Formatting
    https://leetcode.com/problems/license-key-formatting/
    >>> s = "2-5g-3-J" k = 2
    >>> "2-5G-3J"
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s_str = "".join(s.upper().split('-'))
        n = len(s_str)

        if n < k:
            return s_str

        remainder = n % k
        if remainder != 0:
            first_group = s_str[:remainder]
            str_remain = s_str[remainder:]
            return first_group + "-" + "-".join([str_remain[i:i + k] for i in range(0, len(str_remain), k)])
        else:
            return "-".join([s_str[i:i + k] for i in range(0, len(s_str), k)])

    """
    6. Zigzag Conversion
    https://leetcode.com/problems/zigzag-conversion/
    >>> s = "PAYPALISHIRING", numRows = 4
    >>> "PINALSIGYAHRPI"
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)


