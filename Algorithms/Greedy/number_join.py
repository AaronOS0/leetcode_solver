#!/usr/bin/env python
from functools import cmp_to_key

"""
Description: Join number in a list to get the largest number
args:
    lst: numbers in a list
return:
    string: the largest number
"""


def xy_cmp(x: str, y: str) -> str:
    if x+y > y+x:
        return 1
    elif x+y < y+x:
        return -1
    else:
        return 0


def number_join(lst: list) -> str:
    lst_str = list(map(str, lst))
    # cmp_to_key: compare every pair of number in the list, if return Ture(1), exchange the position
    lst_str.sort(key=cmp_to_key(xy_cmp), reverse=True)
    # lst_str.sort(key=cmp_to_key(lambda x, y: int(x+y) - int(y+x)), reverse=True)  # alternative method
    return "".join(lst_str)


lst = [32, 128, 95, 1286, 6, 73]
res = number_join(lst)
print(res, type(res))
