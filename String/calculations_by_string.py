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

    # Method1:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def plusOne1(self, digits: List[int]) -> List[int]:

        n = len(digits)
        for idx in range(n-1, -1, -1):
            if digits[idx] != 9:
                digits[idx] += 1
                return digits
            else:
                digits[idx] = 0
        # Eg.[9,9,9]
        return [1] + n * [0]

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

    # Method1: Bit Calculations
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def addBinary1(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

    """
    415. Add Strings
    https://leetcode.com/problems/add-strings/
    >>> num1 = "456", num2 = "77"
    >>> "533"
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def addStrings(self, num1: str, num2: str) -> str:
        num1_lst, num2_lst = list(num1), list(num2)
        carry, res = 0, []

        while len(num2_lst) > 0 or len(num1_lst) > 0:
            # calculate the number in decimalism
            n1 = ord(num1_lst.pop()) - ord('0') if len(num1_lst) > 0 else 0
            n2 = ord(num2_lst.pop()) - ord('0') if len(num2_lst) > 0 else 0

            temp = n1 + n2 + carry
            carry, remainder = divmod(temp, 10)
            res.append(remainder)

        if carry:
            res.append(carry)

        return ''.join([str(i) for i in res])[::-1]

