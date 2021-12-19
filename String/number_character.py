#!/usr/bin/env python
from typing import List
from collections import Counter

"""
Questions:
299. Bulls and Cows
412. Fizz Buzz
506. Relative Ranks
539.
553.
537.
592.
640.
38.
443.
8.
13.
12.
273.
165.
481.
"""


class Solution:
    """
    299. Bulls and Cows
    https://leetcode.com/problems/bulls-and-cows/
    >>> secret = "1807" guess = "7810"
    >>> "1A3B"
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        # cows = count of common elements - bulls
        counter_s = Counter(secret)
        counter_g = Counter(guess)
        counter_all = sum(min(counter_s[i], counter_g[i]) for i in counter_s)
        return str(bulls) + "A" + str(counter_all - bulls) + "B"

    """
    412. Fizz Buzz
    https://leetcode.com/problems/fizz-buzz/
    >>> n = 5
    >>> ["1","2","Fizz","4","Buzz"]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                lst.append("FizzBuzz")
            elif i % 3 == 0:
                lst.append("Fizz")
            elif i % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append(str(i))
        return lst

    """
    506. Relative Ranks
    https://leetcode.com/problems/relative-ranks/
    >>> score = [10,3,8,9,4]
    >>> ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lst = []
        desc_score = sorted(score, reverse=True)
        for i in score:
            pos = desc_score.index(i)
            if pos == 0:
                lst.append("Gold Medal")
            elif pos == 1:
                lst.append("Silver Medal")
            elif pos == 2:
                lst.append("Bronze Medal")
            else:
                lst.append(str(pos+1))
        return lst

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Use bucket to save each element
    def findRelativeRanks1(self, score: List[int]) -> List[str]:
        lst = [""] * len(score)
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        desc_score = sorted(enumerate(score), key=lambda x: -x[1])

        for i, (idx, _) in enumerate(desc_score):
            lst[idx] = medal[i] if i < 3 else str(i + 1)
        return lst

