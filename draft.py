#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from typing import List
from collections import Counter


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Transform the list to string
        nums_str = "".join(map(lambda x: str(x), nums))
        # Form the regular expression
        pattern = re.compile(r'1+')
        # Get all matched sub str
        matched_sub_str = re.findall(pattern, nums_str)
        if matched_sub_str:
            return max(map(lambda x: len(x), matched_sub_str))
        else:
            return 0

nums = []
res = Solution().findMaxConsecutiveOnes(nums)
print(res)

