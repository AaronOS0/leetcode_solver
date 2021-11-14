#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
from collections import Counter


# For code test
class Solution:
    def hIndex(self, citations: List[int]) -> int:

       return sum([i < j for i, j in enumerate(sorted(citations, reverse=True))])


nums = [4,4,0,0]
res = Solution().hIndex(nums)
print(res)


