#!/usr/bin/env python
from typing import List

'''
Key: Ordered and Disordered space/sub-list
'''


# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Every time, choose an element from the disordered space, insert it into ordered space
def insert_sort(lst: List) -> List:
    n = len(lst)
    # Select from the second element
    for i in range(1, n):
        tmp = lst[i]
        j = i - 1
        '''
        As long as j does not move out of the left boundary 
        and the chosen element is smaller, move the lst[j] to right hand.
        '''
        while j >= 0 and lst[j] > tmp:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = tmp  # As long as j is already ahead of the lst or lst[j] < lst[i], insert lst[i]
    return lst


res = insert_sort([0, 4, 2, 5, 1, 1, 5])
print(res)
