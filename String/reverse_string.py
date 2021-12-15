#!/usr/bin/env python
from typing import List

"""
Questions:
344. Reverse String
541. Reverse String II
557. Reverse Words in a String III
151. Reverse Words in a String
"""


class Solution:
    """
    344. Reverse String
    https://leetcode.com/problems/reverse-string/

    >>> s = ["h","e","l","l","o"]
    >>> ["o","l","l","e","h"]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

    """
    541. Reverse String II
    https://leetcode.com/problems/reverse-string-ii/

    >>> s = "abcdefg"
    >>> k = 2
    >>> "bacdfeg"
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseStr(self, s: str, k: int) -> str:
        return "".join([s[i:i+k][::-1] + s[i+k:i+2*k] for i in range(0, len(s), 2*k)])

    """
    557. Reverse Words in a String III
    https://leetcode.com/problems/reverse-words-in-a-string-iii/

    >>> s = "Let's take LeetCode contest"
    >>> "s'teL ekat edoCteeL tsetnoc"
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseWords(self, s: str) -> str:
        return " ".join([words[::-1] for words in s.split()])

    """
    151. Reverse Words in a String
    https://leetcode.com/problems/reverse-words-in-a-string/

    >>> s = "  hello world  "
    >>> "world hello"
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
