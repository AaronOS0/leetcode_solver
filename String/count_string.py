#!/usr/bin/env python
from typing import List
from collections import Counter
from operator import xor
from functools import reduce

"""
Questions:
387. First Unique Character in a String
389. Find the Difference
383. Ransom Note
242. Valid Anagram
49. Group Anagrams
451. Sort Characters By Frequency
423. Reconstruct Original Digits from English
657.
551.
696.
467.
535.
"""


class Solution:
    """
    387. First Unique Character in a String
    https://leetcode.com/problems/first-unique-character-in-a-string/
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
    >>> s = "loveleetcode"
    >>> 2
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def firstUniqChar(self, s: str) -> int:
        for key, value in Counter(s).items():
            if value == 1:
                return s.index(key)
        return -1

    """
    389. Find the Difference
    https://leetcode.com/problems/find-the-difference/
    >>> s = "abcd", t = "abcde"
    >>> e
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t) - Counter(s))[0]

    # XOR solution
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findTheDifference1(self, s: str, t: str) -> str:
        return chr(reduce(xor, map(ord, s + t)))

    """
    383. Ransom Note
    https://leetcode.com/problems/ransom-note/
    >>> ransomNote = "aa", magazine = "aab"
    >>> true
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return len(Counter(ransomNote) - Counter(magazine)) == 0

    """
    242. Valid Anagram
    https://leetcode.com/problems/valid-anagram/
    >>> s = "anagram", t = "nagaram"
    >>> true
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    """
    49. Group Anagrams
    https://leetcode.com/problems/group-anagrams/
    >>> strs = ["eat","tea","tan","ate","nat","bat"]
    >>> [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            key = tuple(sorted(word))
            dict[key] = dict.get(key, []) + [word]
        return dict.values()

    """
    451. Sort Characters By Frequency
    https://leetcode.com/problems/sort-characters-by-frequency/
    >>> s = "tree"
    >>> "eert"
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def frequencySort(self, s: str) -> str:
        counter_lst = Counter(s).most_common()
        return "".join([val*cnt for val, cnt in counter_lst])

    """
    423. Reconstruct Original Digits from English
    https://leetcode.com/problems/reconstruct-original-digits-from-english/
    Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.
    >>> s = "owoztneoer"
    >>> "012"
    """
    # Time Limit Exceed
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def originalDigits(self, s: str) -> str:
        numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        counter_obj = Counter(s)
        lst = []
        while counter_obj:
            for idx, number in enumerate(numbers):
                counter_num = Counter(number)
                if len(counter_obj) == 0:
                    break
                # whether str contain 0-9
                if len(counter_num - counter_obj) == 0:
                    counter_obj -= counter_num
                    lst.append(str(idx))
        return "".join(sorted(lst))