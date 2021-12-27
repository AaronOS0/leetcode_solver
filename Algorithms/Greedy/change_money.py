#!/usr/bin/env python

"""
Money: [100, 50, 20, 5, 1], five different denominations
Payment: Any value of money
"""


class Solution:
    def change_money(self, denominations: list, pay: int) -> (int, int):
        # initialize a list represent the number of each money
        num_money = [0 for _ in range(len(denominations))]
        for idx, money in enumerate(denominations):
            num_money[idx] = pay // money
            pay = pay % money
        return num_money, pay


denominations = [100, 50, 20, 5, 1]
res = Solution().change_money(denominations, 376)
print(res)
