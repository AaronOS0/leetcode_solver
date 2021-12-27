#!/usr/bin/env python

"""
Key: Ordered and Disordered space/sub-list
"""


# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Every time, select the relative minimum element to append into a new lst
def select_sort(lst: list) -> list:
    new_lst = []
    n = len(lst)
    for i in range(n):
        min_value = min(lst)
        new_lst.append(min_value)
        lst.remove(min_value)
    return new_lst


# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Every time, select the relative minimum element in disordered sub-list, exchange with the last element of ordered list
def select_sort_edition(lst: list) -> list:
    n = len(lst)
    for i in range(n - 1):
        min_loc = i
        for j in range(i+1, n):
            if lst[j] < lst[min_loc]:
                min_loc = j  # Find the location of the smallest value
        if min_loc != i:
            lst[i], lst[min_loc] = lst[min_loc], lst[i]
    return lst


res1 = select_sort([1, 4, 2, 5, 1, 0, 5])
res2 = select_sort_edition([1, 4, 2, 5, 1, 0, 5])
print(res1, res2)
