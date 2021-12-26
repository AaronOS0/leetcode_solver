#!/usr/bin/env python
from typing import List

'''
Procedure:
1. Select an element P, move it to the right position.
    * right position: elements at left hand < P < elements at right hand
2. Recursively do Step 1
'''


# Time Complexity: O(nlog(n)); O(n^2)-Worst case:[6, 5, 4, 3, 2, 1], could solve it by randomly choose the mid_val
# Space Complexity: O(1)
# Reposition the chosen value, return the index
def value_reposition(lst: List, left: int, right: int) -> int:
    mid_val = lst[left]  # Choose the first value as the boundary.
    while left < right:  # As long as there are more than one value in the list
        while left < right and lst[right] >= mid_val:  # Find the value that smaller than boundary but at right.
            right -= 1
        lst[left] = lst[right]  # Put the value on the right to left hand
        while left < right and lst[left] <= mid_val:
            left += 1
        lst[right] = lst[left]  # Put the value on the left to right hand
    lst[left] = mid_val  # left == right 
    return left  # return the index


def quick_sort(lst: List, left: int, right: int) -> List:
    if left < right:
        mid_val = value_reposition(lst, left, right)  # find the boundary(right position/index after reposition)
        quick_sort(lst, left, mid_val - 1)  # recursion on the left
        quick_sort(lst, mid_val + 1, right)  # recursion on the right
    return lst


res = quick_sort([3, 5, 1, 2, 7, 6, 0], 0, 6)
print(res)
