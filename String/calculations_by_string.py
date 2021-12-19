#!/usr/bin/env python
from typing import List
from collections import Counter
from functools import reduce

"""
Questions:
66. Plus One
67. Add Binary
415. Add Strings
"""


class Solution:
    """
    66. Plus One
    https://leetcode.com/problems/plus-one/
    >>> digits = [1,2,3]
    >>> [1,2,4]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        # Transform to real number -> do calculations -> transform back
        res = int(reduce(lambda x, y: str(x)+str(y), digits)) + 1
        return list(map(int, str(res)))

    """
    67. Add Binary
    https://leetcode.com/problems/add-binary/
    >>> a = "1010", b = "1011"
    >>> "10101"
    """
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def addBinary(self, a: str, b: str) -> str:
        # binary -> decimalism -> addition -> binary
        return bin(int(a, 2) + int(b, 2))[2:]

    """
    415. Add Strings
    https://leetcode.com/problems/add-strings/
    >>> num1 = "456", num2 = "77"
    >>> "533"
    """
    # Time Complexity: O()
    # Space Complexity: O()
