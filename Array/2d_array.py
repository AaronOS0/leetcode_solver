#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from collections import Counter

"""
Questions:
118. Pascal's Triangle
119. Pascal's Triangle II
661. Image Smoother
598. Range Addition II
419. Battleships in a Board
"""


class Solution:
    """
    118. Pascal's Triangle
    Given an integer numRows, return the first numRows of Pascal's triangle.
    https://leetcode.com/problems/pascals-triangle/

    >>> numRows = 5
    >>> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    """
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [1]  # list for each layer of the Pascal's triangle
        lst = []  # The Pascal's triangle

        for i in range(numRows):
            lst.append(nums)  # add the list of each layer to Pascal's triangle
            length = len(lst[i])  # The length of the previous layer
            temp = []  # temp list to save the addition from the previous layer
            if length > 1:
                for j in range(length - 1):
                    temp.append(nums[j] + nums[j + 1])

            nums = [1] + temp + [1]

        return lst

    """
    119. Pascal's Triangle II
    https://leetcode.com/problems/pascals-triangle-ii/

    >>> rowIndex = 3
    >>> [1,3,3,1]
    """
    def getRow(self, rowIndex: int) -> List[int]:
        nums = [1]  # list for each layer of the Pascal's triangle
        lst = []  # The Pascal's triangle

        for i in range(rowIndex+1):
            lst.append(nums)  # add the list of each layer to Pascal's triangle
            length = len(lst[i])  # The length of the previous layer
            temp = []  # temp list to save the addition from the previous layer
            if length > 1:
                for j in range(length-1):
                    temp.append(nums[j] + nums[j+1])

            nums = [1] + temp + [1]

        return lst[rowIndex]

    """
    661. Image Smoother
    https://leetcode.com/problems/image-smoother/
    >>> img = [[100,200,100],[200,50,200],[100,200,100]]
    >>> [[137,141,137],[141,138,141],[137,141,137]]
    """
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)  # row
        n = len(img[0])  # column
        res_lst = [[0]*n for i in range(m)]  # initialize the results with 0

        for i in range(m):
            for j in range(n):
                neighbors = [
                    img[x][y]
                    for x in (i-1, i, i+1)
                    for y in (j-1, j, j+1)
                    if 0 <= x < m and 0 <= y < n  # only if the index is valid
                    ]
                res_lst[i][j] = sum(neighbors) // len(neighbors)
        return res_lst

    """
    598. Range Addition II
    https://leetcode.com/problems/range-addition-ii/
    >>> m = 3, n = 3, ops = [[2,2],[3,3]]
    >>> 4
    """
    # Memory Limit Exceeded
    def maxCount1(self, m: int, n: int, ops: List[List[int]]) -> int:
        lst = [[0] * n for i in range(m)]  # initialize an nest list with all 0
        max_val = len(ops)
        cnt = 0

        if max_val == 0:
            return m * n

        for ops_pairs in ops:
            # put all the index of operation value in a list
            increase_lst = [[x, y] for x in range(ops_pairs[0]) for y in range(ops_pairs[1])]
            for increase_index in increase_lst:
                lst[increase_index[0]][increase_index[1]] += 1

        # traverse all the 2-D list to count the max number
        for row in lst:
            for element in row:
                if element == max_val:
                    cnt += 1

        return cnt

    # Transform the question to a mathematical solution
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n
        else:
            return min(i[0] for i in ops) * min(i[1] for i in ops)

    """
    419. Battleships in a Board
    https://leetcode.com/problems/battleships-in-a-board/
    >>> board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    >>> 2
    """
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        cnt = 0

        if m == 0:
            return 0

        for i in range(m):
            for j in range(n):
                # Count the head of the Battleships. If the above or left position is empty, that is the valid head.
                if board[i][j] == "X" and (i == 0 or board[i-1][j] == ".") and (j == 0 or board[i][j-1] == "."):
                    cnt += 1
        return cnt
