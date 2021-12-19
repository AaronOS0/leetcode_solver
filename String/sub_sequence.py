#!/usr/bin/env python
from typing import List
from collections import Counter

"""
Questions:
392. Is Subsequence
524. Longest Word in Dictionary through Deleting
521. Longest Uncommon Subsequence I
"""


class Solution:
    """
    392. Is Subsequence
    https://leetcode.com/problems/is-subsequence/
    >>> s = "abc" t = "ahbgdc"
    >>> true
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        # Empty detection
        if not (len_t or len_s):
            return True
        elif not len_t:
            return False
        elif not len_s:
            return True

        idx = 0
        for i in range(len_t):
            if idx < len_s and t[i] == s[idx]:
                idx += 1

        return idx == len_s

    """
    524. Longest Word in Dictionary through Deleting
    https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
    >>> s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
    >>> "apple"
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        longest_word = ""

        for word in dictionary:
            if self.is_subsequence(s, word):
                len_word, len_longest_word = len(word), len(longest_word)
                # word < longest_word: smallest lexicographical order.
                if len_word > len_longest_word or (len_word == len_longest_word and word < longest_word):
                    longest_word = word
        return longest_word

    # whether word is a subsequence of s
    def is_subsequence(self, s, word):
        idx = 0
        len_s, len_word = len(s), len(word)
        for i in range(len_s):
            if idx < len_word and s[i] == word[idx]:
                idx += 1

        return idx == len_word

    """
    521. Longest Uncommon Subsequence I
    https://leetcode.com/problems/longest-uncommon-subsequence-i/
    >>> a = "aba", b = "cdc"
    >>> 3
    """
    # Time Complexity: O()
    # Space Complexity: O()
    def findLUSlength(self, a: str, b: str) -> int:
        pass

