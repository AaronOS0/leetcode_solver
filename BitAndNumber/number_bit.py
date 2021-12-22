#!/usr/bin/env python
from typing import List
from collections import Counter
from functools import reduce
from math import ceil

"""
Questions:
7. Reverse Integer
9. Palindrome Number
479. Largest Palindrome Product
"""


class Solution:
    """
    7. Reverse Integer
    https://leetcode.com/problems/reverse-integer/
    >>> x = -123
    >>> -321
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self, x: int) -> int:
        max_int = 2 ** 31 - 1
        min_int = - 2 ** 31
        new_x = 0
        sign = 1

        if x < 0:
            sign = -1
            x = abs(x)

        while x != 0:
            if x > 0:
                remainder = x % 10
                x = x // 10

            new_x = new_x * 10 + remainder

        new_x = new_x * sign
        return new_x if min_int <= new_x <= max_int else 0

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse1(self, x: int) -> int:
        max_int = 2 ** 31 - 1
        min_int = - 2 ** 31
        sign = 1

        if x < 0:
            sign = -1

        new_x = sign * int(str(abs(x))[::-1])
        return new_x if min_int <= new_x <= max_int else 0

    def reverse2(self, x: int) -> int:
        max_int = 2147483647
        min_int = -2147483648
        new_x = 0

        if x > 0:
            sign = 1
        else:
            sign = -1

        while x != 0:
            if x > 0:
                remainder = x % 10
                x = x // 10

                if new_x > max_int // 10:
                    return 0
                elif new_x == max_int // 10 and remainder > 7:
                    return 0

            else:
                remainder = 10 - x % 10
                # Eg. -10
                if remainder == 10:
                    remainder = 0

                x = -(-x // 10)

                if new_x > abs(min_int) // 10:
                    return 0
                elif new_x == abs(min_int) // 10 and remainder > 8:
                    return 0

            new_x = new_x * 10 + remainder

        return sign * new_x

    """
    9. Palindrome Number
    https://leetcode.com/problems/palindrome-number/
    >>> x = -121
    >>> false
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = str(x)
        return x == x[::-1]

    """
    479. Largest Palindrome Product
    https://leetcode.com/problems/largest-palindrome-product/
    >>> n = 2
    >>> 987
    """
    # Time Complexity: O()
    # Space Complexity: O()


