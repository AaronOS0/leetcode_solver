#!/usr/bin/env python
import re

"""
Questions:
520. Detect Capital
"""


class Solution:
    """
    520. Detect Capital
    https://leetcode.com/problems/detect-capital/

    >>> word = "FlaG"
    >>> false
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == word.capitalize()

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # [A−Z]*|[a−z]*|[A−Z][a−z]* == [A-Z]*|.[a-z]*
    def detectCapitalUse1(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word) is not None

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Detect the two situations
    def detectCapitalUse2(self, word: str) -> bool:
        n = len(word)

        if n == 1:
            return True

        # All uppercase
        if word[0].isupper() and word[1].isupper():
            for i in range(2, n):
                if not word[i].isupper():
                    return False
        # Capital + lower or all lower case
        else:
            for i in range(1, n):
                if word[i].isupper():
                    return False
        return True







