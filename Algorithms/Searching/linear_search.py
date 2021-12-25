#!/usr/bin/env python
from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def linear_search(lst: List, obj: int) -> int or str:
    for idx, val in enumerate(lst):
        if val == obj:
            return idx
    return "Not Found"


res = linear_search([1, 2, 3, 4, 5], 3)
print(res)
