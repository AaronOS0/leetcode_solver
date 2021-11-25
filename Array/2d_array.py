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

54. Spiral Matrix
59. Spiral Matrix II
498.

566.
48.
73.
289.
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

    """
    54. Spiral Matrix
    https://leetcode.com/problems/spiral-matrix/
    >>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
    >>> [1,2,3,6,9,8,7,4,5]
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        if not matrix:
            return []
        # i,j are the coordinates of the current element
        # di, dj are the move for the next elements
        i, j, di, dj = 0, 0, 0, 1
        m, n = len(matrix), len(matrix[0])

        for v in range(m * n):
            res.append(matrix[i][j])
            matrix[i][j] = ''  # assign the visited elements a different character

            # if the boundary is reached, change direction
            if matrix[(i + di) % m][(j + dj) % n] == '':
                # Top row:(0,1); Right column:(1,0); Bottom Row:(0,-1); Left column:(-1,0)
                di, dj = dj, -di

            # update the coordinates
            i += di
            j += dj

        return res

    """
    59. Spiral Matrix II
    https://leetcode.com/problems/spiral-matrix-ii/
    Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
    >>> n = 3
    >>> [[1,2,3],[8,9,4],[7,6,5]]
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        # initialize n x n matrix with ""

        res = [[0]*n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1

        for v in range(1, n * n+1):
            res[i][j] = v
            # Reach the boundary
            if res[(i+di) % n][(j+dj) % n]:
                di, dj = dj, -di

            i += di
            j += dj

        return res
