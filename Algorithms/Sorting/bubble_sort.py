#!/usr/bin/env python

"""
Key: Ordered and Disordered space/sub-list
"""


# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Every time, move a largest element to the relative last
def bubble_sort(lst: list) -> list:
    n = len(lst)
    # Traverse totally (n - 1) times. Because the last element don't need to move
    for i in range(n - 1):
        # Traverse the disordered sub-list/space
        for j in range(n - 1 - i):
            # Exchange position
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# Time Complexity: O(n^2)
# Space Complexity: O(1)
# If the there is no exchange during a traverse, list is sorted.
def bubble_sort_edition(lst: list) -> list:
    n = len(lst)
    for i in range(n - 1):
        exchange = False
        for j in range(n - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                exchange = True
        if not exchange:
            return lst
    return lst


res1 = bubble_sort([3, 5, 1, 2, 1, 0])
res2 = bubble_sort_edition([3, 5, 1, 2, 1, 0])
print(res1, '\n', res2)
