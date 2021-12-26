#!/usr/bin/env python
from typing import List, Tuple, Union

'''
Description: Fractional Backpack
args:
    goods:[(price, weight)...]
    capacity: the total capacity of bag
return:
    num_goods: the number of each goods
    val: total value of the bag
'''


def fractional_backpack(goods: List[Tuple], capacity: int) -> (List, Union[int, float]):
    # initialize a list represent the number of each goods
    num_goods = [0 for _ in range(len(goods))]
    val = 0  # total value of the bag
    for idx, (price, weight) in enumerate(goods):
        if capacity >= weight:
            num_goods[idx] = 1
            capacity -= weight
            val += price
        else:
            num_goods[idx] = capacity / weight
            capacity = 0
            val += num_goods[idx] * price
            break
    return num_goods, val


goods = [(60, 10), (100, 20), (120, 30)]
goods.sort(key=lambda x: x[0] / x[1], reverse=True)  # pick the most worthy(price/weight) goods fist
res = fractional_backpack(goods, 50)
print(res)
