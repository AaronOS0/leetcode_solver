#!/usr/bin/env python


# Time Complexity: O(logn)
# Space Complexity: O(1)
def binary_search(lst: list, obj: int) -> int or str:
    left = 0
    right = len(lst) - 1  # right boundary

    # if there are values in the sub list
    while left <= right:
        middle = (right + left) // 2
        if lst[middle] > obj:
            right = middle - 1
        elif lst[middle] < obj:
            left = middle + 1
        else:
            return middle
    return "Not Found"


res = binary_search([1, 2, 3, 4, 5, 6], 5)
print(res)
